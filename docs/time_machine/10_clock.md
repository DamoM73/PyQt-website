# Tutorial 10 - Time Machine Clock

!!! learn "In this tutorial we will learn"
    - why `sleep` doesn't work in a GUI app
    - how a `QTimer` sends a `timeout` signal at regular intervals
    - how to get the current time with `QTime` and format it with `toString`
    - how to show a value as soon as the app starts

!!! terms "Terminology"
    - **event loop** – the part of an event-driven program that keeps checking for events and runs the matching event handlers.
    - **blocking** – describes code that stops everything else in the program from running until it finishes, such as `sleep`.
    - **timer** – an object that sends a signal after a set number of milliseconds, either once or again and again.

The usual way to deal with time in Python is `sleep`. But `sleep` doesn't work in a GUI app, because it's **blocking**: it stops the whole program while it waits. Buttons stop responding, nothing on screen updates, and the app looks frozen.

That's because GUI apps rely on the **event loop**, which keeps checking for things like clicks and updates. `sleep` blocks the event loop, so none of those get handled. Instead, GUI apps use **timers**, which let the app keep responding while it waits.

!!! tip "Qt timers"
    Qt's main timer class is `QTimer`. It sends a `timeout` signal after a set interval, and works through the event loop, so it never blocks. A timer can fire once (single-shot) or repeat at regular intervals. The [QTimer documentation](https://doc.qt.io/qt-6/qtimer.html) has all the details.

## Create time_machine.py

1. Copy ***loadui_boilerplate.py*** and rename the copy ***time_machine.py***.
    - Result: ***time_machine.py*** already loads ***time_machine.ui***, because that's the file our boilerplate loads.

## Plan the clock

A `QTimer` has a signal called `timeout` that's sent when its time runs out. We'll use it to update the clock every second. To do that we need to:

1. create a timer
2. write a slot that shows the current time
3. show the current time as soon as the app starts
4. start the timer, so it sends `timeout` every 1000 ms
5. connect the timer's `timeout` signal to our slot

## Code the clock

### 1. Create the timer

Import the two Qt time classes we need, by adding the highlighted line.

```python linenums="1" hl_lines="4" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step01/time_machine.py"
```

??? note "Code explanation"
    - **line 4** → imports `QTime` (which stores a time of day) and `QTimer` (which sends timed signals) from Qt's core module.

The clock timer needs to exist from the moment the app starts, so we create it in `__init__`.

```python linenums="7" hl_lines="10" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step02/time_machine.py:7:21"
```

??? note "Code explanation"
    - **line 16** → creates a `QTimer` and stores it as `self.clock_timer`, so other methods can use it.

### 2. Write the slot

Next we need a slot that shows the current time. Add it under the slots string. The `# clock` comment helps us find the clock's code, because this file will grow.

```python linenums="24" hl_lines="8-15" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step03/time_machine.py:24:39"
```

??? note "Code explanation"
    - **line 32** → defines the `show_time` slot.
    - **lines 33–35** → a docstring that explains what the slot does.
    - **line 36** → gets the current time from the computer as a `QTime` object.
    - **line 37** → turns the time into a string in the format `h:mm:ssa`, such as `9:05:42am`.
    - **line 38** → shows that string on the clock label.

!!! tip "Formatting time"
    There are lots of ways to show a time, and `toString` lets us choose. Some useful codes:

    | Code | Meaning | Example |
    | --- | --- | --- |
    | `h` | hour, no leading zero (12-hour if `a` is used) | `9` |
    | `hh` | hour with a leading zero | `09` |
    | `mm` | minutes with a leading zero | `05` |
    | `ss` | seconds with a leading zero | `42` |
    | `a` | `am` or `pm` | `am` |

    The [QTime toString documentation](https://doc.qt.io/qt-6/qtime.html#toString) lists every option.

### 3. Show the time when the app starts

We want the time on the screen the instant the app opens, not one second later. So we call `show_time` at the end of `__init__`, in a new section.

```python linenums="7" hl_lines="15-16" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step04/time_machine.py:7:24"
```

??? note "Code explanation"
    - **line 22** → calls `show_time` once when the window is created, so the clock never starts blank.

### 4. Start the timer

Now set the timer to fire every 1000 ms (one second).

```python linenums="7" hl_lines="11" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step05/time_machine.py:7:24"
```

??? note "Code explanation"
    - **line 17** → starts the timer with an interval of 1000 milliseconds. It keeps sending `timeout` every second until it's stopped.

### 5. Connect the signal

Finally, replace the `pass` in `signals` with the connection.

```python linenums="1" hl_lines="29-30" title="time_machine.py"
--8<-- "examples/time_machine/10_clock/step06/time_machine.py"
```

??? note "Code explanation"
    - **line 30** → connects the timer's `timeout` signal to `show_time`, so the clock updates every second.

!!! primm "PRIMM"
    1. **Predict** what the **Clock** tab will show.
    2. **Run** ***time_machine.py*** and look at the **Clock** tab.
    3. **Investigate**: is the time correct? Does it tick over every second? Click the other tabs. Does the app still respond while the clock runs?

## Commit and push

1. In GitHub Desktop, type **Added Time Machine clock** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-10-time-machine-clock) page.

### Exercise 1

What happens if you change the timer's interval from `1000` to `5000`? Why do you think this happens?

### Exercise 2

Can you change the clock to show 24-hour time with leading zeros, such as `09:05:42` or `21:05:42`?
