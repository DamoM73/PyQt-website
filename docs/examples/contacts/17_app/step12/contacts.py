import sys
import csv
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
    QDialog
)


class NewContact(QDialog):
    def __init__(self, parent=None):
        """
        Load the new contact dialog's UI.
        """
        super().__init__(parent)
        uic.loadUi("new_contact.ui", self)

    def get_details(self):
        """
        Return the details typed into the dialog as a dictionary.
        """
        return {
            "first_name": self.lineEdit_first_name.text(),
            "last_name": self.lineEdit_last_name.text(),
            "phone_number": self.lineEdit_phone_number.text()
        }


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("contacts.ui", self)

        # --- initialise variables
        self.headers = ["First Name", "Last Name", "Phone Number"]

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.actionOpen.triggered.connect(self.open_contacts)

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def open_contacts(self):
        """
        Load contacts from a CSV file into the table.
        """
        # get the file name from an open dialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "CSV Files (*.csv)"
        )

        # read the file if one was chosen
        if file_path:
            try:
                with open(file_path, mode="r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader, None)
                    data = list(reader)

                # set up the table
                self.tableWidget_contacts.setRowCount(len(data))
                self.tableWidget_contacts.setColumnCount(len(self.headers))
                self.tableWidget_contacts.setHorizontalHeaderLabels(self.headers)

                # put each contact in the table
                for row, record in enumerate(data):
                    for col, field in enumerate(record):
                        self.tableWidget_contacts.setItem(
                            row,
                            col,
                            QTableWidgetItem(field)
                        )
                self.tableWidget_contacts.resizeColumnsToContents()
            except Exception:
                QMessageBox.critical(
                    self,
                    "Error",
                    "Could not open file.",
                    QMessageBox.StandardButton.Ok,
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
