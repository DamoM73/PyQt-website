# Tutorial 17 - Contact App

```{admonition} In this tutorial, you will:
TBA
```

## New file

First, we need to setup your new file:

1. Copy your new **main_window.py** file, calling it **contacts.py**.
2. Change the file name to **contacts.ui**

 ![new file](./assets/img/19/01_new_file.png)

3. Run the code to ensure the window loads.

## Loading Contacts File

### Download Contacts File

The first feature that we will add to our app is loading contacts from a **csv** file. To do this we will need a csv file with contact details.

1. **Right mouse click** on this **[contacts csv file](./assets/img/19/contacts.csv)** 
2. Click on **save link as** and then choose the same folder as your **contacts.py** file.

### Get Contacts File Name

Next we will need to make a slot that opens **Qt's File Dialogue Box** and gets the name of the contact file.

1. Add the **QFileDialog** to the **import** statements

![File dialog](./assets/img/19/02_import_QFileDialogue.png)

2. In the Slots section create the **open_contacts** slot which opens the **QFileDialog** and retrieves the name and path of the selected file.

![Open contact file](./assets/img/19/03_open_contacts.png)

### Read Contacts File

We are now going to read the csv file into the **tableWidget_contacts** in our UI, but we need to handle possible errors, to prevent our program from crashing.

```{admonition} Exception handling
:class: hint
Exception handling is a way for a program to deal with errors that happen while it is running. When something goes wrong, like trying to divide by zero or opening a file that doesn't exist, the program can stop working unless the error is handled.

With exception handling, the program checks for these errors and responds to them without stopping completely. This keeps the program running or allows it to show a helpful message to the user instead of crashing.
```

First we need to import two new modules:

- **csv** &rarr; reading csv files
- **QMessageBox** &rarr; displaying error messages

1. Add the libraires below into your import section

![import csv](./assets/img/19/04_import_csv.png)

Now we need to open and read the csv file. There are two likely errors we need to handle:

- The user did not select a file (ie. they clicked **Cancel** on the dialogue box)
- The csv file cannot be opened.

2. Add the code below to the bottom of the **open_contacts** slot.

![read csv file](./assets/img/19/05_read_csv.png)

Lets look at how this code handles those possible errors.

- **`if file_path:`** &rarr; will only let the program attempt to open a file when a file name has been returned from the file dialog box.
- **`try:`** block &rarr; attempts to open the provided file as a csv and read the contents into the **data** list.
- **`except Exception:`** block &rarr; if the `try:` fails, then a dialog box will pop up with an error message.

### Display Contact Details

Now we need to take the contacts details in the **data** list and write it to **tableWidget_contacts**. Again we need to handle possible errors, in this case where the csv file is empty.

1. We need to import the **QTableWidgetItem** module (the **QtWidgets** import is getting a bit long, so let's spread it over multiple lines).

![Import widgets](./assets/img/19/06_import_widgets.png)

We also need to create headings for our contacts table. We will use a list to store this information.

2. In the `__init__` add the following line.

![headers](./assets/img/19/07_headers.png)

Now we can finally read the contact details from the data list

3. Add the code below into the **try block** in the **open_contact** slot

![display](./assets/img/19/08_read_csv.png)


### Connect Signal to Slot

Next we will connect the signal to our completed **open_contact** slot.

1. In the **signals** method add the code below.

![open signal](./assets/img/19/09_open_signal.png)

### Test File Open

Now run your app and check the you can open the **contacts.csv** and that is displays 10 contacts.

## New Contact Dialog

Now we need to add new contacts using the **new_contact.ui** we created. To access the **new_contact.ui** we need to create a **NewContact** class. 

### Create NewContact class

This new class is not a QDialog, not a QMainWindow, so we need to import that widget.

1. Change your import section

![dialog import](./assets/img/19/10_dialog_import.png)

Now to create the **NewContact** class

2. After the import section add the new class definition

![NewContact_class](./assets/img/19/11_newcontact_class.png)

### Code Ok Button

We need a method that will read the values entered and return them to the **MainWindow**. This method needs to be placed in the **NewContact** class.

3. Under the **NewClass** `__init__` add.

![get_details](./assets/img/19/13_get_details_method.png)

Now we need to make a slot that will launch the new contact dialog

4. At the bottom of the slots section add

![open dialog](./assets/img/19/12_open_dialog.png)

Lets look at some of that code:

- `if dialog.exec():` &rarr; this code block will be executed when the dialog's **Ok** button is clicked.
- `details = dialog.get_details()` &rarr; run the `get_details` method and save the returned values in the `details` variable.
- `print(details)` &rarr; this is only for testing, we will change it later.


Finally, link the **pushButton_add** signal to this slot.

5. In the **signals** method add

![dialog signal](./assets/img/19/14_dialog_signal.png)

### Test Ok Button

Now lets test what we have done.

1. Run your app
2. Click the **Add** button
3. Enter values into the new contact dialog
4. Click **Ok**
5. Check that the values you entered are printed in your terminal.

### Display New Contact

Finally we need to add the new contact details to our **tableWidget_contacts**.

First we will create a method that will take the values in **details** and write them to **tableWidget_contact**. This isn't a slot, so we will create a new utilities section to place this method.

1. At the bottom of the **slots** section add this code:

![add contact](./assets/img/19/15_add_contact.png)

Then we need to execute this method when the Dialog Ok button is pressed.

2. In the **open_contact_dialog** replace the **print** statement with the following code.

![call add contact](./assets/img/19/15_call_add_contact.png)

### Test New Contact

Run your app and add a new contact. Did the information appear correctly in your contact list?

## Saving Contacts

Now for the final step, saving our contact list. We will use the **QFileDialog** to get the path for the save file. Then write the contents of the **tableWidget_contacts** to the file in csv format.

### Getting Save File Path

Use the **QFileDialog** to get the save file path.

1. At the bottom of the **Slots** section add the following code

![save contacts](./assets/img/19/16_save_contacts.png)

### Save Contact to File

Now we need to write the content of the **tableWidget_content** to a csv file. We need to make sure that we have the same error handling as we did for reading a csv file.

2. Complete the **save_content** method with the code below

![save file](./assets/img/19/17_save_file.png)

### Connect Save Signal

Finally we need to connect the **actionSave** signal to our **save_content** slot.

1. In the **signals** method, add the following code.

![connect save signal](./assets/img/19/18_connect_save_signal.png)

### Testing Save

Now to test the save function of your app.

1. Launch your app
2. Open the contacts file
3. Add a new contact
4. Save your contact file
5. Close the app
6. Launch the app again
7. Open the contact file
8. Check that your new contact is in the file.
