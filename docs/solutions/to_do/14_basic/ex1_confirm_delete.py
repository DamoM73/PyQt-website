import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("to_do_list.ui", self)

        # --- initialise variables

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.pushButton_add.clicked.connect(self.add_task)
        self.listWidget_items.itemClicked.connect(self.delete_item)

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def add_task(self):
        """
        Add a new task to the list.
        """
        new_task, ok = QInputDialog.getText(self,
                                            "Add Task",
                                            "Enter a new task:")
        if ok and new_task:
            self.listWidget_items.addItem(new_task)

    def delete_item(self, item):
        """
        Delete the clicked item from the list.
        """
        answer = QMessageBox.question(self,
                                      "Delete task",
                                      "Delete this task?")
        if answer == QMessageBox.StandardButton.Yes:
            row = self.listWidget_items.row(item)
            self.listWidget_items.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
