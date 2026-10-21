# Tutorial 12 - Time Machine Timer

!!! learn "In this tutorial we will learn"
    - how to read values from spin boxes and turn them into a `QTime`
    - how to count down by subtracting time, and stop at zero
    - how to keep helper methods that aren't slots in their own section
    - how to play a sound with `QSoundEffect`

!!! terms "Terminology"
    - **utility method** – a helper method that isn't connected to a signal, but is called by other methods to do a job, such as converting values.

In this tutorial we'll finish the last tab of the Time Machine: the timer.

## Plan the timer

The big difference from the stopwatch is the spin boxes, which set the timer's starting time. When we tested the UI, the spin boxes' arrows already changed their values, so we can use that built-in feature: when **Start** is clicked, we read the three spin boxes and make a starting time from them.

Once we have the starting time, the timer works like the stopwatch, except it takes time away instead of adding it.

Then we need to decide what happens when the timer reaches zero:

1. the timer stops counting down
2. an alarm sounds

| Button | Action |
| --- | --- |
| **Start** | sets the time from the spin boxes and starts counting down |
| **Pause** | pauses the countdown, or starts it again if it's paused |
| **Stop** | stops the countdown and sets the time to zero |
| **Reset** | sets the time back to the spin boxes' values, without changing whether it's running |

## Code the timer

### Variables

Add the same kinds of variables we used for the stopwatch. This time we only need hours, minutes and seconds.

```python linenums="15" hl_lines="9-11" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step01/time_machine.py:15:27"
```

??? note "Code explanation"
    - **line 23** → creates the timer's own `QTimer`.
    - **line 24** → stores the time left, starting at zero.
    - **line 25** → a flag that stores whether the timer is counting down.

### Show the timer's time

Add the slot that shows the timer's time at the bottom of the slots section, under a `# timer` comment.

```python linenums="96" hl_lines="9-15" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step02/time_machine.py:96:111"
```

??? note "Code explanation"
    - **line 105** → defines the `show_tm_time` slot.
    - **lines 106–108** → a docstring that explains what the slot does.
    - **line 109** → formats the time as `h:mm:ss`.
    - **line 110** → shows the time on the timer label.

### Convert the spin boxes to a time

Before we can write the **Start** slot, we need a method that turns the spin box values into a `QTime`. It isn't a slot, because no signal calls it, so it goes in a new **utilities** section below the slots.

```python linenums="104" hl_lines="9-17" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step03/time_machine.py:104:121"
```

??? note "Code explanation"
    - **line 113** → defines the `spinbox_to_time` utility method.
    - **lines 114–116** → a docstring that explains what the method does.
    - **lines 117–119** → read each spin box's current value with its `value` method.
    - **line 120** → returns a new `QTime` made from the three values, so the code that called it gets the time back.

### Start the timer

Now add the **Start** slot, after `show_tm_time`.

```python linenums="105" hl_lines="8-15" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step04/time_machine.py:105:122"
```

??? note "Code explanation"
    - **line 112** → defines the `start_timer` slot.
    - **lines 113–115** → a docstring that explains what the slot does.
    - **line 116** → sets the time left from the spin boxes, using our utility method.
    - **line 117** → starts the timer, firing every second.
    - **line 118** → sets the flag, so the timer is counting down.
    - **line 119** → shows the starting time straight away.

### The other buttons

The **Pause**, **Stop** and **Reset** slots follow the same pattern as the stopwatch's.

```python linenums="112" hl_lines="10-14 16-22 24-29" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step05/time_machine.py:112:141"
```

??? note "Code explanation"
    - **line 121** → defines the `pause_timer` slot.
    - **lines 122–124** → a docstring that explains what the slot does.
    - **line 125** → flips the flag, so one button pauses and restarts the countdown.
    - **line 127** → defines the `stop_timer` slot.
    - **lines 128–130** → a docstring that explains what the slot does.
    - **line 131** → stops the countdown.
    - **line 132** → sets the time left to zero.
    - **line 133** → shows the zero time straight away.
    - **line 135** → defines the `reset_timer` slot.
    - **lines 136–138** → a docstring that explains what the slot does.
    - **line 139** → sets the time left back to the spin boxes' values.
    - **line 140** → shows the new time straight away.

### Count down

The last slot runs every time the timer fires. If the timer is counting down, it takes away one second, and when the time reaches zero it stops.

```python linenums="135" hl_lines="8-16" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step06/time_machine.py:135:151"
```

