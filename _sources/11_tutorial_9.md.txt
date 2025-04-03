# Tutorial 9 - Using loadUi

```{admonition} In this tutorial you will:
- Learn how to load a `.ui` file using the `loadUi` method
- Create a new boilerplate file which uses `loadUi`
```

## New Boilerplate

In this tutorial, we will look at a new way to incorporate the UI file. This new method involves your Python file directly loading the UI file, rather than having to convert it.

### Loading UI

To use this new system, you will create a new boilerplate file. To start this, create a new file and then add the following code:

![starting boilerplate](./assets/img/11/start_new_boilerplate.png)

You will notice that the big difference is on **line 11**. This is where the code loads dynamically loads the QT Designer file, as long as it is in the same directory. 

Run your code to check that it works.

### Completing Boilerplate

Now that we are loading the `.ui` file we need to add in the rest of our usual boiler plate structure. Go ahead and add our **signals** and **slots** system with the code below.

![boilerplate complete](./assets/img/11/new_boilerplate.png)

## Finished Code

You finished code should be the same as below. Save it as your new boilerplate code.

```{code-block} python
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("time_machine.ui", self)

        # --- initialise variables

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        pass  # Add signal-slot connections here

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

Just remember to change the name of the `.ui` file for other projects.