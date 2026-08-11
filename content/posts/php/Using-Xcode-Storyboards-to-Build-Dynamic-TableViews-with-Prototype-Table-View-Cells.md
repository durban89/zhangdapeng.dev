---
title: "Using Xcode Storyboards to Build Dynamic TableViews with Prototype Table View Cells"
date: "2025-06-25 10:26:19"
slug: "using-xcode-storyboards-to-build-dynamic-tableviews-with-prototype-table-view-cells"
categories: ["技术"]
tags: ["Xcode"]
aliases:
  - "/2025/06/25/Using-Xcode-Storyboards-to-Build-Dynamic-TableViews-with-Prototype-Table-View-Cells/"
  - "/2025/06/25/Using-Xcode-Storyboards-to-Build-Dynamic-TableViews-with-Prototype-Table-View-Cells.html"
  - "/Using-Xcode-Storyboards-to-Build-Dynamic-TableViews-with-Prototype-Table-View-Cells/"
  - "/Using-Xcode-Storyboards-to-Build-Dynamic-TableViews-with-Prototype-Table-View-Cells.html"
  - "/2025/06/25/using-xcode-storyboards-to-build-dynamic-tableviews-with-prototype-table-view-cells/"
  - "/2025/06/25/using-xcode-storyboards-to-build-dynamic-tableviews-with-prototype-table-view-cells.html"
  - "/using-xcode-storyboards-to-build-dynamic-tableviews-with-prototype-table-view-cells.html"
---
最近在做IOS开发，坚决支持自己要使用storyboard，关于动态的实现cell还一直不太会，终于找到了一篇外国牛人的帖子。直接粘贴了。想看的下面有链接的。噢耶。

Creating the Example Project

Start Xcode and create a single view application. Name the project and class prefix TableViewStory.

A review of the files in the project navigator panel will reveal that, as requested, Xcode has created a view controller subclass for us named TableViewStoryViewController. In addition, this view controller is represented within the Storyboard file, the content of which may be viewed by selecting the MainStoryboard.storyboard file.

In order to fully understand the steps involved in creating a Storyboard based TableView application we will start with a clean slate by removing the view controller added for us by Xcode. Within the storyboard canvas, select the Table View Story View Controller item so that it is highlighted in blue and press the Delete key on the keyboard. Next, select and delete both the corresponding TableViewStoryViewController.m and TableViewStoryViewController.h files from the project navigator panel. In the resulting panel select the option to delete the files.

At this point we have a template project consisting solely of a storyboard file and the standard app delegate code files and are ready to begin building a storyboard based iPhone application using the UITableView and UITableViewCell classes.

Adding the TableView Controller to the Storyboard

From the perspective of the user, the entry point into this application will be a table view containing a list of cars, with each table view cell containing the vehicle make, model and corresponding image. As such, we will need to add a Table View Controller instance to the storyboard file. Select the MainStoryboard.storyboard file so that the canvas appears in the center of the Xcode window. From within the Object Library panel (accessible via the View -> Utilities -> Show Object Library menu option) drag a Table View Controller object and drop it onto the storyboard canvas as illustrated in Figure 18 1:

Within the storyboard we now have a table view controller instance. Within this instance is also a prototype table view cell that we will be able to configure to design the cells for our table. At the moment these are generic UITableViewCell and UITableViewController classes that do not give us much in the way of control within our application code. So that we can extend the functionality of these instances we need to declare them as being subclasses of UITableViewController and UITableViewCell respectively. Before doing so, however, we need to actually create those subclasses.

Creating the UITableViewController and UITableViewCell Subclasses

We will be declaring the Table View Controller instance within our storyboard as being a subclass of UITableViewController named CarTableViewController. At present, this subclass does not exist within our project so clearly we need to create it before proceeding. To achieve this, select the File -> New -> New File… menu option and in the resulting panel select the option to create a new UIViewController subclass. Click Next and on the subsequent screen, name the class CarTableViewController and change the Subclass of menu to UITableViewController. Make sure that the Targeted for iPad and With XIB for user interface options are both turned off and click Next followed by Create.

Within the Table View Controller added to the storyboard in the previous section, Xcode also added a prototype table cell. Later in this chapter we will add two labels and an image view object to this cell. In order to extend this class it is necessary to, once again, create a subclass. Perform this step by selecting the File -> New -> New File…. menu option. Within the new file dialog select Objective-C class and click Next. On the following screen, name the new class CarTableViewCell, change the Subclass of menu to UITableViewCell and proceed with the class creation.

Next, the items in the storyboard need to be configured to be instances of these subclasses. Begin by selecting the MainStoryboard.storyboard file and select the Navigation Controller scene so that it is highlighted in blue. Within the identity inspector panel (View -> Utilities -> Show Identity Inspector) use the Class drop down menu to change the class from UITableViewController to CarTableViewController as illustrated in Figure 18-2:

