import tkinter as tk
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyLabel(EasyWidget):
    """
    Class to define a `tk.Label` widget, which can be used to display simple text.

    The text can be changed via the `set` method and returned with the `get` method
    of an `EasyLabel` instance.
    """

    def __init__(
            self,
            main_window,
            text: str = "",
            width: int = None,
            height: int = None,
            row: int = ...,
            column: int = 0,
            column_span: int = 1,
            frame: tk.Frame = ...,
            anchor: ANCHORS = "center",
            justify: JUSTIFICATIONS = "left",
            add_to_grid: bool = True
    ):
        """
        Creates a new EasyLabel object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify, width)

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # Label
        self.object_string_var = tk.StringVar()
        self.object_string_var.set(text)
        self.object = tk.Label(
            self.grid_object,
            textvariable=self.object_string_var,
            anchor=anchor,
            justify=justify
        )

        # Arrange widgets
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if add_to_grid is False:
            self.remove_from_grid()
