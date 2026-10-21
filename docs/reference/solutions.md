# Exercise Solutions

These are **a** solution to each exercise. There are many ways to solve each problem, and any code that produces the required result is a correct solution. The highlighted lines are the ones that changed from the end of the tutorial.

Exercises for the Qt Designer tutorials ask us to design our own UI, so they don't have solutions here.

## Tutorial 5 - Signals and Slots

### Exercise 1

Add a push button named `pushButton_reset` to ***tutorial_05.ui*** and convert it again, then:

```python linenums="1" hl_lines="25 31-32" title="first_program.py"
--8<-- "solutions/basics/05_signals_slots/ex1_reset_button.py"
```

## Tutorial 6 - Create Calculator App

### Exercise 1

Add a push button named `pushButton_clear` to ***calculator.ui*** and convert it again. Because `update_display` only shows the equation, `clear_clicked` sets the display back to `0` itself.

```python linenums="1" hl_lines="40 106-108" title="calculator.py"
--8<-- "solutions/calculator/06_create/ex1_clear_button.py"
```

## Tutorial 7 - Refine Calculator App

### Exercise 1

`eval()` raises a `SyntaxError` when the equation is empty or ends with an operator, so we catch that as well, then clear the equation so the next button starts again.

```python linenums="1" hl_lines="191-192 196" title="calculator.py"
--8<-- "solutions/calculator/07_refine/ex1_syntax_error.py"
```

### Exercise 2

Each number slot now calls `number_clicked` with its digit, so the logic is written once. (`zero_clicked` keeps its own code, because zero follows different rules.)

```python linenums="1" hl_lines="49 52 55 58 61 64 67 70 73 135-143" title="calculator.py"
--8<-- "solutions/calculator/07_refine/ex2_number_clicked.py"
```

## Tutorial 10 - Time Machine Clock

### Exercise 1

The clock only updates every 5 seconds, so the seconds jump by 5 instead of ticking over each second. The timer's interval is in milliseconds, and `timeout` is only sent when the interval runs out, so `show_time` only runs every 5000 ms.

### Exercise 2

Capital `HH` gives the hour from `00` to `23` with a leading zero, and leaving out `a` turns off am/pm.

```python linenums="1" hl_lines="42" title="time_machine.py"
--8<-- "solutions/time_machine/10_clock/ex2_24_hour.py"
```

## Tutorial 11 - Time Machine Stopwatch

### Exercise 1

Add a push button named `pushButton_sw_lap` and a list widget named `listWidget_laps` to the **Stopwatch** tab in ***time_machine.ui***, then:

```python linenums="1" hl_lines="42 92 94-99" title="time_machine.py"
--8<-- "solutions/time_machine/11_stopwatch/ex1_lap_button.py"
```

## Tutorial 12 - Time Machine Timer

### Exercise 1

If the spin boxes are all zero, `return` ends `start_timer` straight away, before the timer starts.

```python linenums="1" hl_lines="130-131" title="time_machine.py"
--8<-- "solutions/time_machine/12_timer/ex1_zero_start.py"
```

### Exercise 2

This solution sets the limits in code. Setting each spin box's **maximum** property in Qt Designer works just as well.

```python linenums="1" hl_lines="31-33" title="time_machine.py"
--8<-- "solutions/time_machine/12_timer/ex2_spinbox_limits.py"
```

## Tutorial 14 - Basic To Do

### Exercise 1

`QMessageBox.question` shows **Yes** and **No** buttons and returns the button that was clicked.

```python linenums="1" hl_lines="3 44-49" title="to_do_list.py"
--8<-- "solutions/to_do/14_basic/ex1_confirm_delete.py"
```

## Tutorial 15 - Advanced To Do

### Exercise 1

Reading the file and getting both keys go inside the `try` block, so a bad file or a missing key is caught before the UI changes.

```python linenums="1" hl_lines="4 97-107 109" title="to_do_list.py"
--8<-- "solutions/to_do/15_advanced/ex1_invalid_json.py"
```

## Tutorial 17 - Contact App

### Exercise 1

Add a push button named `pushButton_delete` beside **Add** in ***contacts.ui***, then:

```python linenums="1" hl_lines="54 143-149" title="contacts.py"
--8<-- "solutions/contacts/17_app/ex1_delete_contact.py"
```
