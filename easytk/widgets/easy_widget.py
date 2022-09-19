import tkinter as tk
from easytk.widgets.literals import ANCHORS, JUSTIFICATIONS


class EasyWidget:
    """
    Base class for all widgets, that can be added to an
    `easytk` user interface.
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
        self.label_string_var: tk.StringVar = ...
        self.object: tk.Widget = ...
        self.object_string_var: tk.StringVar = ...
        self.padx: int = 2
        self.row: int = ...
        self.width: int = ...

    def apply_settings(
            self,
            main_window,
            row: int,
            column: int,
            column_span: int,
            frame: tk.Frame,
            anchor: ANCHORS,
            justify: JUSTIFICATIONS,
            width: int = None,
    ):
        """
        Applies the given settings to the `EasyWidget`.

        :type main_window: easytk.Window
        """
        self.main_window = main_window
        self.row = row
        self.column = column
        self.column_span = column_span
        self.frame = main_window.main_frame if frame is ... else frame
        # self.frame = main_window.master_frame if frame is ... else frame
        self.anchor = anchor
        self.justify = justify
        self.width = main_window.width if width is None else width

    def insert_into_grid(
            self,
            frame: tk.Frame,
            row: int,
            column: int,
            column_span: int,
            check_return_widget: bool = True
    ):
        """
        Adds the `EasyWidget` to the grid.

        If no `row` or `column` values are given, the function checks the
        current grid size of the `tk.Frame`, and adds the widget to the
        next free row in the first column, spanning the amount of columns
        defined by `column_span`.
        """
        # TODO: Add options for widgets to define own sticky value
        sticky = 'wen'  # stick to both sides

        if check_return_widget and self.main_window.return_widget is not ...:
            _RETURN_WIDGET_EXISTS = True
            self.main_window.return_widget.grid_object.grid_forget()
        else:
            _RETURN_WIDGET_EXISTS = False

        if row is ...:
            row = frame.grid_size()[1]

        self.grid_object.grid(row=row, column=column, columnspan=column_span, sticky=sticky)

        if _RETURN_WIDGET_EXISTS:
            self.main_window.return_widget.grid_object.grid()

    def remove_from_grid(self):
        """
        Removes the `EasyWidget` from the grid without forgetting the
        previous position. This makes it possible to add the widget
        to the same position as before by making an empty `grid()` call
        without any positioning arguments.
        """
        self.grid_object.grid_remove()

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
        if hasattr(self.object, "xview_moveto"):
            self.object.xview_moveto(1.0)
