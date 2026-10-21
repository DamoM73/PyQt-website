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
        self.equals_was_previous = False
        self.number_has_decimal = False

        # --- connect signals to slots
        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.ui.pushButton_9.clicked.connect(self.nine_clicked)
        self.ui.pushButton_8.clicked.connect(self.eight_clicked)
        self.ui.pushButton_7.clicked.connect(self.seven_clicked)
        self.ui.pushButton_6.clicked.connect(self.six_clicked)
        self.ui.pushButton_5.clicked.connect(self.five_clicked)
        self.ui.pushButton_4.clicked.connect(self.four_clicked)
        self.ui.pushButton_3.clicked.connect(self.three_clicked)
        self.ui.pushButton_2.clicked.connect(self.two_clicked)
        self.ui.pushButton_1.clicked.connect(self.one_clicked)
        self.ui.pushButton_0.clicked.connect(self.zero_clicked)
        self.ui.pushButton_decimal.clicked.connect(self.decimal_clicked)
        self.ui.pushButton_multiply.clicked.connect(self.multiply_clicked)
        self.ui.pushButton_divide.clicked.connect(self.divide_clicked)
        self.ui.pushButton_add.clicked.connect(self.add_clicked)
        self.ui.pushButton_subtract.clicked.connect(self.subtract_clicked)
        self.ui.pushButton_equal.clicked.connect(self.equals_clicked)

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    def nine_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "9"
        self.update_display()

    def eight_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "8"
        self.update_display()

    def seven_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "7"
        self.update_display()

    def six_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "6"
        self.update_display()

    def five_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "5"
        self.update_display()

    def four_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "4"
        self.update_display()

    def three_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "3"
        self.update_display()

    def two_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "2"
        self.update_display()

    def one_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "1"
        self.update_display()

    def zero_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "0"
        self.update_display()

    def decimal_clicked(self):
        if self.equals_was_previous:
            self.equation = ""
        self.equals_was_previous = False
        self.equation += "."
        self.number_has_decimal = True
        self.update_display()

    def multiply_clicked(self):
        self.equals_was_previous = False
        if self.equation != "":
            if self.equation[-1].isdigit() or self.equation[-1] == ".":
                self.equation += "*"
        self.update_display()

    def divide_clicked(self):
        self.equals_was_previous = False
        if self.equation != "":
            if self.equation[-1].isdigit() or self.equation[-1] == ".":
                self.equation += "/"
        self.update_display()

    def add_clicked(self):
        self.equals_was_previous = False
        if self.equation != "":
            if self.equation[-1].isdigit() or self.equation[-1] == ".":
                self.equation += "+"
        self.update_display()

    def subtract_clicked(self):
        self.equals_was_previous = False
        self.equation += "-"
        self.update_display()

    def equals_clicked(self):
        self.equals_was_previous = True
        result = eval(self.equation)
        self.equation = str(result)
        self.update_display()

    # ---- OTHER FUNCTIONS ---- #
    def update_display(self):
        if self.equation != "":
            self.ui.label_display.setText(self.equation)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
