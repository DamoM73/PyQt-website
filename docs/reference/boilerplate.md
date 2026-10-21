# Boilerplate Code

!!! learn "On this page we will learn"
    - where to find both versions of our boilerplate code
    - when to use each version

These tutorials use two boilerplates. Both have the same structure: a variables section in `__init__`, a `signals` method for connecting signals to slots, and a slots section.

## pyuic6 version

We use this version from [Tutorial 1](../basics/01_creating_apps.md) to [Tutorial 7](../calculator/07_refine.md). It's ***main_window.py*** in the [PyQt6 Boiler Plate repo](https://github.com/DamoM73/PyQt6-Boiler-Plate). It imports the view from a Python file made by `pyuic6`, so we must convert the ***.ui*** file every time we change it:

```text
pyuic6 -o ui_main_window.py -x tutorial_01.ui
```

Widgets are reached through `self.ui`, for example `self.ui.label_2`. [Tutorial 5](../basics/05_signals_slots.md#the-boilerplate-code) explains every line.

```python linenums="1" title="main_window.py"
--8<-- "examples/basics/05_signals_slots/step01/main_window.py"
```

## loadUi version

We use this version from [Tutorial 9](../time_machine/09_loadui.md) onwards. It loads the ***.ui*** file every time the app starts, so there's nothing to convert. Change the file name on line 12 for each new app.

Widgets are reached straight from the window, for example `self.label_clock`. [Tutorial 9](../time_machine/09_loadui.md#a-new-boilerplate) explains every line.

```python linenums="1" title="loadui_boilerplate.py"
--8<-- "examples/time_machine/09_loadui/step02/loadui_boilerplate.py"
```
