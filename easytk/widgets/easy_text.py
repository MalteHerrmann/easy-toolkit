import tkinter as tk
from easytk.widgets.easy_widget import EasyWidget
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyText(EasyWidget):
    """
    Class to define a `tk.Text` widget, which can be used to display text.

    The text can be changed via the `set` method and returned with the `get` method
    of an `EasyText` instance.
    """

    def __init__(
            self,
            main_window,
            text: str = "",
            export: bool = False,
            monospace: bool = False,
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
        super().__init__()
        self.apply_settings(main_window, row, column, column_span, frame, anchor, justify)
        self.export = export

        # Widget frame
        self.grid_object = tk.Frame(self.frame, width=width, height=height)

        # Text
        self.object = tk.Text(
            self.grid_object,
        )
        # TODO: Define default font for non-monospace texts?
        if monospace:
            self.object.config(font="Courier")
        self.object.insert(tk.END, text)

        # Arrange widgets
        self.object.pack(side="left", fill="both", expand=True, padx=self.padx)

        # No widget shrinking
        self.grid_object.grid_propagate(False)

        # Add to grid and then remove if desired
        self.insert_into_grid(self.frame, row, column, column_span)
        if add_to_grid is False:
            self.remove_from_grid()

    def set(self, value: str) -> None:
        if isinstance(value, str):
            self.object.delete(1.0, tk.END)
            self.object.insert(1.0, value)
            self.object.xview_moveto(1)

    def get(self) -> str:
        return self.object.get("1.0", "end-1c")
