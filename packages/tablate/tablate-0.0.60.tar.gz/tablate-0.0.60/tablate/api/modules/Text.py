from typing import Union

from tablate.classes.bases.TablateApiBase import TablateApiBase
from tablate.classes.bases.TablateApiItem import TablateApiItem
from tablate.library.initializers.processors.process_frame import process_frame
from tablate.type.primitives import TextAlign, FrameDivider, ContainerBorder, FrameName, TextStyle, TextColor, Background, \
    BackgroundPadding, Multiline, MaxLines, HtmlPxMultiplier, ContainerPadding, ContainerWidth, ColumnPadding, HtmlDefaultColors
from tablate.type.type_input import HtmlTextFrameStylesInput, HtmlContainerStylesInput


class Text(TablateApiItem):

    def __init__(self,
                 # TablateText args
                 text: Union[str, int, float],

                 name: FrameName = None,

                 text_style: TextStyle = None,
                 text_align: TextAlign = None,
                 text_color: TextColor = None,
                 frame_padding: ColumnPadding = None,
                 frame_divider: FrameDivider = None,
                 background: Background = None,
                 background_padding: BackgroundPadding = None,
                 multiline: Multiline = None,
                 max_lines: MaxLines = None,

                 html_default_colors: HtmlDefaultColors = None,

                 html_px_multiplier: HtmlPxMultiplier = None,
                 html_styles: HtmlTextFrameStylesInput = None,
                 # TablateApi arge
                 container_border: ContainerBorder = None,
                 container_padding: ContainerPadding = None,
                 container_width: ContainerWidth = None,
                 html_container_styles: HtmlContainerStylesInput = None) -> None:
        """
        Create a TablateItem text frame (single row, single column) to Tablate container instance.

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
                                   frame_type="text",
                                   frame_args=locals(),
                                   frame_list=self._frame_list,
                                   global_options=self._globals_store.store)

        self._frame_list[frame_dict.name] = frame_dict
