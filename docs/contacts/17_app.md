# Tutorial 17 - Contact App

!!! learn "In this tutorial we will learn"
    - how to read a CSV file into a table widget, and write a table back to a CSV file
    - how exception handling stops file errors from crashing our app
    - how to load a custom dialog's UI into its own class
    - how to open a second window and pass information back to the main window

!!! terms "Terminology"
    - **exception handling** – dealing with errors while a program runs, so it can carry on or show a helpful message instead of crashing.
    - **header row** – the first row of a CSV file, which names the columns instead of holding data.
    - **modal dialog** – a dialog that must be closed before the user can go back to the main window.

## Set up contacts.py

1. Copy ***loadui_boilerplate.py*** and rename the copy ***contacts.py***.
2. Change the ***.ui*** file on line 12 to ***contacts.ui***.

```python linenums="1" hl_lines="12" title="contacts.py"
--8<-- "examples/contacts/17_app/step01/contacts.py"
```

??? note "Code explanation"
    - **line 12** → loads ***contacts.ui***, the main window we designed in [Tutorial 16](16_ui.md).

3. Run ***contacts.py*** to check the window loads.

## Load contacts from a file

### Get the contacts file

The first feature is loading contacts from a CSV file, so we need one.

1. Download [contacts.csv](../downloads/contacts.csv) and save it in your repo, next to ***contacts.py***.
2. Open it in VS Code. It has a **header row** (`First Name,Last Name,Phone Number`) and then one contact on each line.

### Choose the file

The `open_contacts` slot starts by asking the user which file to open. Add `QFileDialog` to the imports.

```python linenums="1" hl_lines="3" title="contacts.py"
--8<-- "examples/contacts/17_app/step02/contacts.py:1:5"
```

