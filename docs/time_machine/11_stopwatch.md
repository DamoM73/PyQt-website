# Tutorial 11 - Time Machine Stopwatch

!!! learn "In this tutorial we will learn"
    - how to plan what each stopwatch button should do
    - how a flag variable stores the stopwatch's state
    - how to use a second, independent timer that fires every 100 ms
    - how to add time to a `QTime` and format it to tenths of a second

!!! terms "Terminology"
    - **state** – the situation a program is in at a particular moment, such as the stopwatch running or stopped.
    - **state machine** – a way of thinking about a program as always being in one state, with rules that decide the next state when an event happens.

Now let's make the second tab work: the stopwatch. It also uses a timer. Qt lets us run as many timers as we like, so the stopwatch gets its own, independent of the clock's. The big difference is that this time we care about how much time has passed.

## Plan the stopwatch

The stopwatch has four buttons:

| Button | Action |
| --- | --- |
| **Start** | starts the time counting |
| **Pause** | stops the time if it's counting, or starts it again if it's paused |
| **Stop** | stops the time counting |
| **Reset** | stops the time and sets it back to zero |

So our plan:

- a variable stores the stopwatch's current time
- a flag stores whether the stopwatch is running
- a timer fires every 100 ms; each time, if the stopwatch is running, we add 100 ms to its time and update the display

!!! tip "State machines"
    A **state machine** organises a program so it's in one **state** at a time, such as "running" or "stopped". The program moves between states when events happen, which makes complicated behaviour easier to manage. Flag variables are a simple way to store the state.

    Our stopwatch has two states, stored in `sw_running`:

    | State | Start | Pause | Stop | Reset |
    | --- | --- | --- | --- | --- |
    | running (`True`) | stays running | → stopped | → stopped | → stopped, time is zero |
    | stopped (`False`) | → running | → running | stays stopped | stays stopped, time is zero |

## Code the stopwatch

### Variables

Add the stopwatch's variables to `__init__`.

```python linenums="15" hl_lines="5-7" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step01/time_machine.py:15:25"
```

??? note "Code explanation"
    - **line 19** → creates the stopwatch's own timer, separate from the clock's.
    - **line 20** → stores the stopwatch's time as a `QTime`, starting at 0 hours, 0 minutes, 0 seconds and 0 milliseconds.
    - **line 21** → a flag that stores the stopwatch's state, starting as not running.

### Slots

We need slots before we can connect signals to them. Add each of these at the bottom of the slots section, under a `# stopwatch` comment.

First, the slot that shows the stopwatch's time.

```python linenums="44" hl_lines="6-12" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step02/time_machine.py:44:56"
```

??? note "Code explanation"
    - **line 50** → defines the `show_sw_time` slot.
    - **lines 51–53** → a docstring that explains what the slot does.
    - **line 54** → formats the stopwatch time as `h:mm:ss:zz`. The `zz` code shows the milliseconds without trailing zeros, so because we always count in steps of 100 ms, it shows tenths of a second (`0:00:01:5` is 1.5 seconds).
    - **line 55** → shows the time on the stopwatch label.

Next, the **Start** button's slot. It starts the timer firing every 100 ms and sets the flag to running.

```python linenums="49" hl_lines="9-14" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step03/time_machine.py:49:63"
```

??? note "Code explanation"
    - **line 57** → defines the `start_sw` slot.
    - **lines 58–60** → a docstring that explains what the slot does.
    - **line 61** → starts the stopwatch's timer, so it sends `timeout` every 100 ms.
    - **line 62** → sets the flag, so the stopwatch is running.

The **Pause** button's slot flips the flag.

```python linenums="57" hl_lines="8-12" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step04/time_machine.py:57:69"
```

??? note "Code explanation"
    - **line 64** → defines the `pause_sw` slot.
    - **lines 65–67** → a docstring that explains what the slot does.
    - **line 68** → uses `not` to flip the flag: `True` becomes `False` and `False` becomes `True`. One line handles both pausing and restarting.

The **Stop** button's slot.

```python linenums="64" hl_lines="7-11" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step05/time_machine.py:64:75"
```

??? note "Code explanation"
    - **line 70** → defines the `stop_sw` slot.
    - **lines 71–73** → a docstring that explains what the slot does.
    - **line 74** → sets the flag to not running, so the time stops counting but stays on the display.

The **Reset** button's slot stops the stopwatch and sets its time back to zero.

```python linenums="70" hl_lines="7-13" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step06/time_machine.py:70:83"
```

??? note "Code explanation"
    - **line 76** → defines the `reset_sw` slot.
    - **lines 77–79** → a docstring that explains what the slot does.
    - **line 80** → sets the stopwatch time back to zero.
    - **line 81** → stops the stopwatch.
    - **line 82** → shows the new time straight away. Without this line the display wouldn't change until the next update, and a stopped stopwatch never updates.

Finally, the slot for the timer's `timeout` signal. If the stopwatch is running, it adds 100 ms and refreshes the display.

```python linenums="76" hl_lines="9-15" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step07/time_machine.py:76:91"
```

??? note "Code explanation"
    - **line 84** → defines the `update_stopwatch` slot.
    - **lines 85–87** → a docstring that explains what the slot does.
    - **line 88** → only changes the time if the stopwatch is running…
    - **line 89** → …adding 100 ms to the time. `addMSecs` returns a new `QTime`, so we store it back in `self.sw_time`.
    - **line 90** → shows the new time.

### Signals

Now connect the four buttons and the timer to their slots.

```python linenums="29" hl_lines="8-13" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step08/time_machine.py:29:42"
```

??? note "Code explanation"
    - **lines 37–40** → connect each button's `clicked` signal to its slot.
    - **line 41** → connects the stopwatch timer's `timeout` signal to `update_stopwatch`, so the time goes up every 100 ms while it's running.

### Initial display

Finally, the stopwatch should show `0:00:00:0` when the app starts, so call `show_sw_time` in the initialise displays section.

```python linenums="7" hl_lines="22" title="time_machine.py"
--8<-- "examples/time_machine/11_stopwatch/step09/time_machine.py:7:29"
```

??? note "Code explanation"
    - **line 28** → shows the stopwatch's starting time as soon as the window is created.

!!! primm "PRIMM"
    1. **Predict** what the **Stopwatch** tab will show when the app starts, and after clicking **Start** and waiting 3 seconds.
    2. **Run** ***time_machine.py*** and try each button.
    3. **Investigate**: what's the difference between **Stop** then **Start**, and **Pause** then **Pause**?

## Test the stopwatch

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | start the app | stopwatch shows `0:00:00:0` | | | |
| 2 | **Start**, wait 3 seconds | time counts up to about `0:00:03:0` | | | |
| 3 | **Pause** while running | time stops | | | |
| 4 | **Pause** again | time carries on from where it stopped | | | |
| 5 | **Stop** while running | time stops and stays on the display | | | |
| 6 | **Reset** | display goes back to `0:00:00:0` straight away | | | |

## Commit and push

1. In GitHub Desktop, type **Added Time Machine stopwatch** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-11-time-machine-stopwatch) page.

### Exercise 1

Can you add a **Lap** button that records the current stopwatch time without stopping it? It should:

- be a new push button on the **Stopwatch** tab with the objectName `pushButton_sw_lap`
- add the current time to a new **List Widget** named `listWidget_laps` under the stopwatch
- clear the list when **Reset** is clicked
