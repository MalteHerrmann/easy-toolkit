import tkinter as tk
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS
from easytk.widgets.easy_widget import EasyWidget


class EasyEntry(EasyWidget):
    """
    Class to define a `tk.Entry` widget, which can be used to get a user input.

    The text can be changed via the `set` method and returned with the `get` method
    of an `EasyEntry` instance.
    """

    def __init__(
            self,
            main_window,
            default_value: str = "",
            description: str = "",
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
        Creates a new `EasyEntry` object.

        :type main_window: easytk.Window
        """
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify, width)

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

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

        # Arrange widgets
        self.label.pack(side="left", padx=(0, self.padx))
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # Remove label if label text is empty
        if description.strip() == "":
            self.label.pack_forget()

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if add_to_grid is False:
            self.remove_from_grid()
