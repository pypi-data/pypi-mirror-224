from copy import deepcopy
from typing import List

from tablate.classes.bases.TablateSet import TablateSet
from tablate.classes.classes import TablateUnion
from tablate.type.primitives import FrameDivider, ContainerBorder, ContainerPadding, ContainerWidth, Background, BackgroundPadding, \
    HtmlPxMultiplier
from tablate.type.type_input import HtmlContainerStylesInput, ColumnStylesInput, TextStylesInput, HtmlFrameStylesInput, \
    HtmlColumnStylesInput, HtmlTextStylesInput
from tablate.type.type_store import FrameDictList


def concat(frame_list: List[TablateUnion],
           container_border: ContainerBorder = None,
           container_padding: ContainerPadding = None,
           container_width: ContainerWidth = None,

           frame_divider: FrameDivider = None,
           background: Background = None,
           background_padding: BackgroundPadding = None,

           html_px_multiplier: HtmlPxMultiplier = None,
           html_container_styles: HtmlContainerStylesInput = None,

           column_styles: ColumnStylesInput = None,
           text_styles: TextStylesInput = None,

           html_frame_styles: HtmlFrameStylesInput = None,

           html_column_styles: HtmlColumnStylesInput = None,
           html_text_styles: HtmlTextStylesInput = None):
    """
    Merge a list of Tablate container instances into a new Tablate container instance. (Useful for IPython environment.)

    Args:
        frame_list: A list of Tablate container instances.
        container_border: outer border style for the Tablate container instance.
            [default: 'thick']
        container_padding: outer padding (in Unicode character width) for the Tablate container instance.
            [default: 1]
        container_width: outer width (in Unicode character width) for the Tablate container instance.
            [default: 120 or terminal width]
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

    Returns: A new TablateSet instance.

    """
    input_dict_list: List[FrameDictList] = []

    for frame_set in frame_list:
        input_dict_list.append(deepcopy(frame_set._frame_list))

    args = deepcopy(locals())

    args["frame_list"] = input_dict_list
    del args["input_dict_list"]
    del args["frame_set"]

    return TablateSet(**args)

# todo: this needs to have process frame applied (probably in TabletSet)
