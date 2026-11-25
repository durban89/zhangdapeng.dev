+++
title = "Handling Failed Message Delivery and Local Message Recovery in RongCloud HarmonyOS SDK"
description = "Learn how to handle failed message delivery, persist message states, retry failed messages, and recover local chat history in RongCloud IM SDK for HarmonyOS."
date = 2026-11-25T15:00:00+08:00
lastmod = 2026-11-25T15:00:00+08:00
slug = "rongcloud-harmonyos-failed-message-recovery"
tags = ["HarmonyOS", "ArkTS", "RongCloud", "IM SDK", "Message Handling"]
categories = ["Development"]
keywords = ["RongCloud HarmonyOS", "ArkTS IM SDK", "Failed Message Retry", "Local Message Storage", "Message Persistence"]
draft = false

toc = true

image = "cover.png"
image_alt = "Handling failed message delivery and local message recovery in RongCloud HarmonyOS IM SDK"
+++

When integrating RongCloud IM SDK into a HarmonyOS application, handling failed message delivery requires more than simply displaying an error notification.

A reliable messaging implementation should support:

- Identifying failed messages through SDK error codes and message IDs.
- Updating message delivery states in the local conversation UI.
- Retrieving failed messages from the local database.
- Retrying failed messages without creating duplicates.
- Recovering unsent messages after the application is terminated or restarted.

This article explains how to implement these mechanisms using HarmonyOS (ArkTS) and RongCloud IMLib.

## 1. Understanding Message Sending Results

When sending a message through RongCloud IM SDK, two important pieces of information should be considered:

| Field        | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| `code`       | Indicates whether the sending operation succeeded or failed.                  |
| `messageId`  | Local message identifier used to locate and update the corresponding message. |
| `messageUId` | Server-generated message identifier available after successful delivery.      |
| `sentStatus` | Indicates the current sending state of a locally stored message.              |
| `extra`      | Custom message metadata that can store additional business information.       |

The `messageId` is particularly important because it allows the application to update the correct message in the conversation list.

For example, when a message fails to send, the application should update its status to `SentStatus.Failed` rather than inserting another message into the list.

## 2. Handling Message Sending Failures

When sending a message, RongCloud provides a callback that can be used to obtain the locally inserted message.

This allows the application to display the message immediately with a `Sending` state, even before the server responds.

### Example: Sending a Text Message

```typescript
import {
  IMEngine,
  Message,
  TextMessage,
  ConversationIdentifier,
  ConversationType,
  ISendMsgOption,
  EngineError,
  SentStatus
} from '@rongcloud/imlib';

export class ChatMessageHelper {

  static async sendTextMessage(
    targetId: string,
    text: string,
    onMessageInserted: (msg: Message) => void,
    onMessageStatusChanged: (
      messageId: number,
      status: SentStatus,
      updatedMsg?: Message
    ) => void
  ): Promise<void> {

    const conId = new ConversationIdentifier();
    conId.conversationType = ConversationType.Private;
    conId.targetId = targetId;

    const textMsg = new TextMessage();
    textMsg.content = text;

    const msg = new Message(conId, textMsg);
    const option: ISendMsgOption = {};

    try {
      const result = await IMEngine.getInstance().sendMessage(
        msg,
        option,
        (insertedMsg: Message) => {
          // The message has been inserted into the local database.
          onMessageInserted(insertedMsg);
        }
      );

      if (result.code === EngineError.Success && result.data) {
        const successMsg = result.data as Message;

        onMessageStatusChanged(
          successMsg.messageId,
          SentStatus.Sent,
          successMsg
        );

        return;
      }

      // Sending failed.
      const failedMsg = (result.data as Message) ?? msg;

      onMessageStatusChanged(
        failedMsg.messageId,
        SentStatus.Failed,
        failedMsg
      );

      this.handleSendErrorCode(result.code);

    } catch (err) {
      onMessageStatusChanged(
        msg.messageId,
        SentStatus.Failed,
        msg
      );
    }
  }

  private static handleSendErrorCode(code: number): void {
    switch (code) {
      case EngineError.NetUnavailable:
      case EngineError.MsgRespTimeout:
        console.warn('Network error or message response timeout.');
        break;

      case EngineError.RejectedByBlacklist:
        console.warn('The recipient has blocked this message.');
        break;

      case EngineError.ForbiddenInGroup:
        console.warn('You are muted in this group.');
        break;

      default:
        console.error(`Message sending failed. Error code: ${code}`);
        break;
    }
  }
}
```

