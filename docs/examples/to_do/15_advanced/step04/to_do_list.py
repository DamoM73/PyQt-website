import sys
import json
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog


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
        self.actionSave.triggered.connect(self.save_list)

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
        row = self.listWidget_items.row(item)
        self.listWidget_items.takeItem(row)

    def save_list(self):
        """
        Save the current list and list name to a JSON file.
        """
        # get the list name from the line edit
        list_name = self.lineEdit_list_name.text()

        # get all the tasks from the list widget
        tasks = []
        for index in range(self.listWidget_items.count()):
            task = self.listWidget_items.item(index).text()
            tasks.append(task)

        # put the list name and tasks in a dictionary
        data = {
            "list_name": list_name,
            "tasks": tasks
        }

        # suggest a file name and open a save dialog
        if list_name:
            suggested_file_name = f"{list_name}.json"
        else:
            suggested_file_name = "to_do_list.json"
        file_path, _ = QFileDialog.getSaveFileName(self,
                                                   "Save To-Do List",
                                                   suggested_file_name,
                                                   "JSON Files (*.json)")

        # save the dictionary if a file was chosen
        if file_path:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
