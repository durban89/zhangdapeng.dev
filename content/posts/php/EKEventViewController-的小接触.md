---
title: "EKEventViewController 的小接触"
date: "2025-06-19 13:53:59"
slug: "ekeventviewcontroller-de-xiao-jie-chu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/EKEventViewController-的小接触/"
  - "/2025/06/19/EKEventViewController-的小接触.html"
  - "/EKEventViewController-的小接触/"
  - "/EKEventViewController-的小接触.html"
  - "/2025/06/19/ekeventviewcontroller-de-xiao-jie-chu/"
  - "/2025/06/19/ekeventviewcontroller-de-xiao-jie-chu.html"
  - "/ekeventviewcontroller-de-xiao-jie-chu.html"
---
apple官方对EKEventViewController是这么描述的

> An EKEventViewController object displays the details of a calendar event. You can set whether users are allowed to edit the event. If the event is an invitation, where the organizer is not the user, you can set whether a calendar preview is shown.

EKEventViewController其实就是一个展示日历事件详情的视图控制器

官方的一段代码的实现是这样的：

```objectivec
#pragma mark -
#pragma mark EKEventEditViewDelegate

// Overriding EKEventEditViewDelegate method to update event store according to user actions.
- (void)eventEditViewController:(EKEventEditViewController *)controller 
          didCompleteWithAction:(EKEventEditViewAction)action
{
    RootViewController * __weak weakSelf = self;
    // Dismiss the modal view controller
    [self dismissViewControllerAnimated:YES completion:^
     {
         if (action != EKEventEditViewActionCanceled)
         {
             dispatch_async(dispatch_get_main_queue(), ^{
                 // Re-fetch all events happening in the next 24 hours
                 weakSelf.eventsList = [self fetchEvents];
                 // Update the UI with the above events
                 [weakSelf.tableView reloadData];
             });
         }
     }];
}


// Set the calendar edited by EKEventEditViewController to our chosen calendar - the default calendar.
- (EKCalendar *)eventEditViewControllerDefaultCalendarForNewEvents:(EKEventEditViewController *)controller
{
    return self.defaultCalendar;
}
```

并且他的实现过程是：

```objectivec
#pragma mark -
#pragma mark Add a new event

// Display an event edit view controller when the user taps the "+" button.
// A new event is added to Calendar when the user taps the "Done" button in the above view controller.
- (IBAction)addEvent:(id)sender
{
    // Create an instance of EKEventEditViewController 
    EKEventEditViewController *addController = [[EKEventEditViewController alloc] init];
    
    // Set addController's event store to the current event store
    addController.eventStore = self.eventStore;
    addController.editViewDelegate = self;
    [self presentViewController:addController animated:YES completion:nil];
}
```

其实跟自己写一个viewcontroller的过程，然后自己再去调用是差不多的，少的是自己不用去写这个逻辑流程，还有就是，如果自己写的话是不是会有什么限制。我觉得应该不会有，不然也不会开放出来让大家使用。
