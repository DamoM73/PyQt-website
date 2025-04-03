# Tutorial 15 - Advanced To Do

```{admonition} In this tutorial, you will:
- Implement functionality to start a fresh to-do list by clearing existing tasks and setting a new title.
- Utilise JSON files to store the to-do list's name and tasks, allowing for data persistence.
- Load previously saved to-do lists from JSON files to continue managing tasks.
- Learn about QActions to manage menu signals like New, Open, and Save for efficient menu handling.
- Implement QFileDialog to enable users to select file locations for saving and opening to-do lists.
```

In this tutorial we will allow the user to save and load their to do lists. We will use the menu to:

- Create a new list
- Open a saved list
- Save the current list

## Advanced To Do Planning

Qt menus signals are called actions. If you look at the `.ui` file in QT Designer you will notice that the menu names are **actionNew**, **actionOpen** and **actionSave**. They are all **QActions**, which have different triggers. 

```{admonition} QActions
:class: hint
A `QAction` lets you reuse the same action (like opening a file) in multiple places—like menus, toolbars, or shortcuts—without writing the code again. To explore QActions more, check out the **[Qt Documentations](https://doc.qt.io/qt-6/qaction.html)**
```

We also need to think about how we will save our data to a file. We will use a JSON file to save the data. You don't need to know many details about the JSON format, except that their structure is equivalent to a Python dictionary.

```{admonition} JSON files
:class: hint
JSON (JavaScript Object Notation) files are a simple way to store and share data in a format that's easy for both people and computers to understand. They look like a list of things (called arrays) or a bunch of labels with values (called objects), kind of like a digital version of organizing your stuff in labeled boxes. For example, you might have a "name" label with the value "Alex" or a list of your favorite games. 

JSON is used a lot in apps and websites to send information back and forth, like saving your profile or showing search results.
```

## Advance To Do Coding

Just like the Basic To Do code, we will work on this code in signal/slot pairs.

### Save To Do List

We will start with saving signal/slot pair, because we can't open a list until one is saved. We need to use the **json** library and the **QFileDialog** from the **QWidgets** library, so we better import these.

![import](./assets/img/17/00_import.png)

1. At the bottom of the slot section add the following code.

![save list](./assets/img/17/01_save_list.png)

This step collects the elements to make a dictionary.

- The first element is the list name taken from `lineEdit_name`.
- The second element is a list of all the tasks. We need to iterate over the **listWidget** and append each element to the task list.
  - Note: we have to use **index** to iterate over the **listWidget** since it does not act like a Python list.

2. Now the second part of **save_list** which uses the **QFileDialog** for the user to choose the file name and save location, and then **json.dump** to save the dictionary as a json file.

![save list 2](./assets/img/17/03_save_list_2.png)

3. Finally we need to connect the signal to the slot we just created

![save file signal](./assets/img/17/04_save_file_signal.png)

Run the app, create a to do list and save it.

1. Does the file appear where you saved it?
2. Open the file in VS Code, does it contain the details from your to do list?

### Open To Do List

Now that we have a saved to do list file, we can create the open file signal/slot pair.

1. At the bottom of the slots section, use the **QFileDialog** to allow users to select their saved to do list file.

![open file dialog](./assets/img/17/05_open_file_dialog.png)

2. If the user selects a file, load the json file into the To Do List UI.

![load file](./assets/img/17/06_load_file.png)

3. Connect the slot to the actionOpen signal

![open action signal](./assets/img/17/07_openaction_signal.png)

Now test your code, by opening the file you previously saved.

### New To Do List

The final feature we need to add is for the New List signal/slot pair. This is quite simple: clear everything and return the focus to **lineEdit_list_name**

1. At the bottom of the slots section add:

![new list slot](./assets/img/17/08_new_list_slot.png)

2. Then connect the signal

![new list signal](./assets/img/17/09_new_list_signal.png)

Now load a saved list and then create a new list and ensure that everything works.