Similarly, select the prototype table cell within the table view controller storyboard scene and change the class from UITableViewCell to the new CarTableViewCell subclass. With the appropriate subclasses created and associated with the objects in the storyboard, the next step is to design the prototype cell.

Declaring the Cell Reuse Identifier

Later in the chapter some code will be added to the project to replicate instances of the prototype table cell. This will require that the cell be assigned a reuse identifier. With the storyboard still visible in Xcode, select the prototype table cell and display the Attributes Inspector. Within the inspector, change the Identifier field to carTableCell:

Designing a Storyboard UITableView Prototype Cell

Table Views are made up of multiple cells, each of which is actually either an instance of the UITableViewCell class or a subclass thereof. A useful feature of storyboarding allows the developer to visually construct the user interface elements that are to appear in the table cells and then replicate that cell at runtime. For the purposes of this example each table cell needs to display an image view and two labels which, in turn, will be connected to outlets that we will later declare in the CarTableViewCell subclass. Much like Interface Builder, components may be dragged from the Object Library panel and dropped onto a scene within the storyboard. Note, however, that this is only possible when the storyboard view is zoomed in. With this in mind, verify that the storyboard is zoomed in using the controls in the bottom right hand corner of the canvas and then drag and drop two Labels and an Image View object onto the prototype table cell. Resize and position the items so that the cell layout resembles that illustrated in Figure 18-4, making sure to stretch the label objects so that they extend toward the right hand edge of the cell.

Having configured the storyboard elements for the table view portion of the application it is time to begin modifying the table view and cell subclasses.

Modifying the CarTableViewCell Class

Within the storyboard file two labels and an image view were added to the prototype cell which, in turn, has been declared as an instance of our new CarTableViewCell class. In order to manipulate these user interface objects from within our code we need to declare three outlets and then connect those outlets to the objects in the storyboard scene. Begin, therefore, by selecting the CarTableViewCell.h file and adding the three outlet properties as follows:

```objectivec
#import <UIKit/UIKit.h>

@interface CarTableViewCell : UITableViewCell
@property (nonatomic, strong) IBOutlet UIImageView *carImage;
@property (nonatomic, strong) IBOutlet UILabel *makeLabel;
@property (nonatomic, strong) IBOutlet UILabel *modelLabel;
@end
```

Having declared the properties, synthesize access within the CarTableViewCell.m implementation file:

```objectivec
#import "CarTableViewCell.h"

@implementation CarTableViewCell
@synthesize makeLabel = _makeLabel;
@synthesize modelLabel = _modelLabel;
@synthesize carImage = _carImage;

@end
```

With the outlet properties declared the next step is to establish the connections to the user interface objects. Within the storyboard file Ctrl-click on the white background of the prototype table cell and drag the resulting blue line to the uppermost of the two labels as outlined in Figure 18-5:

Upon releasing the pointer, select makeLabel from the resulting menu to establish the outlet connection:

Repeat these steps to connect the modelLabel and carImage outlets to the second label and image view objects respectively.

Creating the Table View Datasource

Dynamic Table Views require a datasource to provide the data that will be displayed to the user within the cells. By default, Xcode has designated the CarTableViewController class as the datasource for the table view controller in the storyboard. It is within this class, therefore, that we can build a very simple data model for our application consisting of a number of arrays. The first step is to declare these as properties in the CarTableViewController.h file:

```objectivec
#import <UIKit/UIKit.h>
@interface CarTableViewController : UITableViewController
@property (nonatomic, strong) NSArray *carImages;
@property (nonatomic, strong) NSArray *carMakes;
@property (nonatomic, strong) NSArray *carModels;
@end
```

With the properties declared these need to be synthesized within the CarTableViewController.m file. In addition, the arrays need to be initialized with some data when the application has loaded, making the viewDidLoad: method an ideal location. Select the CarTableViewController.m file within the project navigator panel and modify it as outlined in the following code fragment. Since we will be working with CarTableViewCell instances within the code it is also necessary to import theCarTableViewCell.h file:

```objectivec
#import "CarTableViewController.h"
#import “CarTableViewCell.h”
@implementation CarTableViewController
@synthesize carMakes = _carMakes; 
@synthesize carModels = _carModels;
@synthesize carImages = _carImages;
- (void)viewDidLoad
{
    [super viewDidLoad];
    self.carMakes = [[NSArray alloc]
                     initWithObjects:@"Chevy",
                     @"BMW",
                     @"Toyota",
                     @"Volvo",
                     @"Smart", nil];
    self.carModels = [[NSArray alloc]
                      initWithObjects:@"Volt",
                      @"Mini",
                      @"Venza",
                      @"S60",
                      @"Fortwo", nil];
    self.carImages = [[NSArray alloc]
          initWithObjects:@"chevy_volt.jpg",
                      @"mini_clubman.jpg",
                      @"toyota_venza.jpg",
                      @"volvo_s60.jpg",
                      @"smart_fortwo.jpg", nil];
}
```

