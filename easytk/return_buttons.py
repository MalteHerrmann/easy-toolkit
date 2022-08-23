"""
This module contains the different return button objects,
that are used to close the easytk GUI and return the
respective values to the user.

These widgets are not directly usable and are inserted into
the easytk window automatically, depending on the chosen
window type.
"""
# ------------------------------
# Imports
#
import tkinter as tk
from easytk.widgets import EasyWidget


# ------------------------------
# Classes
#
class EasySelectionButton(EasyWidget):
    """
    Class to define a frame containing a button, that triggers
    the GUI to return the values from all widgets, that contain
    a returnable value.
    """

    def __init__(
            self,
            main_window,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...
    ):
        """
        Creates a new EasySelectionButton object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, "center", "center")

        # Widget frame
        self.grid_object = tk.Frame(self.frame)

        # Button
        self.object = tk.Button(
            self.grid_object,
            text=main_window.selection_text,
            command=main_window.get_return_values
        )

        # Arrange widgets
        self.object.pack()

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Add to grid
        self.insert_into_grid(self.frame, row, column, column_span, check_return_buttons=False)


# ------------------------------
# Execution
#
if __name__ == '__main__':
    print("This file should not be called directly as it only serves as a library.")