The important point is that the application should use the returned `messageId` to update the existing message instead of creating another message entry.

### Handling Different Error Types

Different errors require different strategies.

| Error scenario             | Recommended handling                                   |
| -------------------------- | ------------------------------------------------------ |
| Network unavailable        | Allow the user to retry.                               |
| Message response timeout   | Allow retry, but consider possible duplicate delivery. |
| Connection disconnected    | Wait for reconnection before retrying.                 |
| Recipient blacklist        | Display an appropriate error message.                  |
| Group muted                | Inform the user that sending is restricted.            |
| Sensitive content rejected | Display the corresponding restriction message.         |

Avoid automatically retrying every failed message. Business-level errors generally require user feedback rather than repeated sending attempts.

## 3. Retrieving Failed Messages from the Local Database

A common requirement is to restore failed messages when users reopen a conversation.

RongCloud provides local history retrieval through `getHistoryMessages`.

The returned messages contain a `sentStatus` field that can be used to identify messages that were not successfully sent.

Two states deserve special attention:

- `SentStatus.Failed`: The SDK has marked the message as failed.
- `SentStatus.Sending`: The application may have been terminated before the sending operation completed.

For messages that remain in the `Sending` state after an unexpected application termination, the application can restore them as failed messages and provide a retry option.

### Example: Loading Local Messages

```typescript
static async loadLocalMessages(
  targetId: string
): Promise<Message[]> {

  const conId = new ConversationIdentifier();
  conId.conversationType = ConversationType.Private;
  conId.targetId = targetId;

  const option = {
    timestamp: 0,
    count: 20,
    pullOrder: 0
  };

  const result = await IMEngine.getInstance()
    .getHistoryMessages(conId, option);

  if (result.code !== EngineError.Success || !result.data) {
    return [];
  }

  const messages = result.data as Message[];

  return messages.map((item: Message) => {

    if (
      item.sentStatus === SentStatus.Failed ||
      item.sentStatus === SentStatus.Sending
    ) {
      // Restore an interrupted sending operation as failed.
      item.sentStatus = SentStatus.Failed;
    }

    return item;
  });
}
```

After retrieving the messages, the UI can display a retry button next to messages whose status is `Failed`.

This makes it possible to restore the conversation state without relying exclusively on server-side message history.

## 4. Retrying Failed Messages Without Creating Duplicates

One of the most important details when implementing message retry is how the original message object is handled.

**For a message that has already been inserted into the local database, reuse the original `Message` instance when retrying.**

Do not create a new `Message` object using the original text content.

Why?

The original message already contains its local `messageId`. Reusing it allows the SDK to associate the retry operation with the existing local message record.

Creating a new message instead may result in duplicate entries in the conversation list.

### Example: Retrying a Failed Message

