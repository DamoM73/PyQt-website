# Tutorial 10 - Time Machine Clock

```{admonition} In this tutorial you will:
- Learn how to use **QTimers** to manage time-based events and update the displayed time every second.  
- Create and configure a timer to emit signals at regular intervals using the **timeout** signal.  
- Display and format the current time using Qt’s **toString** method.  
- Test and experiment with timer intervals and time display customisation.
```

The traditional way of dealing with time in Python is to use `sleep`. However, using `sleep` in a UI doesn't work well because it stops everything in the program while it waits. When `sleep` is used, the entire application pauses, including the user interface, so buttons won’t respond, animations will freeze, and the app may appear stuck. 

This happens because most UIs rely on something called an event loop, which constantly checks for things like user actions or updates. `sleep` blocks this loop, preventing it from handling those tasks. Instead of using `sleep`, developers use timers or asynchronous functions, which allow the app to keep responding while performing tasks in the background.

In this lesson you will learn to how to use Qt's built-in timer class.

```{admonition} Flag Variables
:class: hint
Qt provides powerful timer classes that allow developers to manage time-based events in their applications. The primary class is QTimer, which can emit signals at specified intervals, making it useful for tasks like animations, updates, or periodic checks. It operates using the event loop, ensuring efficient and non-blocking execution. Developers can configure timers to be single-shot, firing only once, or to repeat at regular intervals. 

You can find more details on the **[Official Qt Documentation](https://doc.qt.io/qt-6/qtimer.html)**
```

## Create the time_machine.py

Copy the boilerplate that you created in the last tutorial and call it `time_machine.py`.

## Planning the Clock Code
Now lets make the clock work. In Qt timers have a signal called `timeout` that triggers when the set time has expired. We will use that make the clock update the display every second. 

To achieve that we need to:
1. Create a timer
2. Display the current time when the app starts
3. Set the timer to give a signal every 1000ms
4. When the time timer runs out, update the displayed time

## Implementing the Clock Code

1. Import the Qt time modules that we will use for the clock.

![import modules](./assets/img/12/01_import.png)

2. The clock timer needs to be created when the app launches, so we include it in the `__init__`.

![clock timer](./assets/img/12/02_clock_timer.png)

3. We then need a slot that displays the current time.

![show time slot](./assets/img/12/03_show_time.png)

```{admonition} Formatting time
:class: hint
There are so many different ways to display time. Qt's `toString` method allows you to determine the format of the time you display. We will look at some of the formatting methods in these tutorials, but if you want to explore your options you can look at the **[Official Qt Documentaion](https://doc.qt.io/qt-6/qtime.html#toString-1)**
```

4. We want the time to be displayed the instant the app starts, so we should call `show_time` in the `__init__`.

![call show time](./assets/img/12/04_call_show_time.png)

5. Now set and start the timer when the app launches.

![start timer](./assets/img/12/05_start_timer.png)

6. Finally connect the timer signal to the `show_time` slot.

![connect signal to slot](./assets/img/12/06_connect_timer_signal_to_slot.png)

## Testing

Run your app and navigate to the clock tab.

Check that:

- That the time is correct.
- That the clock ticks over every second.

## Exploration

Try a bit of exploring the code:

- What happens if you change the timer value from `1000`
- Can you change the time format to display differently?