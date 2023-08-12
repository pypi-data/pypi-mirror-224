from typing import List

from tablate.classes.bases.TablateApiBase import TablateApiBase
from tablate.classes.bases.TablateApiItem import TablateApiItem
from tablate.library.initializers.processors.process_frame import process_frame
from tablate.type.primitives import FrameDivider, ColumnDivider, ContainerBorder, \
    FrameName, Multiline, MaxLines, Background, BackgroundPadding, HideHeader, ColumnPadding, TextAlign, TextStyle, \
    TextColor, HtmlPxMultiplier, ContainerPadding, ContainerWidth, HtmlDefaultColors
from tablate.type.type_input import TableColumnInput, TableRowsInput, TableBodyFrameStylesInput, \
    TableHeaderFrameStylesInput, HtmlTableFrameStylesInput, HtmlTableHeaderStylesInput, HtmlContainerStylesInput


class Table(TablateApiItem):

    def __init__(self,
                 # TablateTable args
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

                 html_default_colors: HtmlDefaultColors = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlTableFrameStylesInput = None,

                 html_header_styles: HtmlTableHeaderStylesInput = None,

                 container_border: ContainerBorder = None,
                 container_padding: ContainerPadding = None,
                 container_width: ContainerWidth = None,
                 html_container_styles: HtmlContainerStylesInput = None) -> None:
        """
        Create a TablateItem table frame (multiple rows of multiple columns) to Tablate instance.


        Args:
            columns: List of column dicts containing a required column key and optional (str, int, float) to display, as well as column specific styling options.
                [required]
            rows: List of row dicts containing the (str, int, float) values for each column key.
                [required]
            name: Frame name (to prevent duplicate entries).
                [default: None]
            frame_divider: Dividing line at the bottom of the frame.
                [default: 'thick']
            background: Background color for the table frame.
                [default: None]
            background_padding: Additional padding applied to text if background color set (ASCII only).
                [default: 1]
            multiline: Whether the text may wrap to multiple lines.
                [default: False]
            max_lines: Maximum number of lines to which the text may wrap.
                [default: None]
            multiline_header: Whether the header text may wrap to multiple lines.
                [default: False]
            max_lines_header: Maximum number of lines to which the header text may wrap.
                [default: None]
            hide_header: Whether to not render the header.
                [default: False]
            column_divider: Dividing line between columns.
                [default: 'thin']
            column_padding: Text padding within each column.
                [default: 1]
            header_base_divider: Dividing line at the bottom of the table header frame.
                [default: 'thick']
            row_line_divider: Dividing line between each row of the table frame.
                [default: 'thin']
            odd_row_background: Background color for odd rows of table frame.
                [default: None]
            even_row_background: Background color for even rows of table frame.
                [default: None]
            text_style: Text style for table frame.
                [default: 'normal']
            text_align: Text alignment for table frame.
                [default: 'left']
            text_color: Text color for grid frame.
                [default: None]
            header_styles: Specific styles to apply to the table header frame.
                [default: None (inherits table styles)]
            html_px_multiplier: Multiplier applied to HTML px properties.
                [default: 1]
            html_styles: HTML specific styles for table frame.
                [default: {
                "html_frame_styles": {"html_frame_divider_style": "thick", "html_frame_divider_weight: 1, "html_frame_divider_color": 'black', "html_multiline": True (False for Table frames), "html_max_lines": None, "html_background": None },
                "html_column_styles": {"html_column_divider_style": "thin", "html_column_divider_weight": 1, "html_column_divider_color": "black", "html_padding": "6px"},
                "html_text_styles": {"html_text_style": 'normal', "html_text_align": 'left', "html_text_color": None, "html_text_size": 16 },
                "html_row_styles": {"html_row_line_divider_weight": 1, "html_row_line_divider_style": "thin", "html_row_line_divider_color": None, "html_odds_background": None, "html_evens_background": None}
                }] (Tablate constructor option `html_default_colors` applies styles to table headers and even rows, separately from, but overwritten by, this html_styles dict)
            html_header_styles: HTML specific styles for table header frame.
                [default: None (inherits table styles)]
            container_border: outer border style for the Tablate container instance.
                [default: 'thick']
            container_padding: outer padding (in Unicode character width) for the Tablate container instance.
                [default: 1]
            container_width: outer width (in Unicode character width) for the Tablate container instance.
                [default: 120 or terminal width]
            html_container_styles: style dictionary for HTML specific styles for Tablate container instance.
                [default: None]        """
        TablateApiBase.__init__(self=self,
                                container_border=container_border,
                                container_padding=container_padding,
                                frame_divider=frame_divider,
                                container_width=container_width,
                                html_default_colors=html_default_colors,
                                html_container_styles=html_container_styles)

        frame_dict = process_frame(frame_name=name,
                                   frame_type="table",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict
