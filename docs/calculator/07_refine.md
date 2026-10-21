# Tutorial 7 - Refine Calculator App

!!! learn "In this tutorial we will learn"
    - how to calculate the equation with `eval()` when `=` is clicked
    - how to use flag variables to remember what has already happened
    - how to test systematically to find problems, then plan rules to fix them
    - how to read a traceback and guard against the error it describes
    - how to handle an exception with `try` and `except`

!!! terms "Terminology"
    - **flag variable** – a variable that stores `True` or `False` to control part of a program, such as `running` keeping the main loop going.
    - **systematic testing** – testing every combination of inputs in an organised order, so no path through the program is missed.
    - **test coverage** – how much of a program's possible behaviour our tests check.
    - **traceback** – the error report Python prints when a program crashes, showing the path it took to the error with the most recent step last.
    - **index** – the number that gives an item's position in a list, starting from `0`.
    - **string slicing** – making a new string from part of another one, such as `text[:-1]` for everything except the last character.
    - **exception** – an error that happens while a program is running, such as dividing by zero.
    - **leading zero** – a `0` at the start of a whole number, such as the `0` in `09`.
    - **try block** – code inside `try` that Python runs while watching for errors, so a matching `except` can catch an error instead of the program crashing.

In the last tutorial we built a calculator that shows the buttons we click. Now it's time to make it calculate, and to fix the problems that come with that.

## The equals button

