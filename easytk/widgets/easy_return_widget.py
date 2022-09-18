"""
This module contains a generalized class, which serves
the different return button objects, that are used to
close the easytk GUI and return the respective values
to the user. Depending on the selected window type,
this might be a collection of the user inputs (`Selection`)
or a boolean value (`SelectionFalse`, `YesNo`).

These widgets are not directly usable and are inserted into
the easytk window automatically, depending on the chosen
window type.
"""

# ------------------------------
# Imports
#
import tkinter as tk
from typing import Literal
from easytk.widgets.easy_widget import EasyWidget


# ------------------------------
# Classes
#
class EasyReturnWidget(EasyWidget):
    """
    Generalized class, which builds the necessary widgets for
    the selected return type for the GUI (e.g. `SelectionFalse`).

    It contains methods to define the main window's return
    value(s) and close the GUI.
    """

    def __init__(self,
                 main_window,
                 return_type: Literal["Selection", "SelectionFalse", "YesNo"],
                 row: int = ...,
                 column: int = 0,
                 column_span: int = 1,
                 frame: tk.Frame = ...
                 ):
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, "center", "center")

        self.grid_object = tk.Frame(self.frame)
        self.grid_object.grid_propagate(False)

        if return_type in ("Selection", "SelectionFalse"):
            self.select_button = tk.Button(
                self.grid_object,
                text=main_window.selection_text,
                command=self.get_return_values
            )
            self.select_button.pack(side="left")
        elif return_type == "YesNo":
            self.yes_button = tk.Button(
                self.grid_object,
                text=main_window.yes_text,
                command=self.yes_clicked
            )
            self.yes_button.pack(side="left")
        else:
            raise ValueError(f"Unknown window type: {return_type}")

        if return_type == "SelectionFalse":
            self.false_button = tk.Button(
                self.grid_object,
                text=main_window.false_text,
                command=self.no_clicked
            )
            self.false_button.pack(side="left")

        elif return_type == "YesNo":
            self.no_button = tk.Button(
                self.grid_object,
                text=main_window.no_text,
                command=self.no_clicked
            )
            self.no_button.pack(side="left")

        self.insert_into_grid(self.frame, row, column, column_span, check_return_widget=False)

    def yes_clicked(self):
        """
        Callback function for the yes button.
        """
        self.main_window.return_values = True
        self.main_window.close()

    def no_clicked(self):
        """
        Callback function for the no button.
        """
        self.main_window.return_values = False
        self.main_window.close()

    def get_return_values(self):
        """
        Callback function for the select button.

        Gets all returnable values from the widgets contained in the GUI
        and assigns them to the main window.
        """

        return_values = tuple(widget.get() for widget in self.main_window.return_objects)
        self.main_window.return_values = return_values
        self.main_window.close()


# ------------------------------
# Execution
#
if __name__ == '__main__':
    print("This file should not be called directly as it only serves as a library.")
