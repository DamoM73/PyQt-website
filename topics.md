## 01_introduction.md
Code wrappers
:class: tip
Code wrappers are like translators that let code written in one programming language talk to code written in another. They work by creating **bindings**, which are special connections that make functions or objects from one language available in another. For example, if you have a Python program and want it to use a library written in C, a wrapper acts as a bridge, using bindings to translate between Python and C so they can work together seamlessly. This allows developers to use the strengths of multiple languages in the same project.


## 02_setup.md
In this lesson you will:
- Set up your computer for the course
- Install Python
- Set up a version control workflow
- Install an Integrated Development Environment
- Install Qt Designer
- Download the PyQt boilerplate code
- Create a virtual environment

## 03_tutorial_1.md
In this tutorial you will:
- Create a UI for a simple app in Qt Designer
- Add some formatted text to the UI
- Convert the UI to the view Python file
- Launch and test the app.

## 04_tutorial_2.md
In this tutorial you will learn to:
- change label geometry
- change label alignment
- change label margins
- copy widgets in a window
- use labels to add images
- change label font colour
- change label background colour
- change label borders

## 05_tutorial_3.md
In this tutorial you will:
- Learn about Qt's three Layouts
- Learn about static and dynamic UIs
- Apply Layout to organise a window


## 06_tutorial_4.md
In this tutorial you will:
- Nest layouts to create a more complex UI
- Use spaces to control layout expansion


## 07_tutorial_5.md
In this tutorial you will:
- add pushButtons to your UI
- use QT's signals and slots process architecture to create an interactive UI

## 08_tutorial_6.md
In this tutorial you will:
- apply learnt techniques to develop a calculator app
- use QT Styles to change the appearance of your app
- develop the application logic inside the control file

## 09_tutorial_7.md
In this tutorial you will:
- Enhance the calculator application to perform basic arithmetic operations using Python's eval() function.
- Assign appropriate signals and slots to the equals button to handle user input effectively.
- Utilize a flag variable to track when the equals button has been pressed, ensuring correct behaviour for subsequent number and operator inputs.
- Modify slot methods for number and decimal buttons to incorporate the flag variable, resetting the equation as needed to maintain accurate calculations.
- Run the refined calculator application to identify and resolve issues, ensuring it handles simple calculations correctly and mimics standard calculator behaviour.

## 10_tutorial_8.md
In this tutorial you will:
- Understand Tabbed Layouts in PyQt
- Design User Interfaces with Tabs
- Implement a QTabWidget in Qt Designer

## 11_tutorial_9.md
In this tutorial you will:
- Learn how to load a `.ui` file using the `loadUi` method
- Create a new boilerplate file which uses `loadUi`

## 12_tutorial_10.md
In this tutorial you will:
- Learn how to use **QTimers** to manage time-based events and update the displayed time every second.  
- Create and configure a timer to emit signals at regular intervals using the **timeout** signal.  
- Display and format the current time using Qt’s **toString** method.  
- Test and experiment with timer intervals and time display customisation.

## 13_tutorial_11.md
In this tutorial you will:
- Plan and implement a user interface with Start, Stop, Pause, and Reset buttons, each managing the stopwatch's state.
- Utilise flag variables to track whether the stopwatch is running or paused, ensuring accurate control over its operation.
- Set up a timer that triggers every 100 milliseconds to update the stopwatch's time display, reflecting elapsed time accurately.
- Establish connections between user interactions (button presses) and corresponding functions to control the stopwatch's behaviour effectively.

## 14_tutorial_12.md
In this tutorial you will:
- Implement a user interface featuring spinboxes to set the starting time and buttons to control the timer's operation.
- Develop the logic to convert spinbox values into a countdown timer, manage time subtraction, and handle timer updates.
- Utilise variables to track the timer's status, ensuring accurate control over start, stop, pause, and reset actions.
- Establish connections between user interactions (e.g., button presses) and corresponding functions to control the timer's behaviour effectively.
- Incorporate sound notifications that trigger when the timer reaches zero, enhancing the timer's functionality.

## 15_tutorial_13.md
In this tutorial, you will:
- Design a user interface for a to-do list using PyQt and Qt Designer.
- Configure the main window's size and title to suit the application's requirements.
- Add 'File' menu options such as New, Open, and Save to manage to-do lists.
- Incorporate widgets like Line Edit, List Widget, Push Button, and Horizontal Spacer, and adjust their properties for optimal functionality.
- Use vertical and horizontal layouts to structure the application's interface effectively.

## 16_tutorial_14.md
In this tutorial, you will:
- Utilise a QLineEdit widget to set and display the to-do list's title.
- Implement a QPushButton that, when clicked, opens an input dialog box for entering new tasks.
- Use a QListWidget to show all added tasks, ensuring they are visible and organised.
- Enable item removal from the list by connecting the QListWidget's itemClicked signal to a function that deletes the selected task.

## 17_tutorial_15.md
In this tutorial, you will:
- Implement functionality to start a fresh to-do list by clearing existing tasks and setting a new title.
- Utilise JSON files to store the to-do list's name and tasks, allowing for data persistence.
- Load previously saved to-do lists from JSON files to continue managing tasks.
- Learn about QActions to manage menu signals like New, Open, and Save for efficient menu handling.
- Implement QFileDialog to enable users to select file locations for saving and opening to-do lists.

## 18_tutorial_16.md
In this tutorial, you will:
- Design a main application window using Qt Designer.  
- Create a second window layout using Qt Designer.  
- Set up buttons in the main window to trigger actions.

## 19_tutorial_17.md
In this tutorial, you will:
- Load multiple window designs into a PyQt application using `.ui` files.  
- Implement functionality to open a secondary window from the main window.  
- Pass information between windows within a PyQt application.  
- Test and validate navigation between multiple windows.
