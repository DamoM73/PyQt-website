# Common Errors

!!! learn "On this page we will learn"
    - how to read the errors we're most likely to see while building PyQt apps
    - what causes each error, and how to fix it

When our app crashes, Python prints a **traceback** in the VS Code terminal. Read it from the bottom up: the last line says what went wrong, and the lines above it show which line of our code it happened on. (Paths in the examples below are shortened; yours will show where your repo is.)

## No module named 'PyQt6'

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 2, in <module>
    from PyQt6 import uic
ModuleNotFoundError: No module named 'PyQt6'
```

- **line 2** → the error happened on line 2 of ***time_machine.py***, the first PyQt6 import.
- **line 4** → Python can't find PyQt6.

**Cause:** VS Code is running our file with a Python that doesn't have PyQt6 installed, usually because the virtual environment isn't selected.

**Fix:** press ++ctrl+shift+p++ (++cmd+shift+p++ on macOS), choose **Python: Select Interpreter** and pick the one with `.venv` in its name. If there's no `.venv`, follow the [virtual environment](../start/setup.md#virtual-environment) steps in Setup.

## pyuic6 is not recognised

If typing a `pyuic6` command in the terminal says something like **pyuic6 is not recognized** (Windows) or **command not found** (macOS), the terminal isn't using our virtual environment, which is where `pyuic6` was installed.

**Fix:** close the terminal (bin icon), open a new one (**Terminal** → **New Terminal**) and check the prompt starts with `(.venv)`, then run the command again.

## The wrong UI appears

This isn't an error message: the app runs, but it shows the UI from an earlier tutorial.

**Cause:** with the `pyuic6` boilerplate, our controller imports its view from a Python view file. Either we forgot to convert the new ***.ui*** file, or the import on line 3 still names the old view file.

**Fix:** convert the UI file again (for example `pyuic6 -o ui_calculator.py -x calculator.ui`) and check line 3 imports from the right file. See [Tutorial 6](../calculator/06_create.md#create-the-controller-file).

## UI file not found

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 13, in __init__
    uic.loadUi("time_machin.ui", self)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
PyQt6.uic.exceptions.UIFileException: time_machin.ui: invalid Qt Designer file: [Errno 2] No such file or directory: 'time_machin.ui'
```

- **line 2** → the error happened on line 13, where `loadUi` loads the UI file.
- **line 5** → there's no file called ***time_machin.ui***. (The real message is much longer, because it also shows the lines inside PyQt that tried to open the file, but this is the part that matters.)

**Cause:** the file name in `loadUi` doesn't match the ***.ui*** file exactly (here it's misspelt), or the ***.ui*** file isn't saved in the repo folder.

**Fix:** check the spelling, including capitals, and check the ***.ui*** file is next to the Python file in VS Code's file panel.

## No attribute 'ui'

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 48, in <module>
    window = MainWindow()
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 23, in __init__
    self.show_time()
    ~~~~~~~~~~~~~~^^
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 43, in show_time
    self.ui.label_clock.setText(formatted_time)
    ^^^^^^^
AttributeError: 'MainWindow' object has no attribute 'ui'
```

- **lines 2–3** → the crash started when the window was created on line 48.
- **lines 4–6** → `__init__` called `show_time` on line 23.
- **lines 7–9** → the problem is `self.ui` on line 43.
- **line 10** → our window has no attribute called `ui`.

**Cause:** this file uses `loadUi`, which puts the widgets straight into the window, so there's no `self.ui`.

**Fix:** use `self.label_clock` instead of `self.ui.label_clock`. (The opposite is also true: with the `pyuic6` boilerplate we must use `self.ui.`.) See [Tutorial 9](../time_machine/09_loadui.md#complete-the-boilerplate).

## No attribute 'label_clok'

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 48, in <module>
    window = MainWindow()
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 23, in __init__
    self.show_time()
    ~~~~~~~~~~~~~~^^
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 43, in show_time
    self.label_clok.setText(formatted_time)
    ^^^^^^^^^^^^^^^
AttributeError: 'MainWindow' object has no attribute 'label_clok'. Did you mean: 'label_clock'?
```

- **lines 7–9** → the problem is `self.label_clok` on line 43.
- **line 10** → there's no widget called `label_clok`, and Python suggests the name we probably meant.

**Cause:** the widget name in our code doesn't match its **objectName** in Qt Designer.

**Fix:** check the objectName in Qt Designer's Property Editor and use exactly the same name, including capitals. Accepting VS Code's suggestions as we type helps avoid this.

## Unexpected type 'NoneType'

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 48, in <module>
    window = MainWindow()
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 20, in __init__
    self.signals()
    ~~~~~~~~~~~~^^
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\time_machine.py", line 30, in signals
    self.clock_timer.timeout.connect(self.show_time())
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
TypeError: argument 1 has unexpected type 'NoneType'
```

- **lines 7–9** → the problem is the `connect` on line 30.
- **line 10** → `connect` was given `None` instead of a method.

**Cause:** there are brackets after the slot's name: `self.show_time()`. The brackets **call** the method straight away, and `connect` gets the value it returns, which is `None`.

**Fix:** remove the brackets, so we pass the method itself: `connect(self.show_time)`.

## The app closes when a button is clicked

If the app suddenly closes when we click something, scroll up in the terminal to find the traceback. Since PyQt 5.5, an unhandled error inside a slot ends the whole app. The traceback tells us which slot and which line, just like the [operator first](../calculator/07_refine.md#operator-first) error in Tutorial 7.
