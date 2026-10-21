import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTime, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("time_machine.ui", self)

        # --- initialise variables
        self.clock_timer = QTimer()
        self.clock_timer.start(1000)

        self.sw_timer = QTimer()
        self.sw_time = QTime(0, 0, 0, 0)
        self.sw_running = False

        # --- connect signals to slots
        self.signals()

        # --- initialise displays
        self.show_time()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        # clock
        self.clock_timer.timeout.connect(self.show_time)

    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    # clock
    def show_time(self):
        """
        Update the clock display with the current time.
        """
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("h:mm:ssa")
        self.label_clock.setText(formatted_time)

    # stopwatch
    def show_sw_time(self):
        """
        Update the stopwatch display with the current stopwatch time.
        """
        formatted_time = self.sw_time.toString("h:mm:ss:zz")
        self.label_stopwatch.setText(formatted_time)

    def start_sw(self):
        """
        Start the stopwatch.
        """
        self.sw_timer.start(100)
        self.sw_running = True

    def pause_sw(self):
        """
        Pause the stopwatch, or start it again if it is paused.
        """
        self.sw_running = not self.sw_running


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