??? note "Code explanation"
    - **line 142** → defines the `update_timer` slot.
    - **lines 143–145** → a docstring that explains what the slot does.
    - **line 146** → only counts down if the timer is running…
    - **line 147** → …taking one second away. `addSecs(-1)` adds negative one second, which returns a new `QTime`.
    - **line 148** → shows the new time.
    - **line 149** → checks whether the time has reached zero…
    - **line 150** → …and if so, stops the countdown.

### Signals

Connect the four buttons and the timer to their slots.

```python linenums="34" hl_lines="15-20" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step07/time_machine.py:34:54"
```

??? note "Code explanation"
    - **lines 49–52** → connect each timer button's `clicked` signal to its slot.
    - **line 53** → connects the timer's `timeout` signal to `update_timer`, so it counts down every second.

### Initial display

Finally, show the timer's starting time when the app opens.

```python linenums="15" hl_lines="19" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step08/time_machine.py:15:34"
```

??? note "Code explanation"
    - **line 33** → shows `0:00:00` on the timer tab as soon as the window is created.

!!! primm "PRIMM"
    1. **Predict** what will happen if you set the spin boxes to 0 hours, 0 minutes and 5 seconds, then click **Start**.
    2. **Run** ***time_machine.py*** and test it.
    3. **Investigate**: try every button while the timer is counting down. Does each one do what the plan says?

---

## Add an alarm

Most timers sound an alarm when they reach zero, so let's add one to ours.

### Get the sound file

We'll use this sound effect: [alarm_sound.wav](../downloads/alarm_sound.wav).

1. Download ***alarm_sound.wav*** and move it into your repo, in the same folder as ***time_machine.py***.
    - Why: like `loadUi`, Qt looks for the file in the folder VS Code runs our app from.

### Import the modules

Qt handles sound in its multimedia module. We'll use `QSoundEffect` from `QtMultimedia`, which plays short sounds. To tell it where the sound file is, we also need `QUrl` from `QtCore`.

```python linenums="1" hl_lines="4-5" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step09/time_machine.py:1:7"
```

??? note "Code explanation"
    - **line 4** → adds `QUrl`, which describes the location of a file.
    - **line 5** → imports `QSoundEffect`, which loads and plays a short sound.

### Set up the sound

Add the alarm's variables after the other timer variables.

```python linenums="23" hl_lines="5-8" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step10/time_machine.py:23:32"
```

??? note "Code explanation"
    - **line 27** → creates a `QSoundEffect` for the alarm.
    - **line 28** → loads ***alarm_sound.wav***. `QUrl.fromLocalFile` turns the file name into the kind of location `QSoundEffect` needs.
    - **line 29** → plays the sound once each time it's played.
    - **line 30** → sets the volume to half (volumes go from `0.0` to `1.0`).

### Play the alarm

We already check for zero in `update_timer`, so that's where the alarm goes.

```python linenums="155" hl_lines="10" title="time_machine.py"
--8<-- "examples/time_machine/12_timer/step11/time_machine.py:155:165"
```

??? note "Code explanation"
    - **line 164** → plays the alarm when the time reaches zero.

!!! primm "PRIMM"
    1. **Predict** what will happen when a 3-second timer finishes.
    2. **Run** ***time_machine.py*** and test it (turn your sound on).
    3. **Investigate**: what happens if you click **Start** without setting any time? What happens if you set the minutes to `75`? Keep your answers for the exercises.

## Test the timer

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | start the app | timer shows `0:00:00` | | | |
| 2 | set 0:00:05, **Start** | counts down to `0:00:00`, stops, alarm sounds | | | |
| 3 | **Pause** while counting | countdown stops; **Pause** again carries on | | | |
| 4 | **Stop** while counting | countdown stops and shows `0:00:00` | | | |
| 5 | **Reset** while counting | time goes back to the spin box values | | | |
| 6 | **Start** with all spin boxes at 0 | ? | | | |
| 7 | set minutes to `75`, **Start** | ? | | | |

## Commit and push

1. In GitHub Desktop, type **Added Time Machine timer** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-12-time-machine-timer) page.

### Exercise 1

Test case 6 finds a bug: if we click **Start** with all the spin boxes at zero, the timer counts down from `23:59:59`. Can you fix it so **Start** does nothing when the time is zero?

### Exercise 2

Test case 7 finds another bug: a spin box goes up to 99, but a `QTime` can't have 75 minutes, so the display goes blank. Can you limit the spin boxes so they can only hold valid times (hours 0–23, minutes 0–59, seconds 0–59)? You can do it in Qt Designer (the spin box's **maximum** property) or in `__init__` with each spin box's `setMaximum` method.
