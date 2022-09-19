import tkinter as tk
from typing import Union
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyCheckbutton(EasyWidget):
    """
    Class to define a widget, that displays a `tk.Checkbutton`.
    """

    def __init__(
            self,
            main_window,
            description: str = "",
            on: bool = False,
            width: int = None,
            height: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: ANCHORS = "w",
            justify: JUSTIFICATIONS = "left",
            add_to_grid: bool = True
    ):
        """
        Creates a new `EasyCheckbutton` object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify, width)

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # Variables
        self.label_string_var = tk.StringVar()
        self.label_string_var.set(description)
        self.object_var = tk.IntVar()
        self.object_var.set(1 if on else 0)

        # Checkbutton
        self.object = tk.Checkbutton(
            self.grid_object,
            variable=self.object_var,
            textvariable=self.label_string_var,
            anchor=anchor
        )

        # Arrange widgets
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if add_to_grid is False:
            self.remove_from_grid()

    def set(self, value: Union[bool, int]):
        """
        Sets the `EasyCheckbutton` on or off.
        """
        if not isinstance(value, int):
            value = int(value)

        self.object_var.set(value)

    def get(self) -> int:
        """
        Returns if the `EasyCheckbutton` is toggled on or off.
        """
        return self.object_var.get()
