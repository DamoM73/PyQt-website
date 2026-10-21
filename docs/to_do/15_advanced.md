# Tutorial 15 - Advanced To Do

!!! learn "In this tutorial we will learn"
    - how menu items send signals through `QAction` objects
    - how to store data in a JSON file so it's kept after the app closes
    - how to let the user choose where to save and open files with `QFileDialog`
    - how to clear the UI to start a new list

!!! terms "Terminology"
    - **action** – a Qt object, called a `QAction`, that represents a command such as **Save**, and sends a `triggered` signal when the user chooses it.
    - **JSON** – short for JavaScript Object Notation, a text format for storing data as labels and values, laid out like a Python dictionary.
    - **data persistence** – keeping data after a program closes, usually by saving it to a file or database.
    - **dictionary** – a collection that stores values with names, called keys, so we can look each value up by its name.

At the moment our To Do List forgets everything when we close the app. In this tutorial we'll use the **File** menu to:

- create a new list
- save the current list
- open a saved list

## Plan the advanced features

### Menu signals

In Qt, each menu item is an **action**. If we open ***to_do_list.ui*** in Qt Designer and look in the Object Inspector, the menu items are called `actionNew`, `actionOpen` and `actionSave`. Each one is a `QAction`, and it sends a `triggered` signal when the user chooses it.

