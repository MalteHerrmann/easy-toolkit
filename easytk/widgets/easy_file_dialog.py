import os
import tkinter as tk
from tkinter import filedialog
from typing import List, Literal, Union, Tuple
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS

# Colors
_OK_COLOR = "#d3ffce"
_NOT_OK_COLOR = "#ffe4e1"
_OVERWRITE_COLOR = "#ffff70"


class EasyFileDialog(EasyWidget):
    """
    Class to define a widget, that consists of an entry field
    and a button to open a file/directory dialog, as well as an optional
    label to describe the file/directory to be selected.
    """

    def __init__(
            self,
            main_window,
            description: str = "",
            initial_dir: str = os.getcwd(),
            filetypes: Union[List[Tuple[str, str]], None] = None,
            selection_type: Literal["file", "dir", "save"] = "file",
            default_value: str = "",
            width: int = None,
            height: int = None,
            label_width: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: ANCHORS = "center",
            justify: JUSTIFICATIONS = "left",
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
        self.label_string_var = tk.StringVar()
        self.label_string_var.set(description)
        self.label = tk.Label(
            self.grid_object,
            textvariable=self.label_string_var,
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

    def set(self, value: str):
        """
        Sets the value of the object string variable.
        """
        if not isinstance(value, str):
            value = str(value)

        self.object_string_var.set(value)
        self.check_path(self.selection_type)
        self.object.xview_moveto(1.0)