??? note "Code explanation"
    - **line 3** → adds `QFileDialog`, which we used in [Tutorial 15](../to_do/15_advanced.md#save-a-list).

Then create the slot under the slots string.

```python linenums="25" hl_lines="5-15" title="contacts.py"
--8<-- "examples/contacts/17_app/step03/contacts.py:25:40"
```

??? note "Code explanation"
    - **line 29** → defines the `open_contacts` slot.
    - **lines 30–32** → a docstring that explains what the slot does.
    - **lines 34–39** → open a file dialog that only shows CSV files, and store the chosen file's path. The arguments are spread over several lines to keep them readable.

### Read the file

Next we read the CSV file. Opening a file can go wrong, so we need to handle errors to stop our app crashing. There are two likely problems:

- the user didn't choose a file (they clicked **Cancel**)
- the file can't be opened or read

!!! tip "Exception handling"
    **Exception handling** is how a program deals with errors that happen while it runs. Without it, something like opening a missing file stops the program. With it, the program catches the error and responds, for example by showing the user a helpful message. The [Good programming practice](https://damom73.github.io/digital-solutions-text-2025/good-practice) page of the Digital Solutions text has more about writing robust code.

We'll use the `csv` library to read the file and `QMessageBox` to show an error message. Add them to the imports.

```python linenums="1" hl_lines="2 4" title="contacts.py"
--8<-- "examples/contacts/17_app/step04/contacts.py:1:5"
```

??? note "Code explanation"
    - **line 2** → imports Python's `csv` library, which reads and writes CSV files.
    - **line 4** → adds `QMessageBox`, Qt's ready-made message dialog.

Now add the code below to the bottom of `open_contacts`.

```python linenums="34" hl_lines="9-22" title="contacts.py"
--8<-- "examples/contacts/17_app/step05/contacts.py:34:56"
```

??? note "Code explanation"
    - **line 43** → only tries to read a file if one was chosen.
    - **line 44** → starts a `try` block, so any error in the next lines is caught.
    - **line 45** → opens the file for reading. `newline=""` lets the `csv` library handle line endings itself.
    - **line 46** → creates a CSV reader, which splits each line into a list of values.
    - **line 47** → skips the header row. `next` reads one row and we don't keep it; `None` stops an error if the file is empty.
    - **line 48** → reads the rest of the rows into `data`, a list of contacts where each contact is a list of three values.
    - **line 49** → if anything in the `try` block raised an exception…
    - **lines 50–55** → …shows an error message box with the title **Error**, the message **Could not open file.** and an **OK** button.

### Show the contacts

Now we need to put the contacts in `data` into `tableWidget_contacts`. To do that we need `QTableWidgetItem`, because every cell in a table widget holds one. Our `QtWidgets` import is getting long, so let's spread it over several lines.

```python linenums="1" hl_lines="4-10" title="contacts.py"
--8<-- "examples/contacts/17_app/step06/contacts.py:1:12"
```

??? note "Code explanation"
    - **lines 4–10** → import the same widgets as before plus `QTableWidgetItem`, one per line inside round brackets, so the import is easy to read and change.

The table also needs headings for its columns. We'll store them in a list in `__init__`.

```python linenums="14" hl_lines="9" title="contacts.py"
--8<-- "examples/contacts/17_app/step07/contacts.py:14:26"
```

??? note "Code explanation"
    - **line 22** → creates the list of column headings. Keeping them in one variable means we only have to change them in one place.

Now add the code that fills the table, inside the `try` block after the file is read.

```python linenums="50" hl_lines="8-11 13-21" title="contacts.py"
--8<-- "examples/contacts/17_app/step08/contacts.py:50:71"
```

??? note "Code explanation"
    - **line 58** → sets the table's number of rows to the number of contacts.
    - **line 59** → sets the number of columns to the number of headings.
    - **line 60** → shows our headings at the top of the columns.
    - **line 63** → loops through the contacts. `enumerate` gives us each contact's row number as well as the contact itself…
    - **line 64** → …then loops through that contact's values, with their column numbers.
    - **lines 65–69** → put each value in its cell, wrapped in a `QTableWidgetItem`.
    - **line 70** → widens each column to fit its longest value.

### Connect the signal

Replace the `pass` in `signals` with the connection for the **Open** menu item.

```python linenums="27" hl_lines="5" title="contacts.py"
--8<-- "examples/contacts/17_app/step09/contacts.py:27:32"
```

??? note "Code explanation"
    - **line 31** → connects the **Open** action's `triggered` signal to `open_contacts`.

!!! primm "PRIMM"
    1. **Predict** how many rows the table will have after you open ***contacts.csv***.
    2. **Run** ***contacts.py***, choose **File** → **Open** and open ***contacts.csv***.
    3. **Investigate**: delete line 47, run it again and open the file. What changes, and why? (Put the line back afterwards.)

There should be 10 contacts in the table.

---

## New contact dialog

Now we'll use ***new_contact.ui*** to add new contacts. The main window is a `QMainWindow`, but our dialog is a `QDialog`, so it needs its own class.

### Create the NewContact class

Add `QDialog` to the imports.

```python linenums="1" hl_lines="9-10" title="contacts.py"
--8<-- "examples/contacts/17_app/step10/contacts.py:1:13"
```

??? note "Code explanation"
    - **line 9** → now ends with a comma, because `QTableWidgetItem` is no longer the last item.
    - **line 10** → adds `QDialog`, the class every Qt dialog is built on.

Now add the `NewContact` class between the imports and `MainWindow`.

```python linenums="9" hl_lines="6-12" title="contacts.py"
--8<-- "examples/contacts/17_app/step11/contacts.py:9:24"
```

??? note "Code explanation"
    - **line 14** → defines `NewContact` as a subclass of `QDialog`.
    - **line 15** → defines `__init__`. The `parent` parameter is the window that opens the dialog, and it defaults to `None` (no parent).
    - **lines 16–18** → a docstring that explains what `__init__` does.
    - **line 19** → runs `QDialog`'s own `__init__`, passing on the parent so the dialog appears over the main window.
    - **line 20** → loads ***new_contact.ui*** into the dialog, just like we load the main window's UI.

### Get the details

When **OK** is clicked, the main window needs the details the user typed. We'll give `NewContact` a method that returns them as a dictionary.

```python linenums="14" hl_lines="9-17" title="contacts.py"
--8<-- "examples/contacts/17_app/step12/contacts.py:14:31"
```

??? note "Code explanation"
    - **line 22** → defines the `get_details` method.
    - **lines 23–25** → a docstring that explains what the method does.
    - **lines 26–30** → return a dictionary with the text from each of the dialog's three line edits.

### Open the dialog

Back in `MainWindow`, add a slot that opens the dialog, at the bottom of the slots section.

```python linenums="94" hl_lines="6-13" title="contacts.py"
--8<-- "examples/contacts/17_app/step13/contacts.py:94:107"
```

??? note "Code explanation"
    - **line 99** → defines the `open_contact_dialog` slot.
    - **lines 100–102** → a docstring that explains what the slot does.
    - **line 103** → creates a `NewContact` dialog, with our main window as its parent.
    - **line 104** → shows the dialog and waits until it's closed. `exec` returns a value that counts as `True` if **OK** was clicked and `False` if **Cancel** was clicked…
    - **line 105** → …so only if **OK** was clicked, gets the details from the dialog.
    - **line 106** → prints the details to the terminal, just for testing. We'll replace it soon.

!!! tip "Modal dialogs"
    `exec` opens the dialog as a **modal dialog**: the user has to close it before they can use the main window again. That's why our code can simply wait at line 104 and then read the details.

Connect the **Add** button to the slot.

```python linenums="47" hl_lines="6" title="contacts.py"
--8<-- "examples/contacts/17_app/step14/contacts.py:47:53"
```

??? note "Code explanation"
    - **line 52** → connects the **Add** button's `clicked` signal to `open_contact_dialog`.

!!! primm "PRIMM"
    1. **Predict** what will appear in the terminal after you click **Add**, type some details and click **OK**. What about **Cancel**?
    2. **Run** ***contacts.py*** and test both.
    3. **Investigate**: what type of value is printed? Which method made it?

### Show the new contact

Now we'll put the new contact's details in the table. This method isn't a slot, so it goes in a new utilities section at the bottom of the class.

```python linenums="104" hl_lines="6-14 16-22" title="contacts.py"
--8<-- "examples/contacts/17_app/step15/contacts.py:104:126"
```

??? note "Code explanation"
    - **line 110** → defines the `add_contact` utility method, which takes the dictionary of details.
    - **lines 111–113** → a docstring that explains what the method does.
    - **line 115** → if the table is empty (no file has been opened yet)…
    - **lines 116–117** → …sets up its columns and headings.
    - **line 120** → the new row's number is the current number of rows, because rows count from `0`.
    - **line 121** → inserts a new, empty row at the bottom of the table.
    - **lines 122–124** → put the first name, last name and phone number in the new row's three cells.
    - **line 125** → resizes the columns to fit.

Now replace the `print` in `open_contact_dialog` with a call to `add_contact`.

```python linenums="99" hl_lines="9" title="contacts.py"
--8<-- "examples/contacts/17_app/step16/contacts.py:99:107"
```

??? note "Code explanation"
    - **line 107** → passes the details to `add_contact`, so the new contact appears in the table.

!!! primm "PRIMM"
    1. **Predict** where the new contact will appear in the table.
    2. **Run** ***contacts.py***, open ***contacts.csv*** and add a contact.
    3. **Investigate**: what happens if you add a contact before opening a file?

---

## Save contacts

The last feature is saving. We'll use `QFileDialog` to get the file name, then write the table to the file in CSV format, with the same error handling we used for reading.

Add the `save_contacts` slot after `open_contact_dialog`.

```python linenums="104" hl_lines="6-16" title="contacts.py"
--8<-- "examples/contacts/17_app/step17/contacts.py:104:120"
```

??? note "Code explanation"
    - **line 109** → defines the `save_contacts` slot.
    - **lines 110–112** → a docstring that explains what the slot does.
    - **lines 114–119** → open a save dialog that only shows CSV files, and store the chosen path.

Now add the code that writes the file.

```python linenums="114" hl_lines="8-26" title="contacts.py"
--8<-- "examples/contacts/17_app/step18/contacts.py:114:140"
```

??? note "Code explanation"
    - **line 122** → only saves if a file was chosen.
    - **line 123** → starts a `try` block, so errors are caught.
    - **line 124** → opens the file for writing.
    - **line 125** → creates a CSV writer, which turns lists of values into lines of the file.
    - **line 126** → writes the header row first, so our saved files look the same as ***contacts.csv*** and open correctly next time.
    - **line 127** → loops through every row in the table…
    - **line 128** → …starting an empty list for that row's values…
    - **line 129** → …then loops through every column…
    - **line 130** → …getting the cell's item.
    - **line 131** → adds the item's text to the row, or an empty string if the cell is empty (an empty cell has no item, so calling `item.text()` would crash).
    - **line 132** → writes the row to the file.
    - **line 133** → if anything went wrong…
    - **lines 134–139** → …shows an error message instead of crashing.

Finally, connect the **Save** menu item.

```python linenums="47" hl_lines="7" title="contacts.py"
--8<-- "examples/contacts/17_app/step19/contacts.py:47:54"
```

??? note "Code explanation"
    - **line 53** → connects the **Save** action's `triggered` signal to `save_contacts`.

## Test the Contacts app

| Test case | Input | Expected outcome | Actual outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | **Open** ***contacts.csv*** | 10 contacts, with our headings | | | |
| 2 | **Open**, then **Cancel** | no change, no error | | | |
| 3 | **Add**, type details, **OK** | new contact in the last row | | | |
| 4 | **Add**, then **Cancel** | no new row | | | |
| 5 | **Add** before opening a file | table gets headings and the new contact | | | |
| 6 | **Save**, close the app, run it again, **Open** the saved file | every contact is back, including the new one | | | |

## Commit and push

1. In GitHub Desktop, type **Finished Contacts app** in the **Summary** box.
2. Click **Commit to main**, then **Push origin**.

We've now built four apps, and learnt the workflow and Qt features we need to design and build our own GUI apps.

## Exercises

!!! primm "PRIMM"
    Time to **modify** the code and see what happens.

Solutions are on the [Exercise Solutions](../reference/solutions.md#tutorial-17-contact-app) page.

### Exercise 1

Can you add a **Delete** button that removes the selected contact from the table? It should:

- be a new push button beside **Add** in ***contacts.ui***, with the objectName `pushButton_delete`
- remove the row of the selected cell (look up `currentRow` and `removeRow` in the [QTableWidget documentation](https://doc.qt.io/qt-6/qtablewidget.html))
- do nothing if no contact is selected