!!! tip "QActions"
    A `QAction` lets us use the same command (like **Save**) in several places, such as a menu, a toolbar button and a keyboard shortcut, without writing the code more than once. The [QAction documentation](https://doc.qt.io/qt-6/qaction.html) has the details.

### Saving the data

We'll store each list in a **JSON** file. We don't need to know much about JSON, except that its structure matches a Python **dictionary**, so Python's `json` library can save a dictionary to a file and load it back.

!!! tip "JSON files"
    JSON (JavaScript Object Notation) files store data as text that's easy for both people and computers to read. Data is stored as labels with values (called objects), and lists of values (called arrays). JSON is used everywhere to save settings and to send data between apps and websites. The [JSON](https://damom73.github.io/digital-solutions-text-2025/json) page of the Digital Solutions text explains it in more detail.

Our saved list will look like this:

```text
{
    "list_name": "Camp Packing",
    "tasks": [
        "Toothbrush",
        "Pillow",
        "Sleeping Bag"
    ]
}
```

We'll keep working in slot/signal pairs. We start with **Save**, because we can't open a list until one has been saved.

## Save a list

We need the `json` library and `QFileDialog`, so let's import them.

```python linenums="1" hl_lines="2 4" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step01/to_do_list.py:1:5"
```

??? note "Code explanation"
    - **line 2** → imports Python's `json` library, which saves and loads JSON files.
    - **line 4** → adds `QFileDialog`, Qt's ready-made dialog for choosing files.

The first part of the `save_list` slot collects the data into a dictionary. Add it at the bottom of the slots section.

```python linenums="43" hl_lines="6-11 13-17 19-23" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step02/to_do_list.py:43:66"
```

??? note "Code explanation"
    - **line 48** → defines the `save_list` slot.
    - **lines 49–51** → a docstring that explains what the slot does.
    - **line 53** → gets the list's name from the line edit.
    - **line 56** → creates an empty Python list for the tasks.
    - **line 57** → loops through every row number in the list widget, from `0` up to its number of items. A list widget isn't a Python list, so we can't loop over it directly; we use its `count` and `item` methods instead.
    - **line 58** → gets the text of the item in that row…
    - **line 59** → …and adds it to `tasks`.
    - **lines 62–65** → put the list name and the tasks in a dictionary, ready to save as JSON.

The second part asks the user where to save the file, then saves the dictionary there.

```python linenums="48" hl_lines="20-28 30-33" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step03/to_do_list.py:48:81"
```

??? note "Code explanation"
    - **line 68** → if the list has a name…
    - **line 69** → …suggests a file name made from it, such as ***Camp Packing.json***…
    - **line 70** → …otherwise…
    - **line 71** → …suggests ***to_do_list.json***.
    - **lines 72–75** → open a save dialog with a title, the suggested file name and a filter so only JSON files are shown. It returns the chosen path and the filter used; we only need the path, so the filter goes into `_`, which is how Python programmers show a value they're ignoring.
    - **line 78** → only saves if the user chose a file (if they clicked **Cancel**, `file_path` is an empty string)…
    - **line 79** → …opening the file for writing (`"w"`). The `with` block closes the file automatically when it finishes.
    - **line 80** → writes the dictionary to the file as JSON, indented by 4 spaces so it's easy to read.

Finally, connect the **Save** action's `triggered` signal.

```python linenums="20" hl_lines="7" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step04/to_do_list.py:20:26"
```

??? note "Code explanation"
    - **line 26** → connects the **Save** menu item's `triggered` signal to `save_list`.

!!! primm "PRIMM"
    1. **Predict** what will appear in the file after you name a list, add three tasks and choose **File** → **Save**.
    2. **Run** ***to_do_list.py***, create a list and save it.
    3. **Investigate**: does the file appear where you saved it? Open it in VS Code. Does it contain your list's name and tasks?

## Open a list

Now that we have a saved list, we can write the **Open** slot/signal pair. First, the slot asks the user which file to open.

```python linenums="80" hl_lines="4-12" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step05/to_do_list.py:80:92"
```

??? note "Code explanation"
    - **line 83** → defines the `open_list` slot.
    - **lines 84–86** → a docstring that explains what the slot does.
    - **lines 88–91** → open a file dialog that only shows JSON files, and store the chosen path. The empty string means the dialog starts in the current folder.

Then it loads the file into the UI.

```python linenums="83" hl_lines="11-18" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step06/to_do_list.py:83:101"
```

??? note "Code explanation"
    - **line 94** → only loads a file if one was chosen…
    - **line 95** → …opening it for reading (`"r"`)…
    - **line 96** → …and turning the JSON back into a Python dictionary.
    - **line 97** → puts the saved list name into the line edit.
    - **line 98** → clears any tasks already in the list widget, so the opened list doesn't mix with the old one.
    - **lines 99–100** → add each saved task to the list widget.

Then connect the **Open** action.

```python linenums="20" hl_lines="8" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step07/to_do_list.py:20:27"
```

??? note "Code explanation"
    - **line 27** → connects the **Open** menu item's `triggered` signal to `open_list`.

!!! primm "PRIMM"
    1. **Predict** what will happen when you open the file you just saved.
    2. **Run** ***to_do_list.py*** and open your saved list.
    3. **Investigate**: what happens if you open a JSON file that wasn't made by our app? Keep the answer in mind for Exercise 1.

## New list

The last feature is **New**. It's simple: clear everything and put the cursor back in the list name box.

```python linenums="94" hl_lines="10-16" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step08/to_do_list.py:94:110"
```

??? note "Code explanation"
    - **line 103** → defines the `new_list` slot.
    - **lines 104–106** → a docstring that explains what the slot does.
    - **line 107** → clears the list name.
    - **line 108** → clears all the tasks.
    - **line 109** → moves the keyboard focus to the list name box, so the user can start typing straight away.

Connect the **New** action.

```python linenums="20" hl_lines="9" title="to_do_list.py"
--8<-- "examples/to_do/15_advanced/step09/to_do_list.py:20:28"
```

??? note "Code explanation"
    - **line 28** → connects the **New** menu item's `triggered` signal to `new_list`.

!!! primm "PRIMM"
    1. **Predict** what the window will look like after **File** → **New**.
    2. **Run** ***to_do_list.py***, open a saved list, then choose **File** → **New**.
    3. **Investigate**: what happens to the unsaved changes if you choose **New** by mistake?

## Test the To Do List

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | name a list, add tasks, **Save** | JSON file has the name and every task | | | |
| 2 | **Save**, then **Cancel** | nothing is saved, no error | | | |
| 3 | **Open** a saved list | name and tasks appear, old tasks are gone | | | |
| 4 | **Open**, then **Cancel** | list doesn't change, no error | | | |
| 5 | **New** | name and tasks are cleared, cursor is in the name box | | | |
| 6 | **Open** a file that isn't a valid To Do List | ? | | | |

## Commit and push

1. In GitHub Desktop, type **Added save, open and new to To Do List** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-15-advanced-to-do) page.

### Exercise 1

Test case 6 finds a bug: opening a file that isn't valid JSON, or a JSON file without `list_name` and `tasks`, crashes the app. Can you use `try` and `except` so the app shows an error message with `QMessageBox.critical` instead of crashing?