```typescript
static async resendFailedMessage(
  failedMsg: Message,
  onMessageStatusChanged: (
    messageId: number,
    status: SentStatus,
    updatedMsg?: Message
  ) => void
): Promise<void> {

  if (failedMsg.sentStatus !== SentStatus.Failed) {
    return;
  }

  // Update the UI before retrying.
  onMessageStatusChanged(
    failedMsg.messageId,
    SentStatus.Sending,
    failedMsg
  );

  const option: ISendMsgOption = {};

  const result = await IMEngine.getInstance().sendMessage(
    failedMsg,
    option,
    (updatedMsg: Message) => {
      onMessageStatusChanged(
        updatedMsg.messageId,
        SentStatus.Sending,
        updatedMsg
      );
    }
  );

  if (result.code === EngineError.Success && result.data) {

    const successMsg = result.data as Message;

    onMessageStatusChanged(
      successMsg.messageId,
      SentStatus.Sent,
      successMsg
    );

  } else {

    onMessageStatusChanged(
      failedMsg.messageId,
      SentStatus.Failed,
      failedMsg
    );

    this.handleSendErrorCode(result.code);
  }
}
```

The retry process follows this sequence:

1. Check whether the message is in the `Failed` state.
2. Update the UI to `Sending`.
3. Pass the original message object to `sendMessage`.
4. Update the existing message to `Sent` if successful.
5. Keep the message in the `Failed` state if the retry fails.

For media messages such as images, audio, and files, use `sendMediaMessage` instead of `sendMessage`, while following the same principle of reusing the original message object.

## 5. Preserving Failure Reasons Across Application Restarts

The local message database stores the message delivery state, but the original sending error code may not be available when retrieving the message later.

For example, after restarting the application, the UI may know that a message failed but may no longer know whether the reason was:

- Network unavailable.
- Message response timeout.
- Recipient blacklist.
- Group restrictions.
- Sensitive content rejection.

If the application needs to display the specific failure reason after restarting, it can save the error code in the message's `extra` field.

### Saving the Error Code

When sending fails:

```typescript
const failedMsg = result.data as Message;

const errorInfo = JSON.stringify({
  errorCode: result.code
});

await IMEngine.getInstance().setMessageExtra(
  failedMsg.messageId,
  errorInfo
);
```

### Restoring the Error Code

When retrieving local messages:

```typescript
const extra = item.extra;

if (extra) {
  try {
    const errorInfo = JSON.parse(extra);

    console.info(
      `Original sending error: ${errorInfo.errorCode}`
    );

  } catch (error) {
    console.warn('Unable to parse message extra data.');
  }
}
```

This approach allows the application to preserve additional business information associated with a failed message.

If the application already uses `extra` for other purposes, merge the error information into the existing JSON structure rather than overwriting unrelated metadata.

## 6. Why Do Failed Messages Disappear After Restarting the App?

A common problem during IM SDK integration is that failed messages appear correctly in the conversation before the application is terminated, but disappear after reopening it.

This usually indicates a problem with local persistence, database initialization, or message retrieval.

There are four important areas to investigate.

### 6.1 The Message Was Never Inserted into the Local Database

Not every failed sending operation necessarily produces a locally persisted message.

For example:

- The SDK connection or local database initialization has not completed.
- `sendMessage` is called before the required connection initialization.
- The message parameters are invalid.
- A custom message type is not registered correctly.
- The custom message type does not have the required persistence configuration.

The most important diagnostic step is checking whether the local insertion callback was triggered.

```typescript
const result = await IMEngine.getInstance().sendMessage(
  msg,
  option,
  (insertedMsg: Message) => {

    console.info(
      `Message inserted: ${insertedMsg.messageId}`
    );

  }
);
```

If this callback is never triggered, do not assume the failed message has been persisted.

### 6.2 The Application Loads Remote History Instead of Local History

Another common cause is using the wrong history retrieval API.

Consider the difference:

| API                        | Purpose                                           |
| -------------------------- | ------------------------------------------------- |
| `getHistoryMessages`       | Retrieves locally stored message history.         |
| `getRemoteHistoryMessages` | Retrieves message history from the remote server. |

A failed message that was never successfully delivered to the server cannot be retrieved from remote history.

Therefore, if the application uses `getRemoteHistoryMessages` and directly replaces the conversation UI with the returned data, locally stored failed messages may disappear.

For conversation initialization, retrieve local history first or implement an appropriate local and remote message merging strategy.

