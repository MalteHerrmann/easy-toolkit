"""
The widgets, that can be added to an easytk window, are defined in this
module. All widgets are subclasses of the abstract class EasyWidget, which
defines common methods and attributes, e.g. for adding the widget to the
main window.

It should be noted, that these widgets are not directly usable, but rather
should be added using the add_* methods of the Window class.
"""
# ------------------------------
# Imports
#
import os
import tkinter as tk
from tkinter import filedialog
from typing import List, Literal, Tuple, Union

# ------------------------------
# Globals
#
_CURRENT_DIR = os.getcwd()

# Colors
_OK_COLOR = "#d3ffce"
_NOT_OK_COLOR = "#ffe4e1"
_OVERWRITE_COLOR = "#ffff70"


# ------------------------------
# Classes
#
class EasyWidget:
    """
    Base class for all widgets, that can be added to an
    easytk user interface.
    """

    def __init__(self):
        self.add_to_grid: bool = True
        self.anchor: str = ...
        self.column: int = ...
        self.column_span: int = 1
        self.frame: tk.Frame = ...
        self.grid_object: tk.Frame = ...
        self.justify: str = ...
        self.main_window = ...
        self.padx: int = 2
        self.row: int = ...

    def apply_settings(
            self,
            main_window,
            row: int,
            column: int,
            column_span: int,
            frame: tk.Frame,
            anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"],
            justify: Literal["left", "right", "center"]
    ):
        """
        Applies the given settings to the widget.
        """
        self.main_window = main_window
        self.row = row
        self.column = column
        self.column_span = column_span
        self.frame = main_window.master_frame if frame is ... else frame
        self.anchor = anchor
        self.justify = justify

    def insert_into_grid(
            self,
            frame: tk.Frame,
            row: int,
            column: int,
            column_span: int,
    ):
        """
        Adds the widget to the grid. If no row or column values are
        given, the function checks the current grid size of the frame,
        and adds the widget to the next free row in the first column,
        spanning the amount of columns defined by column_span.
        """
        if hasattr(self, "main_window") and len(self.main_window.return_buttons) > 0:
            _RETURN_BUTTONS_EXIST = True
            for button in self.main_window.return_buttons:
                button.grid_object.grid_forget()
        else:
            _RETURN_BUTTONS_EXIST = False

        if row is ...:
            row = frame.grid_size()[1]

        self.grid_object.grid(row=row, column=column, columnspan=column_span)

        if _RETURN_BUTTONS_EXIST:
            for button in self.main_window.return_buttons:
                button.grid_object.grid()

    def remove_from_grid(self):
        """
        Removes the widget from the grid without forgetting the
        previous position. This makes it possible to add the widget
        to the same position as before by making an empty grid() call
        without any positioning arguments.
        """
        self.grid_object.grid_remove()


class EasyFileDialogue(EasyWidget):
    """
    Class to define a widget, that consists of an entry field
    and a button to open a file/directory dialogue, as well as an optional
    label to describe the file/directory to be selected.
    """

    def __init__(
            self,
            main_window,
            description: str = "",
            initial_dir: str = _CURRENT_DIR,
            filetypes: Union[List[Tuple[str, str]], None] = None,
            selection_type: Literal["file", "dir", "save"] = "file",
            default_value: str = "",
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
        Creates a new EasyFileDialogue object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify)
        self.selection_type = selection_type

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # Label
        self.string_var = tk.StringVar()
        self.string_var.set(description)
        self.label = tk.Label(
            self.grid_object,
            textvariable=self.string_var,
            width=label_width,
            anchor=anchor,
            justify=justify
        )

        # Entry field
        self.object_string_var = tk.StringVar()
        self.object_string_var.set(default_value)
        self.object = tk.Entry(
            self.grid_object,
            textvariable=self.object_string_var,
            width=width
        )
        self.object.xview_moveto(1.0)

        # Dialogue button
        button = tk.Button(
            self.grid_object,
            text="...",
            width=5,
            command=lambda: self.file_chosen(
                initial_dir,
                filetypes
            )
        )

        # Arrange widgets
        self.label.pack(side="left", padx=(0, self.padx))
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)
        button.pack(side="left", padx=(self.padx, 0))

        # Remove label if label text is empty
        if description == "":
            self.label.pack_forget()

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Bind the string variable to the check path method
        self.object_string_var.trace("w", self.check_path)
        self.check_path()

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if add_to_grid is False:
            self.remove_from_grid()

    def check_path(self, *_):
        """
        Checks if the path stored in the object string variable is valid.
        """
        value = self.get()
        if value.strip() == "":
            return

        if self.selection_type == "dir":
            if os.path.isdir(value):
                background_color = _OK_COLOR
            else:
                background_color = _NOT_OK_COLOR
        elif self.selection_type == "file":
            if os.path.isfile(value):
                background_color = _OK_COLOR
            else:
                background_color = _NOT_OK_COLOR
        elif self.selection_type == "save":
            dir_name = os.path.dirname(value)
            if os.path.isfile(value) and os.path.exists(value):
                background_color = _OVERWRITE_COLOR
            elif dir_name == "" or os.path.isdir(dir_name):
                background_color = _OK_COLOR
            else:
                background_color = _NOT_OK_COLOR
        else:
            raise ValueError(f"Invalid path type: {self.selection_type}. Expecting 'file', 'dir' or 'save'.")

        self.object.config(background=background_color)

    def file_chosen(
            self,
            initial_dir: str,
            filetypes: Union[List[Tuple[str, str]], None]
    ):
        """
        Opens a file/directory dialogue and sets the selected path in the entry field.
        """
        if ("All files", "*.*") not in filetypes:
            filetypes.append(("All files", "*.*"))

        if self.selection_type == "file":
            path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=filetypes)
        elif self.selection_type == "dir":
            path = filedialog.askdirectory(initialdir=initial_dir)
        elif self.selection_type == "save":
            path = filedialog.asksaveasfilename(initialdir=initial_dir, filetypes=filetypes)
        else:
            raise ValueError("Invalid selection type.")

        self.set(path)

    def get(self):
        """
        Returns the value of the object string variable.
        """
        return self.object_string_var.get()

    def set(self, value: str):
        """
        Sets the value of the object string variable.
        """
        if not isinstance(value, str):
            value = str(value)

        self.object_string_var.set(value)
        self.check_path(self.selection_type)
        self.object.xview_moveto(1.0)
