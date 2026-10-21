import sys
import csv
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem
)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("contacts.ui", self)

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
