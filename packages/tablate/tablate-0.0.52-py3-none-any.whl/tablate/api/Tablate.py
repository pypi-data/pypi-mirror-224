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
    """
    Container for text, grid and table frames. Allows cumulative addition of frames to an instance.

     Note:
         When using the 'Tablate' class in an IPython environment, it is important to name each frame (or else rerunning
            cells will create duplicate entries).

    Args:
        outer_border:
            outer border style for the Tablate container instance.
                [default: 'thick']
        outer_padding:
            outer padding (in Unicode character width) for the Tablate container instance.
                [default: 1]
        outer_width:
            outer width (in Unicode character width) for the Tablate container instance.
                [default: 120 or terminal width]
        html_default_colors:
            apply the default HTML color scheme to the Tablate instance.
                [default: True]
        frame_divider:
            default divider between frames within the Tablate container instance.
                [default: 'thick']
        background:
            default background for frames withing the Tablate container instance.
                [default: None]
        background_padding:
            additional padding applied to cells with a background color set when outputting to ASCII.
                [default: 1]
        html_px_multiplier:
            multiplier for HTML properties inherited from base (ASCII) styling.
                [default: 6]
        html_outer_styles:
            style dictionary for HTML specific styles for Tablate container instance.
                [default: None]
        column_styles:
            style dictionary for default column styles.
                [default: {"column_divider": 'thin', "padding": 1, "background_padding": 1}]
        text_styles:
            style dictionary for default text styles.
                [default: {
                "text_style": 'normal',
                "text_align": 'left',
                "text_color": None
                }]
        html_frame_styles:
            style dictionary for default HTML frame styles.
                [default: {\n
                "html_frame_divider_style": "thick",
                "html_frame_divider_weight: 1,
                "html_frame_divider_color": 'black',
                "html_multiline": True (False for Table frames),
                "html_max_lines": None,
                "html_background": None
                }]
        html_column_styles:
            style dictionary for default HTML column styles.
                [default: {
                "html_column_divider_style": 'thin',
                "html_column_divider_weight": 1,
                "html_column_divider_color": 'black',
                "html_padding": 6px
                }]
        html_text_styles:
            style dictionary for default HTML text styles.
                [default: {
                "html_text_style": 'normal',
                "html_text_align": 'left',
                "html_text_color": None,
                "html_text_size": 16
                }]
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
        Add a new text frame (single row, single column) to Tablate container instance.

        Args:
            text: Text frame content.
            name: Frame name (to prevent duplicate entries). [default: None]
            text_style: [default: 'normal']
            text_align: [default: 'left']
            text_color: [default: 'None']
            frame_divider: Dividing line at the bottom of the frame. [default: 'thick']
            frame_padding: Text padding within Text frame. [default: 1]
            background: Background color for the Text frame. [default: None]
            background_padding: Additional padding applied to text if background color set. [default: 1]
            multiline: Whether the text may wrap to multiple lines. [default: True]
            max_lines: Maximum number of lines to which the text may wrap. [default: None]
            html_px_multiplier: Multiplier for HTML properties inherited from base (ASCII) styling. [default: 6]
            html_styles: {"html_frame_styles": {"html_frame_divider_style": "thick", "html_frame_divider_weight: 1, "html_frame_divider_color": 'black', "html_multiline": True (False for Table frames), "html_max_lines": None, "html_background": None}, "html_text_styles": {"html_text_style": 'normal', "html_text_align": 'left', "html_text_color": None, "html_text_size": 16}}]
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
        """

        Add a new grid frame (single row of multiple columns) to Tablate instance.

        Args:
            columns:
            name:
            frame_divider:
            background:
            background_padding:
            multiline:
            max_lines:
            column_divider:
            column_padding:
            text_style:
            text_align:
            text_color:
            html_px_multiplier:
            html_styles:
        """
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
        """
        Add a new table frame (multiple rows of multiple columns) to Tablate instance.

        Args:
            columns:
            rows:
            name:
            frame_divider:
            multiline:
            max_lines:
            background:
            background_padding:
            multiline_header:
            max_lines_header:
            hide_header:
            column_divider:
            column_padding:
            header_base_divider:
            row_line_divider:
            odd_row_background:
            even_row_background:
            text_style:
            text_align:
            text_color:
            header_styles:
            body_styles:
            html_px_multiplier:
            html_styles:
            html_header_styles:
            html_body_styles:
        """
        frame_dict = process_frame(frame_name=name,
                                   frame_type="table",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict
