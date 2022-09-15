"""
This file contains the main class for creating user interfaces with the
easytk module.
"""

# ------------------------------
# Imports
#
import os
import tkinter as tk

from easytk import return_buttons, widgets
from typing import Any, List, Literal, Tuple, Union


# ------------------------------
# Globals
#
_CURRENT_DIR = os.getcwd()
_ROOT = tk.Tk()
_ROOT.withdraw()

WINDOW_TYPES = Literal["Selection", "SelectionFalse", "YesNo", "Message"]


# ------------------------------
# Classes
#
class Window:
    """
    Main class to create user interfaces with the easytk module.
    It can be called with the desired interface type.
    """

    def __init__(
            self,
            window_type: WINDOW_TYPES = "SelectionFalse",
            window_title: str = "easytk",
            testing: bool = False
    ):
        """
        Creates an instance of an easytk window.

        :param window_type: The type of GUI that will be displayed
        :param window_title: The title of the GUI
        """
        self.label_width: int = ...
        self.return_values: Tuple[Any] = ...
        self.title: str = window_title
        self.window_type: WINDOW_TYPES = window_type
        self._TESTING: bool = testing

        # Initialize return button texts
        self.cancel_text: str = "Cancel"  # TODO: necessary? or should SelectionFalse be renamed to SelectionCancel?
        self.false_text: str = "Cancel"
        self.no_text: str = "No"
        self.ok_text: str = "OK"
        self.selection_text: str = "Select"
        self.yes_text: str = "Yes"

        # Initialize and configure the main window
        self.master_frame = tk.Toplevel(_ROOT)
        self.master_frame.attributes("-topmost", True)
        self.master_frame.protocol("WM_DELETE_WINDOW", self.close)  # Close window on close button
        self.master_frame.title(window_title)

        # Initialize collectors
        self.entries: List[Any] = []
        self.return_widget: return_buttons.EasyReturnWidget = ...
        self.return_objects: List[widgets.EasyWidget] = []

    def close(self):
        """
        Closes the window and destroys the tkinter root object.
        """
        self.master_frame.destroy()
        if not self._TESTING:
            _ROOT.destroy()

    def show(self) -> Union[Tuple, bool, None]:
        """
        Shows the `Window` and returns the value(s), that are given back
        for the chosen window type.
        """
        column_span, _ = self.master_frame.grid_size()
        self.return_widget = self.add_return_widget(self.window_type, column_span=column_span)

        self.center_window()
        if not self._TESTING:
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

    def config(self, **kwargs):
        """
        Checks if the given kwargs refer to valid settings and if so,
        changes to the given value.

        :param kwargs: The name of a class attribute and its new value
        """

        for arg in kwargs:
            if hasattr(self, arg):
                previous_value = eval(f"self.{arg}")
                if not isinstance(kwargs[arg], type(previous_value)) and previous_value is not None:
                    raise ValueError(f"""Incompatible type {type(kwargs[arg])} for setting: {arg}.\n --> Should be {eval('type(self.{})'.format(arg))}""")
                else:
                    if arg == "title":
                        self.master_frame.title(kwargs[arg])
                    else:
                        exec("""self.{} = {}""".format(arg, repr(kwargs[arg])))
            else:
                raise ValueError(f"Unknown setting: {arg}\n --> This cannot be edited at the present moment.")

    def add_return_widget(
            self,
            window_type: WINDOW_TYPES,
            column_span: int = 1
    ) -> return_buttons.EasyReturnWidget:
        """
        Adds the widget corresponding to the chosen window type
        to the layout.

        :return: the added `EasyReturnWidget` object
        """

        return return_buttons.EasyReturnWidget(self, window_type, column_span=column_span)

    def add_file_dialogue(
            self,
            text: str,
            initial_dir: str = _CURRENT_DIR,
            filetypes: Union[List[Tuple[str, str]], None] = None,
            default_value: str = ...,
            width: int = None,
            height: int = None,
            label_width: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: widgets.ANCHORS = "center",
            justify: widgets.JUSTIFICATIONS = "left",
            add_to_grid: bool = True
    ):
        """
        Adds a `widgets.EasyFileDialogue` to the window.
        """
        added_widget = widgets.EasyFileDialogue(
            self,
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
            add_to_grid=add_to_grid
        )

        # Add to collectors
        self.entries.append(added_widget.object)
        self.return_objects.append(added_widget)

        return added_widget

    def add_label(
            self,
            text: str,
            width: int = None,
            height: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: widgets.ANCHORS = "center",
            justify: widgets.JUSTIFICATIONS = "left",
            add_to_grid: bool = True
    ):
        """
        Adds an `widgets.EasyLabel` to the window.
        """
        added_widget = widgets.EasyLabel(
            self,
            text=text,
            width=width,
            height=height,
            row=row,
            column=column,
            column_span=column_span,
            frame=frame,
            anchor=anchor,
            justify=justify,
            add_to_grid=add_to_grid
        )

        return added_widget
