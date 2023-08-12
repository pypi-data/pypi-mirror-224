from typing import List, Union

from tablate.classes.bases.TablateApiBase import TablateApiBase
from tablate.classes.bases.TablateApiItem import TablateApiItem
from tablate.library.initializers.processors.process_frame import process_frame
from tablate.type.primitives import FrameDivider, ColumnDivider, ContainerBorder, ContainerPadding, ContainerWidth, Background, \
    BackgroundPadding, HtmlPxMultiplier, Multiline, MaxLines, ColumnPadding, TextStyle, TextAlign, TextColor, FrameName, \
    HtmlDefaultColors
from tablate.type.type_input import GridColumnInput, HtmlContainerStylesInput, HtmlGridFrameStylesInput


class Grid(TablateApiItem):

    def __init__(self,
                 # TablateGrid args
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
                 html_styles: HtmlGridFrameStylesInput = None,
                 # TablateApi args
                 html_default_colors: HtmlDefaultColors = None,
                 container_border: ContainerBorder = None,
                 container_padding: ContainerPadding = None,
                 container_width: ContainerWidth = None,
                 html_container_styles: HtmlContainerStylesInput = None) -> None:
        """
        Create a TablateItem grid frame (single row of multiple columns) to Tablate instance.

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
            container_border: outer border style for the Tablate container instance.
                [default: 'thick']
            container_padding: outer padding (in Unicode character width) for the Tablate container instance.
                [default: 1]
            container_width: outer width (in Unicode character width) for the Tablate container instance.
                [default: 120 or terminal width]
            html_container_styles: style dictionary for HTML specific styles for Tablate container instance.
                [default: None]
        """
        TablateApiBase.__init__(self=self,
                                container_border=container_border,
                                container_padding=container_padding,
                                frame_divider=frame_divider,
                                container_width=container_width,
                                html_container_styles=html_container_styles,
                                html_default_colors=html_default_colors)

        frame_dict = process_frame(frame_name=name,
                                   frame_type="grid",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict
