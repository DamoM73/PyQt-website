import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_calculator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- initialise variables
        self.equation = ""

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.ui.pushButton_9.clicked.connect(self.nine_clicked)

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def nine_clicked(self):
        self.equation += "9"

    # ---- OTHER FUNCTIONS ---- #
    def update_display(self):
        self.ui.label_display.setText(self.equation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
