# Tutorial 9 - Using loadUi

!!! learn "In this tutorial we will learn"
    - how `uic.loadUi` loads a ***.ui*** file straight into our window
    - how this differs from converting the UI with `pyuic6`
    - how to create a new boilerplate file that uses `loadUi`

!!! terms "Terminology"
    - **loadUi** – a PyQt function that reads a ***.ui*** file while the app runs and builds its widgets inside our window.

So far we've converted every UI file into a Python view file with `pyuic6`. That works, but every time we change the design we have to remember to convert it again. In this tutorial we'll learn another way: our Python file loads the ***.ui*** file directly, so the app always uses the latest design.

## Two ways to use a UI file

| | `pyuic6` | `uic.loadUi` |
| --- | --- | --- |
| How it works | converts the ***.ui*** file into a Python view file before we run the app | reads the ***.ui*** file every time the app starts |
| After changing the design | convert it again | just run the app |
| How our code gets a widget | `self.ui.label_display` | `self.label_display` |
| Files needed | the controller and the view file (***ui_calculator.py***) | the controller and the ***.ui*** file |

We'll use `loadUi` for the rest of these tutorials. Both ways are common, so it's worth knowing both.

## A new boilerplate

### Load the UI

1. In VS Code, create a new file, add the code below and save it as ***loadui_boilerplate.py***.

```python linenums="1" title="loadui_boilerplate.py"
--8<-- "examples/time_machine/09_loadui/step01/loadui_boilerplate.py"
```

??? note "Code explanation"
    - **line 1** → imports `sys`, just like the old boilerplate.
    - **line 2** → imports `uic`, PyQt's UI tools, which include `loadUi`.
    - **line 3** → imports `QApplication` and `QMainWindow`. There's no `Ui_MainWindow` import this time, because there's no view file.
    - **line 6** → defines our `MainWindow` class as a subclass of `QMainWindow`.
    - **line 7** → defines `__init__`, which runs when the window is created.
    - **lines 8–10** → a docstring that explains what `__init__` does.
    - **line 11** → runs `QMainWindow`'s own `__init__`.
    - **line 12** → loads ***time_machine.ui*** from the same folder and builds all its widgets inside our window (`self`). Every widget becomes an attribute of the window, named by its objectName.
    - **line 15** → only runs the code below when this file is run directly.
    - **lines 16–19** → create the application and our window, show the window and start the event loop.

!!! primm "PRIMM"
    1. **Predict** what will appear when you run the file.
    2. **Run** ***loadui_boilerplate.py***.
    3. **Investigate**: in Qt Designer, change the **Clock** tab's label text, save ***time_machine.ui***, and run the file again without converting anything. What changes?

!!! warning "File not found?"
    `loadUi` looks for the ***.ui*** file in the folder VS Code is running from. If the error message ends with `invalid Qt Designer file: [Errno 2] No such file or directory: 'time_machine.ui'`, check that the UI file is saved in the repo folder (next to the Python file) and that its name is spelt exactly the same, including capitals. The [Common Errors](../reference/common_errors.md#ui-file-not-found) page shows the whole message.

### Complete the boilerplate

Now that the UI loads, let's add the rest of our usual structure: the variables section, the `signals` method and the slots section. Add the highlighted code below.

```python linenums="1" hl_lines="14 16-17 19-23 25-28" title="loadui_boilerplate.py"
--8<-- "examples/time_machine/09_loadui/step02/loadui_boilerplate.py"
```

??? note "Code explanation"
    - **line 17** → calls `signals`, so the signals are connected as soon as the window is created.
    - **line 19** → defines the `signals` method, where we'll connect signals to slots.
    - **lines 20–22** → a docstring that explains what `signals` is for.
    - **line 23** → a `pass` placeholder until we add connections.
    - **lines 26–28** → a string that marks where the slot methods go.

This is our new boilerplate. For each new app we'll copy it and change the name of the ***.ui*** file on line 12. The [Boilerplate Code](../reference/boilerplate.md) page has both versions, in case we need them again.

!!! tip "No more self.ui"
    With `loadUi`, the widgets belong to the window itself. So where the calculator used `self.ui.label_display`, the Time Machine will use `self.label_clock`. Using `self.ui.` with `loadUi` gives an `AttributeError`.

## Commit and push

1. In GitHub Desktop, type **Added loadUi boilerplate** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.
