"""
This file contains the main class for creating user interfaces with the
easytk module.
"""

# ------------------------------
# Imports
#
import os
import tkinter as tk

from easytk import widgets
from typing import Any, List, Literal, Tuple, Union


# ------------------------------
# Globals
#
_CURRENT_DIR = os.getcwd()
_ROOT = tk.Tk()
_ROOT.withdraw()


# ------------------------------
# Classes
#
class Window:
    """
    Main class to create user interfaces with the easytk module.
    It can be called with the desired interface type.
    """

    def __init__(self, window_type="SelectionFalse", window_title="easytk"):
        self.return_values = None
        self.window_type = window_type

        # Initialize and configure the main window
        self.master_frame = tk.Toplevel(_ROOT)
        self.master_frame.attributes("-topmost", True)
        self.master_frame.protocol("WM_DELETE_WINDOW", self.close)  # Close window on close button
        self.master_frame.title(window_title)

        # Initialize collectors
        self.entries: List[Any] = []
        self.return_buttons: List[widgets.EasyWidget] = []
        self.return_objects: List[widgets.EasyWidget] = []

    def close(self):
        """
        Closes the window and destroys the tkinter root object.
        """
        self.master_frame.destroy()
        _ROOT.destroy()

    def show(self) -> Union[Tuple, bool, None]:
        """
        Shows the window and returns the value(s), that are given back
        for the chosen window type.
        """
        self.center_window()
        self.master_frame.update()
        self.master_frame.deiconify()
        self.master_frame.wait_window()

        return self.return_values

    def center_window(self):
        """
        Places the window at the center of the screen.
        """
        screen_width = self.master_frame.winfo_screenwidth()
        screen_height = self.master_frame.winfo_screenheight()
        window_width = self.master_frame.winfo_reqwidth()
        window_height = self.master_frame.winfo_reqheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.master_frame.geometry("+{}+{}".format(x_position, y_position))

    def yes_clicked(self):
        """
        Callback function for the yes button.
        """
        self.return_values = True
        self.close()

    def no_clicked(self):
        """
        Callback function for the no button.
        """
        self.return_values = False
        self.close()

    def cancel_clicked(self):
        """
        Callback function for the cancel button.
        """
        self.return_values = False
        self.close()

    def add_file_dialogue(self,
                          text: str,
                          initial_dir: str = _CURRENT_DIR,
                          filetypes: Tuple[Tuple[str, str]] = (),
                          default_value: str = ...,
                          width: int = None,
                          height: int = None,
                          label_width: int = None,
                          row: int = ...,
                          column: int = 1,
                          column_span: int = 1,
                          frame: tk.Frame = ...,
                          anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = "center",
                          justify: Literal["left", "right", "center"] = "left",
                          add_to_grid: bool = True
                          ):
        """
        Adds a file dialogue to the window.
        """
        added_widget = widgets.EasyFileDialogue(self,
                                                description=text,
                                                selection_type="file",
                                                initial_dir=initial_dir,
                                                filetypes=filetypes,
                                                default_value=default_value,
                                                width=width,
                                                height=height,
                                                label_width=label_width,
                                                row=row,
                                                column=column,
                                                column_span=column_span,
                                                frame=frame,
                                                anchor=anchor,
                                                justify=justify,
                                                add_to_grid=add_to_grid)

        # Add to collectors
        self.entries.append(added_widget.object)
        self.return_objects.append(added_widget)

        return added_widget