In [Tutorial 6](06_create.md#how-our-calculator-will-work) we planned to use `eval()` to work out the equation, but we didn't connect the `=` button. Let's do that now, with our usual three steps.

First, create the `equals_clicked` slot placeholder at the bottom of the slots section.

```python linenums="101" hl_lines="5-6" title="calculator.py"
--8<-- "examples/calculator/07_refine/step01/calculator.py:101:106"
```

??? note "Code explanation"
    - **line 105** → defines the `equals_clicked` slot.
    - **line 106** → a `pass` placeholder until we write the code.

Next, connect the `=` button's signal at the bottom of `signals`.

```python linenums="21" hl_lines="20" title="calculator.py"
--8<-- "examples/calculator/07_refine/step02/calculator.py:21:40"
```

??? note "Code explanation"
    - **line 40** → connects `pushButton_equal`'s `clicked` signal to `equals_clicked`.

Then replace the `pass` with the code that calculates the answer.

```python linenums="105" hl_lines="3-5" title="calculator.py"
--8<-- "examples/calculator/07_refine/step03/calculator.py:105:109"
```

??? note "Code explanation"
    - **line 107** → uses `eval()` to work out the equation string, and stores the answer in `result`.
    - **line 108** → turns the answer back into a string and makes it the new equation, so we can keep calculating with it.
    - **line 109** → shows the answer on the display.

!!! primm "PRIMM"
    1. **Predict** what the display will show after **5** **+** **2** **=**.
    2. **Run** ***calculator.py*** and try some simple calculations.
    3. **Investigate**: after an answer appears, what happens when you click a number? What about an operator?

It works for simple calculations, but it won't take long to find problems with our calculator. The rest of this tutorial is about finding and fixing them.

---

## After clicking equals

After we click `=`, the display shows the answer, which is good. The problem is the next button we click: its character is added to the end of the answer.

- If the next button is an operator (**+**, **-**, **x** or **/**), that's how a calculator should work. We're carrying on from the answer.
- If the next button is a number, a calculator would clear the answer and start a new calculation. Ours adds the number to the answer instead.

So our number buttons need to know whether the last button clicked was `=`. To remember that, we'll use a **flag variable**.

!!! tip "Flag variables"
    A **flag variable** is a Boolean that records whether something has happened. It's set to `True` when the event happens and back to `False` when it no longer applies. Flags are often used in loops, decisions and event handling to control what the program does next.

### Create the flag variable

Add the flag to the variables section of `__init__`.

```python linenums="15" hl_lines="3" title="calculator.py"
--8<-- "examples/calculator/07_refine/step04/calculator.py:15:20"
```

??? note "Code explanation"
    - **line 17** → creates the `equals_was_previous` flag, starting as `False` because no button has been clicked yet.

!!! tip "Naming flag variables"
    Name a flag as a statement, so its value reads naturally: `equals_was_previous = True` makes sense in a sentence.

### Set the flag

The flag must be `True` straight after `=` is clicked, and `False` after any other button. Start with `equals_clicked`.

```python linenums="107" hl_lines="2" title="calculator.py"
--8<-- "examples/calculator/07_refine/step05/calculator.py:107:111"
```

??? note "Code explanation"
    - **line 108** → sets the flag to `True`, because `=` was the last button clicked.

Now set it to `False` in `nine_clicked`.

```python linenums="47" hl_lines="2" title="calculator.py"
--8<-- "examples/calculator/07_refine/step06/calculator.py:47:51"
```

??? note "Code explanation"
    - **line 48** → sets the flag to `False`, because **9** is now the last button clicked.

Add the same line to the top of every other slot except `equals_clicked`.

??? tip "Check your code"
    ```python linenums="1" hl_lines="53 58 63 68 73 78 83 88 93 98 103 108 113 118" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step07/calculator.py"
    ```

### Use the flag

Now we can use the flag. For each **number** button and the **decimal** button:

1. check whether the last button was `=`
2. if it was, clear `self.equation` before adding the new character

Start with `nine_clicked`. These lines must go at the **top** of the method, before the flag is set back to `False`.

```python linenums="47" hl_lines="2-3" title="calculator.py"
--8<-- "examples/calculator/07_refine/step08/calculator.py:47:53"
```

??? note "Code explanation"
    - **line 48** → checks whether the last button clicked was `=`…
    - **line 49** → …and if so, clears the equation so a new calculation starts.

Make the same change to the other number slots and `decimal_clicked`, but not the operators, because they carry on from the answer.

??? tip "Check your code"
    ```python linenums="1" hl_lines="55-56 62-63 69-70 76-77 83-84 90-91 97-98 104-105 111-112 118-119" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step09/calculator.py"
    ```

!!! primm "PRIMM"
    1. **Predict** what the display will show after **5** **+** **2** **=** **3**, and after **5** **+** **2** **=** **+** **3** **=**.
    2. **Run** ***calculator.py*** and test both.
    3. **Investigate**: why must the `if` statement come **before** the line that sets the flag to `False`?

---

## Multiple operators

The next problem is that our calculator lets us click several operators in a row. Is that a problem?

### Plan with systematic testing

Let's test every pair of operators and record what happens. The table below summarises the results.

| Operators | Example | Result | Analysis | Verdict |
| --- | --- | --- | --- | --- |
| `++` | `5++2` | `7` | Works, because the second `+` means `+2`. But it's the same as `+`, so it isn't needed. | Prevent |
| `+-` | `5+-2` | `3` | Works, because `-` means `-2`. Allowing it makes it easier to enter negative numbers. | Allow |
| `+*` | `5+*2` | Error | `+*` is invalid syntax. | Prevent |
| `+/` | `5+/2` | Error | `+/` is invalid syntax. | Prevent |
| `-+` | `5-+2` | `3` | Works, but it's the same as `-`. | Prevent |
| `--` | `5--2` | `7` | Works, because the second `-` means `-2`. Allowing it makes negative numbers easier. | Allow |
| `-*` | `5-*2` | Error | `-*` is invalid syntax. | Prevent |
| `-/` | `5-/2` | Error | `-/` is invalid syntax. | Prevent |
| `*+` | `5*+2` | `10` | Works, but it's the same as `*`. | Prevent |
| `*-` | `5*-2` | `-10` | Correct, and there's no other way to enter this calculation. | Allow |
| `**` | `5**2` | `25` | Python's exponent operator (5 to the power of 2). Our calculator doesn't do powers. | Prevent |
| `*/` | `5*/2` | Error | `*/` is invalid syntax. | Prevent |
| `/+` | `5/+2` | `2.5` | Works, but it's the same as `/`. | Prevent |
| `/-` | `5/-2` | `-2.5` | Correct, and there's no other way to enter this calculation. | Allow |
| `/*` | `5/*2` | Error | `/*` is invalid syntax. | Prevent |
| `//` | `5//2` | `2` | Python's floor division operator (the whole-number part of `5/2`). Our calculator doesn't do floor division. | Prevent |

!!! tip "Systematic testing"
    The table tests every combination in order: all the pairs starting with `+`, then `-`, then `*`, then `/`. **Systematic testing** like this makes sure we test every path our program can take, which improves our **test coverage** and helps make our code reliable. The [Testing](https://damom73.github.io/digital-solutions-text-2025/testing) page of the Digital Solutions text shows how to document unit tests.

From the table, what should happen when an operator is clicked depends on two things: which button it is, and the last character in `self.equation`.

| Button | Last character in the equation | Action |
| --- | --- | --- |
| **+** | `+` `-` `*` or `/` | don't add `+` |
| **+** | `.` or a digit | add `+` |
| **-** | any character | add `-` |
| **x** | `+` `-` `*` or `/` | don't add `*` |
| **x** | `.` or a digit | add `*` |
| **/** | `+` `-` `*` or `/` | don't add `/` |
| **/** | `.` or a digit | add `/` |

That boils down to two rules:

1. for **-**, nothing changes
2. for **+**, **x** and **/**: only add the operator if the last character is a digit or `.`

### Code the rules

Start with `multiply_clicked`. Add the `if` statement and indent the line under it.

```python linenums="124" hl_lines="3-4" title="calculator.py"
--8<-- "examples/calculator/07_refine/step10/calculator.py:124:128"
```

??? note "Code explanation"
    - **line 126** → checks whether the last character of the equation is a digit or a decimal point…
    - **line 127** → …and only then adds `*`.

Line 126 uses two string tools:

- **Indexing**: a string is a sequence of characters, and each character has an **index**, just like the items in a list. Indexes can count backwards from the end, so `self.equation[-1]` is always the last character. We can also [slice strings](https://www.w3schools.com/python/python_strings_slicing.asp) the same way we slice lists.
- **String methods**: `.isdigit()` returns `True` if the string contains only digits (`0`–`9`). A `.` isn't a digit, so we also check for `self.equation[-1] == "."`.

Make the same change in `divide_clicked` and `add_clicked`.

??? tip "Check your code"
    ```python linenums="1" hl_lines="132-133 138-139" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step11/calculator.py"
    ```

!!! primm "PRIMM"
    1. **Predict** which operator pairs the calculator will now accept.
    2. **Run** ***calculator.py*** and use the summary table to test every pair.
    3. **Investigate**: what happens if you click **x** before any number?

---

## Operator first

Run the calculator and click **x** before any number. The app closes, and this appears in the terminal:

``` { .text .error linenums="1" }
Traceback (most recent call last):
  File "C:\Users\student\Documents\GitHub\PyQt6-Boiler-Plate\calculator.py", line 126, in multiply_clicked
    if self.equation[-1].isdigit() or self.equation[-1] == ".":
       ~~~~~~~~~~~~~^^^^
IndexError: string index out of range
```

- **line 1** → Python is about to show the steps that led to the crash.
- **line 2** → the error happened on line 126 of ***calculator.py***, inside `multiply_clicked`.
- **line 3** → the line of code that crashed.
- **line 4** → the `^` marks point to the exact part that caused the problem: `self.equation[-1]`.
- **line 5** → the type of error, `IndexError`, and what it means: we asked for a character that doesn't exist.

In fixing the last problem, we've created a new one. Let's work out why.

### Plan the fix

`IndexError: string index out of range` means `self.equation[-1]` doesn't exist. Looking back at `__init__`, `self.equation` starts as `""`. An empty string has no characters, so it has no last character.

So we only want to check the last character when the equation isn't empty.

### Code the fix

Add the new `if` statement to `multiply_clicked`, and indent the two lines under it.

```python linenums="124" hl_lines="3-5" title="calculator.py"
--8<-- "examples/calculator/07_refine/step12/calculator.py:124:129"
```

??? note "Code explanation"
    - **line 126** → only checks the last character if the equation isn't empty, which guards against the `IndexError`.
    - **lines 127–128** → are now inside the new `if` statement, so they only run when the equation has at least one character.

Make the same change in `divide_clicked` and `add_clicked`.

??? tip "Check your code"
    ```python linenums="1" hl_lines="133-135 140-142" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step13/calculator.py"
    ```

!!! primm "PRIMM"
    1. **Predict** what will happen now when you click **x** first.
    2. **Run** ***calculator.py*** and click **x**.
    3. **Investigate**: what happened to the `0` on the display?

## Prevent a blank display

Good news: no error. Bad news: the `0` on the display has disappeared.

That's because every slot calls `update_display`, which shows `self.equation`. Until now the equation always had something in it, but now we can click a button and leave `self.equation` as `""`. So `update_display` shows an empty string.

The fix is to only update the display when there's something to show.

```python linenums="157" hl_lines="2-3" title="calculator.py"
--8<-- "examples/calculator/07_refine/step14/calculator.py:157:159"
```

??? note "Code explanation"
    - **line 158** → only changes the display if the equation isn't empty…
    - **line 159** → …so the display keeps showing `0` until there's an equation to show.

---

## Double decimal

The next problem: we can click the decimal button twice in a row and get `..`, which a calculator shouldn't allow.

### Plan the fix

A number can only have one decimal point, but the equation can have several, as long as each number only has one (`1.5+2.5` is fine). So we need to know whether the **current** number already has a decimal point.

Each number in the equation ends when an operator is clicked. So we can use another flag:

- clicking the decimal button sets it to `True`
- clicking an operator (or `=`) sets it back to `False`
- the decimal button only adds `.` if the flag is `False`

### Code the fix

First, create the flag.

```python linenums="15" hl_lines="4" title="calculator.py"
--8<-- "examples/calculator/07_refine/step15/calculator.py:15:21"
```

??? note "Code explanation"
    - **line 18** → creates the `number_has_decimal` flag, starting as `False`.

Set the flag to `True` in `decimal_clicked`.

```python linenums="118" hl_lines="6" title="calculator.py"
--8<-- "examples/calculator/07_refine/step16/calculator.py:118:124"
```

??? note "Code explanation"
    - **line 123** → records that the current number now has a decimal point.

Now only add the decimal point if the current number doesn't have one. Add the `if` statement and indent the two lines under it.

```python linenums="118" hl_lines="5-7" title="calculator.py"
--8<-- "examples/calculator/07_refine/step17/calculator.py:118:125"
```

??? note "Code explanation"
    - **line 122** → checks that the current number doesn't already have a decimal point…
    - **lines 123–124** → …and only then adds `.` and sets the flag.

Finally, every operator starts a new number, so it needs to set the flag back to `False`. Start with `multiply_clicked`. The new line goes inside the inner `if` statement, so it only runs when the operator is actually added.

```python linenums="127" hl_lines="6" title="calculator.py"
--8<-- "examples/calculator/07_refine/step18/calculator.py:127:133"
```

??? note "Code explanation"
    - **line 132** → a new number starts after `*`, so it can have its own decimal point.

Add the same line to `divide_clicked` and `add_clicked` (inside the inner `if`), and to `subtract_clicked` and `equals_clicked`.

??? tip "Check your code"
    ```python linenums="1" hl_lines="140 148 154 161" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step19/calculator.py"
    ```

!!! primm "PRIMM"
    1. **Predict** what the display will show after **1** **.** **.** **5** **+** **.** **5**.
    2. **Run** ***calculator.py*** and test it.
    3. **Investigate**: what happens if you click **.** straight after `=`? Why?

---

## Leading zeros

In our calculator, **0** works like every other digit, but it shouldn't. We can enter numbers with **leading zeros** such as `09`, which isn't how numbers are written. Python agrees: `eval("5+08")` crashes with a `SyntaxError`, because Python doesn't allow leading zeros in whole numbers.

### Plan the fix

Let's work out when `0` should and shouldn't be allowed.

| Possible equation | Valid? | When we can detect it | How to detect it |
| --- | --- | --- | --- |
| `09` | No | when **0** is clicked | `self.equation` is `""` |
| `909` | Yes | when **0** is clicked | `self.equation[-1]` is a digit |
| `+0` | Yes | when **0** is clicked | `self.equation[-1]` is an operator |
| `+09` | No | when a digit is clicked | `self.equation[-1]` is `0` and `self.equation[-2]` is an operator |

That gives us two rules:

1. when **0** is clicked: don't add it if the equation is empty
2. when **1**–**9** is clicked: if the last character is `0` and the one before it is an operator, remove the `0` first

### Code the fix

The first rule goes in `zero_clicked`. Add the `if` statement and indent the line under it.

```python linenums="111" hl_lines="5-6" title="calculator.py"
--8<-- "examples/calculator/07_refine/step20/calculator.py:111:117"
```

??? note "Code explanation"
    - **line 115** → only adds a `0` if the equation isn't empty…
    - **line 116** → …so a number can't start with `0`.

The second rule goes in `nine_clicked`, just before the `9` is added.

```python linenums="48" hl_lines="5-7" title="calculator.py"
--8<-- "examples/calculator/07_refine/step21/calculator.py:48:56"
```

??? note "Code explanation"
    - **line 52** → checks the equation isn't empty, so the indexes on the next line exist.
    - **line 53** → checks whether the last character is `0` and the character before it is one of the four operators, which means the current number is just `0`…
    - **line 54** → …and if so, uses string slicing to remove the last character. `self.equation[:-1]` means "everything except the last character".

Make the same change in the slots for **1** to **8**.

??? tip "Check your code"
    ```python linenums="1" hl_lines="62-64 72-74 82-84 92-94 102-104 112-114 122-124 132-134" title="calculator.py"
    --8<-- "examples/calculator/07_refine/step22/calculator.py"
    ```

!!! primm "PRIMM"
    1. **Predict** what the display will show after **5** **+** **0** **8**, and after **5** **+** **0** **.** **8**.
    2. **Run** ***calculator.py*** and test both.
    3. **Investigate**: why does `0.8` still work?

---

## Divide by zero

Other calculators show an error message when we divide by zero. Ours crashes.

### Plan the fix

Dividing by zero is mathematically impossible, so Python raises a `ZeroDivisionError` **exception**. We can catch that exception with a `try`...`except` block.

!!! tip "Try and except"
    A **try block** holds code that might raise an exception. If it does, Python jumps to the matching `except` block instead of crashing, so the program can carry on. W3Schools has a good [Python Try Except tutorial](https://www.w3schools.com/python/python_try_except.asp).

We'll put `eval()` inside a `try` block. If it raises a `ZeroDivisionError`, we'll set `result` to a message, so the message appears on the display.

### Code the fix

Replace the `eval()` line in `equals_clicked` with the highlighted `try`...`except` block.

```python linenums="185" hl_lines="3-6" title="calculator.py"
--8<-- "examples/calculator/07_refine/step23/calculator.py:185:193"
```

??? note "Code explanation"
    - **line 187** → starts a `try` block, so Python watches the next line for errors.
    - **line 188** → works out the equation, just like before.
    - **line 189** → if `eval()` raised a `ZeroDivisionError`…
    - **line 190** → …stores a message in `result` instead of crashing.

That creates a new problem: after dividing by zero, `self.equation` is now words, and our calculator can't calculate with words. So once the message is on the display, we need to reset the equation.

```python linenums="185" hl_lines="10-11" title="calculator.py"
--8<-- "examples/calculator/07_refine/step24/calculator.py:185:195"
```

??? note "Code explanation"
    - **line 194** → checks whether the result was the error message…
    - **line 195** → …and if so, clears the equation, so the next button starts a new calculation.

!!! primm "PRIMM"
    1. **Predict** what will happen after **5** **/** **0** **=**, then **2** **+** **3** **=**.
    2. **Run** ***calculator.py*** and test it.
    3. **Investigate**: what happens if you click `=` before entering anything? Keep that result in mind for Exercise 1.

## Test the calculator

Here are some tests from this tutorial, recorded in the format the Digital Solutions [Testing](https://damom73.github.io/digital-solutions-text-2025/testing) page uses. Run each one and fill in the **Actual outcome** and **Pass/Fail** columns for our calculator.

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | `5 + 2 =` | `7` | | | |
| 2 | `5 + 2 = 3` | `3` | | | |
| 3 | `5 + + 2 =` | `7` (second `+` ignored) | | | |
| 4 | `5 * - 2 =` | `-10` | | | |
| 5 | `x` first | display stays `0`, no crash | | | |
| 6 | `1 . . 5` | `1.5` | | | |
| 7 | `5 + 0 8 =` | `13` | | | |
| 8 | `5 / 0 =` | `Cannot divide by zero` | | | |
| 9 | `=` first | ? | | | |

## Commit and push

1. In GitHub Desktop, type **Refined calculator** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-7-refine-calculator-app) page.

### Exercise 1

Test case 9 shows another bug: clicking `=` before entering anything (or straight after an operator, such as `5 + =`) closes the app with a `SyntaxError`. Can you stop it crashing? It should:

- show `Error` on the display instead
- let the next button start a new calculation

### Exercise 2

Our ten number slots are almost identical, which breaks the DRY (Don't Repeat Yourself) principle. Can you replace their code with one method, `number_clicked(self, digit)`, that each number slot calls (for example `self.number_clicked("9")`)? The calculator should behave exactly the same, so run all the tests in the table again afterwards.