For a class to act as the datasource for a table view controller a number of methods must be implemented. These methods will be called by the table view object in order to obtain both information about the table and also the table cell objects to display. When we created the CarTableViewController class we specified that it was to be a subclass of UITableViewController. As a result, Xcode created templates of these data source methods for us within the CarTableViewController.m file. To locate these template datasource methods, scroll down the file until the #pragma mark – Table view data source marker comes into view. The first template method, named numberOfSectionsInTableView: needs to return the number of sections in the table. For the purposes of this example we only need one section so will simply return a value of 1 (note also that the #warning line needs to be removed):

```objectivec
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
   // Return the number of sections.
   return 1;
}
```

The next method is required to return the number of rows to be displayed in the table. This is equivalent to the number of items in our carModels array so can be modified as follows:

```objectivec
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
   // Return the number of rows in the section.
   return [self.carModels count];
}
```

The above code calls the count method on the carModels array object to obtain the number of items in the array and returns that value to the table view.

The final datasource method that needs to be modified is cellForRowAtIndexPath:. Each time the table view controller needs a new cell to display it will call this method and pass through an index value indicating the row for which a cell object is required. It is the responsibility of this method to create a new instance of our CarTableViewCell class (unless an instance already exists for re-use) and extract the correct car make, model and image file name from the data arrays based on the index value passed through to the method. The code will then set those values on the appropriate outlets on the CarTableViewCell object. Begin by removing the template code from this method and then re-write the method so that as reads as follows:

```objectivec
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"carTableCell";
    CarTableViewCell *cell = [tableView
          dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[CarTableViewCell alloc]
          initWithStyle:UITableViewCellStyleDefault 
          reuseIdentifier:CellIdentifier];
    }
    // Configure the cell...
    cell.makeLabel.text = [self.carMakes 
          objectAtIndex: [indexPath row]];
    cell.modelLabel.text = [self.carModels 
           objectAtIndex:[indexPath row]];
    UIImage *carPhoto = [UIImage imageNamed: 
           [self.carImages objectAtIndex: [indexPath row]]];
    cell.carImage.image = carPhoto;
    return cell;
}
```

Before proceeding with this tutorial we need to take some time to deconstruct this code and explain what is actually happening. The code begins by creating a string that represents the reuse identifier that was assigned to the CarTableViewCell class within the storyboard (in this instance the identifier was set to carTableCell):

```objectivec
static NSString *CellIdentifier = @"carTableCell";
```

Next, the following lines of code are executed:

```objectivec
CarTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
if (cell == nil) {
    cell = [[CarTableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
}
```

This code calls the dequeueReusableCellWithIdentifier: method of the table view object to find out if an existing cell is available for re-use as the new row. If no cell is available then a new instance of the CarTableViewCell class is created ready for use. Having either created a new cell, or obtained an existing reusable cell the code simply uses the outlets previously added to the CarTableViewCell class to set the labels with the car make and model. The code then creates a new UIImage object configured with the image of the current car and assigns it to the image view outlet. Finally, the method returns the cell object to the table view:

```objectivec
// Configure the cell...
cell.makeLabel.text = [self.carMakes objectAtIndex: [indexPath row]];
cell.modelLabel.text = [self.carModels objectAtIndex:[indexPath row]];
UIImage *carPhoto = [UIImage imageNamed:[self.carImages objectAtIndex: [indexPath row]]];
cell.carImage.image = carPhoto;
return cell;
```

Downloading and Adding the Image Files

Before a test run of the application can be performed the image files referenced in the code need to be added to the project. An archive containing the images may be downloaded from the following URL:

<http://www.ebookfrenzy.com/code/carImages.zip>

Once the file has been downloaded, unzip the files and then drag and drop them from a Finder window onto the Supporting Files category of the Xcode project navigator panel.

Compiling and Running the Application

Now that the storyboard work and code modifications are complete the final step in this chapter is to run the application by clicking on the Run button located in the Xcode toolbar. Once the code has compiled the application will launch and execute within an iOS Simulator session as illustrated in Figure 18-7.

Clearly the table view has been populated with multiple instances of our prototype table view cell, each of which has been customized through outlets to display different car information and photos. The next step, which will be outlined in the next chapter entitled Implementing TableView Navigation using Xcode Storyboards will be to use the storyboard to add navigation capabilities to the application so that selecting a row from the table results in a detail scene appearing to the user.

Summary

The Storyboard feature of Xcode significantly eases the process of creating complex table view based interfaces within iPhone applications. Arguably the most significant feature is the ability to visually design the appearance of a table view cell and then have that cell automatically replicated at run time to display information to the user in table form.

---

木有图片，我木有copy图片过来的，你们自己去源文章看吧，我这里就简单的描述一下，其实是跟自己自定义一个cell是一个样子的（使用xib文件），只是这里的话直接在storyboard里面了 