### 6.3 The Local Database Is Not Initialized Before Retrieving Messages

RongCloud maintains local message databases associated with individual user accounts.

When the application restarts, it must restore the correct SDK user context before querying local history.

A recommended initialization sequence is:

1. Initialize the SDK using `IMEngine.getInstance().init(...)`.
2. Connect using `connect(token)`.
3. Wait for the connection callback or confirm that the current user context is ready.
4. Retrieve local messages using `getHistoryMessages`.
5. Render the conversation UI.

For example:

```typescript
await IMEngine.getInstance().connect(token);

// Retrieve local history only after the SDK has
// initialized the appropriate user database.

const messages = await ChatMessageHelper.loadLocalMessages(
  targetId
);
```

The exact connection callback and result handling should follow the API signature of the IMLib version used in your project.

Calling the history API too early may result in an empty message list because the correct local database context has not yet been established.

### 6.4 Custom Message Types Do Not Support Local Persistence

If you use custom message types, check their message registration configuration.

The corresponding `MessageTag` must include the `ISPERSISTED` attribute when local persistence is required.

Without the persistence attribute, the message may exist only in the current application runtime and disappear after the process is terminated.

## 7. A Practical Troubleshooting Checklist

When a failed message disappears after restarting the application, check the following items in order:

| Check                      | What to verify                                           |
| -------------------------- | -------------------------------------------------------- |
| Local insertion callback   | Was the `onInserted` callback triggered?                 |
| Message ID                 | Is the returned `messageId` valid?                       |
| Message status             | Is the message marked as `Failed` or `Sending`?          |
| SDK initialization         | Was `init()` completed?                                  |
| Connection initialization  | Was `connect(token)` executed before retrieving history? |
| Local history              | Are you using `getHistoryMessages`?                      |
| User context               | Is the SDK using the correct logged-in user?             |
| Custom message persistence | Does the message type include `ISPERSISTED`?             |

These checks help determine whether the problem is related to message insertion, database initialization, or history retrieval.

## 8. Recommended Message Lifecycle

A reliable message lifecycle should look like this:

```text
User sends a message
        |
        v
Create Message object
        |
        v
Insert message into local database
        |
        v
Display message as Sending
        |
        v
Send message to RongCloud
        |
        +----------------------+
        |                      |
        v                      v
    Success                  Failure
        |                      |
        v                      v
   Mark as Sent          Mark as Failed
                               |
                               v
                       Save error code
                         if required
                               |
                               v
                       Application restarts
                               |
                               v
                       Initialize SDK
                               |
                               v
                       Connect with token
                               |
                               v
                       Load local history
                               |
                               v
                       Restore failed messages
                               |
                               v
                       User clicks Retry
                               |
                               v
                       Reuse original Message
                               |
                               v
                       Send again
```

The key is to treat local message persistence and server delivery as two separate operations.

A message can be successfully inserted into the local database even if its delivery to the server eventually fails.

This distinction is essential for building a reliable messaging experience.

## Conclusion

When handling failed messages in RongCloud HarmonyOS applications, the most important considerations are:

1. Use `messageId` to update the correct message in the conversation UI.
2. Use `sentStatus` to identify failed or interrupted messages.
3. Use `getHistoryMessages` to retrieve locally persisted conversation history.
4. Reuse the original `Message` instance when retrying a locally stored message.
5. Save the original error code in `extra` if the application needs to restore detailed failure information.
6. Initialize the SDK and restore the correct user context before querying local history.
7. Ensure custom message types have the required persistence configuration.

By separating local message storage from remote message delivery, applications can reliably restore failed messages and provide users with a consistent retry experience, even after unexpected application termination.

**Note:** The code examples use the HarmonyOS ArkTS API structure discussed in this article. Import paths, callback signatures, enum names, and method availability should be verified against the specific RongCloud IMLib version integrated into your project.
