import tkinter as tk
from tkinter import ttk
from typing import List
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyCombobox(EasyWidget):
    """
    Class to define a widget, that displays a `tkinter.ttk.Combobox`.
    """

    def __init__(
            self,
            main_window,
            values: List[str],
            description: str = "",
            default_value: str = ...,
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
        Creates a new `EasyCombobox` object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify)

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

        # Combobox
        self.object = ttk.Combobox(
            self.grid_object,
            values=values,
        )
        value = values[0] if default_value is ... else default_value
        self.object.set(value)

        # Arrange widgets
        self.label.pack(side="left", padx=(0, self.padx))
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Remove label if label text is empty
        if description.strip() == "":
            self.label.pack_forget()

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if not add_to_grid:
            self.remove_from_grid()

    def set(self, value: str):
        """
        Sets the `EasyCombobox` to the given `value`.
        """
        if not isinstance(value, str):
            value = str(value)

        self.object.set(value)

    def set_values(self, values: List[str]):
        """
        Adjusts the selectable `values` in the `EasyCombobox`.
        """
        self.object.config(values=values)

    def get(self) -> str:
        """
        Returns the currently selected item in the `EasyCombobox`.
        """
        return self.object.get()
