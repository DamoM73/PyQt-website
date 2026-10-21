# Tutorial 14 - Basic To Do

!!! learn "In this tutorial we will learn"
    - how to use a list widget as the place our app stores its data
    - how to get text from the user with an input dialog
    - how tuple unpacking works with a method that returns two values
    - how a signal can pass information, such as the item that was clicked, to its slot

!!! terms "Terminology"
    - **dialog box** – a small pop-up window that shows the user a message or asks them for input.
    - **tuple** – a group of values written in round brackets that works like a list but can't be changed.
    - **unpacking** – storing each value from a tuple or list in its own variable in one line, such as `new_task, ok = ...`.
    - **safety** – the usability principle that a digital solution helps users avoid serious errors and recover easily when something goes wrong.

In this tutorial we'll build the basic features of our To Do List:

- naming the list
- adding tasks to the list
- showing all the tasks
- removing tasks from the list

## Plan the basic To Do List

Naming the list is already done: the user types the name into the line edit, and Qt handles that for us. So we only need to plan adding and removing tasks.

- **Storing the data**: we'll store the tasks in the list widget itself. It's the **model** and part of the **view** at the same time, which is fine for a small app.
- **Adding a task**: clicking **Add item** opens an input **dialog box**, where the user types the new task. If they click **OK**, the task is added to the list.
- **Removing a task**: the list widget sends an `itemClicked` signal when a task is clicked, and the signal passes along the item that was clicked. We'll use it to remove that task.

!!! tip "Dialog boxes"
    Qt's ready-made **dialog boxes** are pop-up windows that let our app talk to the user. A message box shows a warning, a file dialog lets the user choose a file, and an input dialog asks them to type something. Qt builds them for us, so we only need a line or two of code. The [Qt dialog documentation](https://doc.qt.io/qt-6/dialogs.html) lists the rest.

This code is a bit more complicated, so we'll change our process slightly. Instead of adding all the slots and then all the signals, we'll work in slot/signal pairs, so we can test each pair before moving on.

## Set up to_do_list.py

1. Copy ***loadui_boilerplate.py*** and rename the copy ***to_do_list.py***.
2. Change the ***.ui*** file name on line 12, and add `QInputDialog` to the imports, as highlighted below.

```python linenums="1" hl_lines="3 12" title="to_do_list.py"
--8<-- "examples/to_do/14_basic/step01/to_do_list.py"
```

??? note "Code explanation"
    - **line 3** → adds `QInputDialog`, Qt's ready-made input dialog.
    - **line 12** → loads ***to_do_list.ui*** instead of ***time_machine.ui***.

We won't need any variables for this app, because all the data is stored in the widgets.

## Add a task

The first slot/signal pair is for the **Add item** button. Add the slot under the slots string.

```python linenums="26" hl_lines="4-12" title="to_do_list.py"
--8<-- "examples/to_do/14_basic/step02/to_do_list.py:26:38"
```

??? note "Code explanation"
    - **line 29** → defines the `add_task` slot.
    - **lines 30–32** → a docstring that explains what the slot does.
    - **lines 33–35** → opens an input dialog with the title **Add Task** and the prompt **Enter a new task:**, and waits for the user. The first argument, `self`, makes our window the dialog's parent, so the dialog appears over it. The dialog returns two values, which we unpack into `new_task` and `ok`.
    - **line 36** → only carries on if the user clicked **OK** (`ok` is `True`) and typed something (`new_task` isn't an empty string)…
    - **line 37** → …and adds the new task to the list widget.

!!! tip "Tuple unpacking"
    When a method returns a **tuple**, such as `("Pack hat", True)`, Python lets us unpack its values straight into separate variables. `QInputDialog.getText` returns two values:

    - the text in the dialog's text box
    - a Boolean that's `True` if **OK** was clicked

    On line 33 we unpack them into `new_task` and `ok`, so we can check each one separately.

Now connect the button's signal to the slot, replacing the `pass` line in `signals`.

```python linenums="19" hl_lines="5" title="to_do_list.py"
--8<-- "examples/to_do/14_basic/step03/to_do_list.py:19:24"
```

??? note "Code explanation"
    - **line 23** → connects the **Add item** button's `clicked` signal to `add_task`.

!!! primm "PRIMM"
    1. **Predict** what will happen when you click **Add item**, type a task and click **OK**. What will happen if you click **Cancel** instead?
    2. **Run** ***to_do_list.py*** and test it.
    3. **Investigate**: what happens if you click **OK** without typing anything? Which part of line 36 handles that?

### Test adding tasks

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | click **Add item** | input dialog opens | | | |
| 2 | type a task, click **OK** | task appears in the list | | | |
| 3 | leave the box empty, click **OK** | nothing is added | | | |
| 4 | type a task, click **Cancel** | nothing is added | | | |

## Remove a task

When the user clicks a task, the list widget's `itemClicked` signal passes the clicked **item** to the slot. We can ask the list widget which row that item is in, then remove that row.

Add the slot after `add_task`.

```python linenums="36" hl_lines="4-9" title="to_do_list.py"
--8<-- "examples/to_do/14_basic/step04/to_do_list.py:36:45"
```

??? note "Code explanation"
    - **line 39** → defines the `delete_item` slot. It has a second parameter, `item`, because the `itemClicked` signal sends the clicked item.
    - **lines 40–42** → a docstring that explains what the slot does.
    - **line 43** → asks the list widget for the row number of the clicked item.
    - **line 44** → removes the item in that row from the list.

Now connect the signal.

```python linenums="19" hl_lines="6" title="to_do_list.py"
--8<-- "examples/to_do/14_basic/step05/to_do_list.py:19:25"
```

??? note "Code explanation"
    - **line 24** → connects the list widget's `itemClicked` signal to `delete_item`.

!!! primm "PRIMM"
    1. **Predict** what will happen when you click a task in the list.
    2. **Run** ***to_do_list.py***, add three tasks, and click the middle one.
    3. **Investigate**: what would happen if you clicked a task by accident? Is that good design?

!!! tip "Digital Solutions link"
    Deleting a task with one click, with no warning and no undo, goes against the **safety** usability principle: the app should help users avoid serious errors and recover from them. See [Usability](https://damom73.github.io/digital-solutions-text-2025/usability-principles) in the Digital Solutions text, then try Exercise 1.

## Commit and push

1. In GitHub Desktop, type **Added basic To Do List** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-14-basic-to-do) page.

### Exercise 1

Can you make the app ask "Delete this task?" before it removes a task, and only remove it if the user clicks **Yes**? Look up `QMessageBox.question` in the [QMessageBox documentation](https://doc.qt.io/qt-6/qmessagebox.html).
