from copy import deepcopy
from typing import List, Union

from tablate.classes.bases.TablateApiSet import TablateApiSet
from tablate.library.initializers.processors.process_frame import process_frame
from tablate.type.primitives import FrameDivider, Multiline, TextColor, \
    TextAlign, TextStyle, MaxLines, HideHeader, Background, ColumnDivider, ColumnPadding, HtmlPxMultiplier, \
    BackgroundPadding, FrameName, OuterBorder, OuterPadding, OuterWidth, HtmlDefaultColors
from tablate.type.type_input import GridColumnInput, TableColumnInput, TableRowsInput, HtmlOuterStylesInput, \
    ColumnStylesInput, TextStylesInput, HtmlFrameStylesInput, \
    HtmlColumnStylesInput, HtmlTextStylesInput, HtmlTextFrameStylesInput, HtmlGridStylesInput, \
    HtmlTableHeaderStylesInput, HtmlTableBodyStylesInput, HtmlTableStylesInput, \
    TableHeaderFrameStylesInput, TableBodyFrameStylesInput


class Tablate(TablateApiSet):
    """Exceptions are documented in the same way as classes.

     The __init__ method may be documented in either the class level
     docstring, or as a docstring on the __init__ method itself.

     Either form is acceptable, but the two should not be mixed. Choose one
     convention to document the __init__ method and be consistent with it.

     Note:
         Do not include the `self` parameter in the ``Args`` section.

    """
    def __init__(self,
                 outer_border: OuterBorder = None,
                 outer_padding: OuterPadding = None,
                 outer_width: OuterWidth = None,

                 html_default_colors: HtmlDefaultColors = None,

                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_outer_styles: HtmlOuterStylesInput = None,

                 column_styles: ColumnStylesInput = None,
                 text_styles: TextStylesInput = None,

                 html_frame_styles: HtmlFrameStylesInput = None,

                 html_column_styles: HtmlColumnStylesInput = None,
                 html_text_styles: HtmlTextStylesInput = None) -> None:
        """

        Args:
            outer_border:
            outer_padding:
            outer_width:
            html_default_colors:
            frame_divider:
            background:
            background_padding:
            html_px_multiplier:
            html_outer_styles:
            column_styles:
            text_styles:
            html_frame_styles:
            html_column_styles:
            html_text_styles:
        """
        args = deepcopy(locals())
        del args["self"]

        TablateApiSet.__init__(self=self, **args)

    def add_text_frame(self,
                       text: Union[str, int, float],

                       name: FrameName = None,

                       text_style: TextStyle = None,
                       text_align: TextAlign = None,
                       text_color: TextColor = None,

                       frame_divider: FrameDivider = None,
                       frame_padding: ColumnPadding = None,
                       background: Background = None,
                       background_padding: BackgroundPadding = None,
                       multiline: Multiline = None,
                       max_lines: MaxLines = None,

                       html_px_multiplier: HtmlPxMultiplier = None,
                       html_styles: HtmlTextFrameStylesInput = None) -> None:
        """

        Args:
            text: Text string to insert into the text frame
            name: Name for the frame (useful for IPython)
            text_style: Normal / Bold
            text_align: Left / Right / Center
            text_color: ASCII color
            frame_divider: Blah
            frame_padding: Blah
            background: Blah
            background_padding: Blah
            multiline: Blah
            max_lines: Blah
            html_px_multiplier: Blah
            html_styles: Blah
        """
        frame_dict = process_frame(frame_name=name,
                                   frame_type="text",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict

    def add_grid_frame(self,
                       columns: List[Union[str, GridColumnInput]],

                       name: FrameName = None,

                       frame_divider: FrameDivider = None,
                       background: Background = None,
                       background_padding: BackgroundPadding = None,
                       multiline: Multiline = None,
                       max_lines: MaxLines = None,

                       column_divider: ColumnDivider = None,
                       column_padding: ColumnPadding = None,

                       text_style: TextStyle = None,
                       text_align: TextAlign = None,
                       text_color: TextColor = None,

                       html_px_multiplier: HtmlPxMultiplier = None,
                       html_styles: HtmlGridStylesInput = None) -> None:

        frame_dict = process_frame(frame_name=name,
                                   frame_type="grid",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict

    def add_table_frame(self,
                        columns: List[TableColumnInput],
                        rows: List[TableRowsInput],

                        name: FrameName = None,

                        frame_divider: FrameDivider = None,
                        multiline: Multiline = None,
                        max_lines: MaxLines = None,
                        background: Background = None,
                        background_padding: BackgroundPadding = None,

                        multiline_header: Multiline = None,
                        max_lines_header: MaxLines = None,
                        hide_header: HideHeader = None,

                        column_divider: ColumnDivider = None,
                        column_padding: ColumnPadding = None,
                        header_base_divider: FrameDivider = None,

                        row_line_divider: FrameDivider = None,
                        odd_row_background: Background = None,
                        even_row_background: Background = None,

                        text_style: TextStyle = None,
                        text_align: TextAlign = None,
                        text_color: TextColor = None,

                        header_styles: TableHeaderFrameStylesInput = None,
                        body_styles: TableBodyFrameStylesInput = None,

                        html_px_multiplier: HtmlPxMultiplier = None,
                        html_styles: HtmlTableStylesInput = None,

                        html_header_styles: HtmlTableHeaderStylesInput = None,
                        html_body_styles: HtmlTableBodyStylesInput = None) -> None:

        frame_dict = process_frame(frame_name=name,
                                   frame_type="table",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict
