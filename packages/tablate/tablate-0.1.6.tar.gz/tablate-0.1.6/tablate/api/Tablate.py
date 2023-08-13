from copy import deepcopy
from typing import List, Union

from tablate.classes.bases.TablateApiSet import TablateApiSet
from tablate.library.calcs.gen_frame_name import gen_frame_name
from tablate.library.initializers.processors.process_frame import process_frame
from tablate.library.initializers.table_init import table_init
from tablate.type.primitives import FrameDivider, Multiline, TextColor, \
    TextAlign, TextStyle, MaxLines, HideHeader, Background, ColumnDivider, ColumnPadding, HtmlPxMultiplier, \
    BackgroundPadding, FrameName, ContainerBorder, ContainerPadding, ContainerWidth, HtmlDefaultColors
from tablate.type.type_input import GridColumnInput, TableColumnInput, TableRowsInput, HtmlContainerStylesInput, \
    ColumnStylesInput, TextStylesInput, HtmlFrameStylesInput, \
    HtmlColumnStylesInput, HtmlTextStylesInput, HtmlTextFrameStylesInput, HtmlGridFrameStylesInput, \
    HtmlTableHeaderStylesInput, HtmlTableFrameStylesInput, \
    TableHeaderFrameStylesInput
from tablate.type.type_store import FrameDict


class Tablate(TablateApiSet):
    """
    Container for text, grid and table frames. Allows cumulative addition of frames to an instance.

     Note:
         When using the 'Tablate' class in an IPython environment, it is important to name each frame (or else rerunning cells will create duplicate entries).

    Args:
        container_border: outer border style for the Tablate container instance.
            [default: 'thick']
        container_padding: outer padding (in Unicode character width) for the Tablate container instance.
            [default: 1]
        container_width: outer width (in Unicode character width) for the Tablate container instance.
            [default: 120 or terminal width]
        html_default_colors: apply the default HTML color scheme to the Tablate instance.
            [default: True]
        frame_divider: default dividing line between frames within the Tablate container instance.
            [default: 'thick']
        background: default background for frames withing the Tablate container instance.
            [default: None]
        background_padding: additional padding applied to cells with a background color set (ASCII only).
            [default: 1]
        html_px_multiplier: Multiplier applied to HTML px properties.
            [default: 1]
        html_container_styles: style dictionary for HTML specific styles for Tablate container instance.
            [default: None]
        column_styles: style dictionary for default base column styles.
            [default: {"column_divider": 'thin', "padding": 1, "background_padding": 1}]
        text_styles: style dictionary for default base text styles.
            [default: {
            "text_style": 'normal',
            "text_align": 'left',
            "text_color": None
            }]
        html_frame_styles: style dictionary for default HTML specific frame styles.
            [default: {\n
            "html_frame_divider_style": "thick",
            "html_frame_divider_weight: 1,
            "html_frame_divider_color": 'black',
            "html_multiline": True (False for Table frames),
            "html_max_lines": None,
            "html_background": None
            }]
        html_column_styles: style dictionary for default HTML specific column styles.
            [default: {
            "html_column_divider_style": 'thin',
            "html_column_divider_weight": 1,
            "html_column_divider_color": 'black',
            "html_padding": 6px
            }]
        html_text_styles: style dictionary for default HTML specific text styles.
            [default: {
            "html_text_style": 'normal',
            "html_text_align": 'left',
            "html_text_color": None,
            "html_text_size": 16
            }]
    """

    def __init__(self,
                 container_border: ContainerBorder = None,
                 container_padding: ContainerPadding = None,
                 container_width: ContainerWidth = None,

                 html_default_colors: HtmlDefaultColors = None,

                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_container_styles: HtmlContainerStylesInput = None,

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
                [required]
            name: Frame name (to prevent duplicate entries).
                [default: None]
            text_style: Text style for text frame.
                [default: 'normal']
            text_align: Text alignment for text frame.
                [default: 'left']
            text_color: Text color for text frame.
                [default: 'None']
            frame_divider: Dividing line at the bottom of the frame.
                [default: 'thick']
            frame_padding: Text padding within text frame.
                [default: 1]
            background: Background color for the text frame.
                [default: None]
            background_padding: Additional padding applied to text if background color set (ASCII only).
                [default: 1]
            multiline: Whether the text may wrap to multiple lines.
                [default: True]
            max_lines: Maximum number of lines to which the text may wrap.
                [default: None]
            html_px_multiplier: Multiplier applied to HTML px properties.
                [default: 1]
            html_styles: HTML specific styles for text frame.
                [default: {
                "html_frame_styles": {"html_frame_divider_style": "thick", "html_frame_divider_weight: 1, "html_frame_divider_color": 'black', "html_multiline": True (False for Table frames), "html_max_lines": None, "html_background": None },
                "html_text_styles": {"html_text_style": 'normal', "html_text_align": 'left', "html_text_color": None, "html_text_size": 16 }
                }]
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
                       html_styles: HtmlGridFrameStylesInput = None) -> None:
        """

        Add a new grid frame (single row of multiple columns) to Tablate instance.

        Args:
            columns: Either a list of contents (str, int, float) for columns or a list of column dicts containing contents and styles for columns.
                [required]
            name: Frame name (to prevent duplicate entries).
                [default: None]
            frame_divider: Dividing line at the bottom of the frame.
                [default: 'thick']
            background: Background color for the grig frame.
                [default: None]
            background_padding: Additional padding applied to text if background color set (ASCII only).
                [default: 1]
            multiline: Whether the text may wrap to multiple lines.
                [default: True]
            max_lines: Maximum number of lines to which the text may wrap.
                [default: None]
            column_divider: Dividing line between columns.
                [default: 'thin']
            column_padding: Text padding within each column.
                [default: 1]
            text_style: Text style for grid frame.
                [default: 'normal']
            text_align: Text alignment for grid frame.
                [default: 'left']
            text_color: Text color for grid frame.
                [default: 'None']
            html_px_multiplier: Multiplier applied to HTML px properties.
                [default: 1]
            html_styles: HTML specific styles for grid frame.
                [default: {
                "html_frame_styles": {"html_frame_divider_style": "thick", "html_frame_divider_weight: 1, "html_frame_divider_color": 'black', "html_multiline": True (False for Table frames), "html_max_lines": None, "html_background": None },
                "html_column_styles": {"html_column_divider_style": "thin", "html_column_divider_weight": 1, "html_column_divider_color": "black", "html_padding": "6px"}
                "html_text_styles": {"html_text_style": 'normal', "html_text_align": 'left', "html_text_color": None, "html_text_size": 16 }
                }]
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
                        background: Background = None,
                        background_padding: BackgroundPadding = None,
                        multiline: Multiline = None,
                        max_lines: MaxLines = None,

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

                        html_px_multiplier: HtmlPxMultiplier = None,
                        html_styles: HtmlTableFrameStylesInput = None,

                        html_header_styles: HtmlTableHeaderStylesInput = None) -> None:
        """
        Add a new table frame (multiple rows of multiple columns) to Tablate instance.

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
        """
        frame_dict = process_frame(frame_name=name,
                                   frame_type="table",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict

    def from_dict(self,
                  dict_object: dict,
                  name: FrameName = None,
                  capitalize_keys: bool = True,
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

                  html_px_multiplier: HtmlPxMultiplier = None,
                  html_styles: HtmlTableFrameStylesInput = None,

                  html_header_styles: HtmlTableHeaderStylesInput = None):
        """
        Creates a table frame from a dict in three possible formats:
            - {"one": [1, 2, 3], "two": [4, 5, 6]}
            - {'one': {0: 1, 1: 2, 2: 3}, 'two': {0: 1, 1: 2, 2: 3}}
            - {'one': {(1, 'red'): 1, (1, 'blue'): 2, (2, 'green'): 3}, 'two': {(1, 'red'): 1, (1, 'blue'): 2, (2, 'green'): 3}

        Pandas returns the latter two dict types from its `.to_dict()` method.

        Args:
            dict_object: Input dict.
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
        """
        name = gen_frame_name(name=name, type="table", frame_dict=self._frame_list)

        args = deepcopy(locals())
        del args["self"]
        del args["dict_object"]
        del args["capitalize_keys"]

        columns = []
        rows = []
        for col_index, (col_key, col_value) in enumerate(dict_object.items()):
            if type(col_value) == dict:
                for row_index, (row_value_index, row_value) in enumerate(col_value.items()):
                    if col_index == 0:
                        rows.append({})
                        if type(row_value_index) == tuple:
                            for i in range(0, len(row_value_index)):
                                if row_index == 0:
                                    columns.append({"key": f"i{i}", "width": "10%", "text_align": "right"})
                                rows[row_index][f"i{i}"] = row_value_index[i]
                        else:
                            if row_index == 0:
                                columns.append({"key": "i", "width": "10%", "text_align": "right"})
                            rows[row_index]["i"] = row_value_index
                    rows[row_index][col_key.title() if capitalize_keys else col_key] = row_value
            elif type(col_value) == list:
                for row_index, row_value in enumerate(col_value):
                    if col_index == 0:
                        rows.append({})
                    rows[row_index][col_key.title() if capitalize_keys else col_key] = row_value
            columns.append({"key": col_key.title() if capitalize_keys else col_key})

        # new_table = Table(columns=columns, rows=rows, **args)
        # todo: fix column widths... ensure no bugs if millions of index columns
        # todo: for later allow specific column widths
        table_store = table_init(**args,
                                 columns=columns,
                                 rows=rows,
                                 global_options=self._globals_store.store)
        self._frame_list[name] = FrameDict(name=name,
                                           type="table",
                                           args={"columns": columns, "rows": rows, **args},
                                           store=table_store)
