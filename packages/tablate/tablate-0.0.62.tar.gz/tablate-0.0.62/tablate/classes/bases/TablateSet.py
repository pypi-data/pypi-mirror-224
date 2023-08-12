from copy import deepcopy
from typing import List

from tablate.classes.bases.TablateApiSet import TablateApiSet
from tablate.library.calcs.gen_frame_name import gen_frame_name
from tablate.type.primitives import ContainerBorder, ContainerPadding, ContainerWidth, FrameDivider, Background, BackgroundPadding, \
    HtmlPxMultiplier
from tablate.type.type_input import HtmlContainerStylesInput, ColumnStylesInput, TextStylesInput, HtmlFrameStylesInput, \
    HtmlColumnStylesInput, HtmlTextStylesInput
from tablate.type.type_store import FrameDictList


class TablateSet(TablateApiSet):

    def __init__(self,
                 frame_list: List[FrameDictList],
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

        super().__init__(container_border=container_border,
                         container_padding=container_padding,
                         container_width=container_width,
                         frame_divider=frame_divider,
                         background=background,
                         background_padding=background_padding,
                         html_px_multiplier=html_px_multiplier,
                         html_container_styles=html_container_styles,
                         column_styles=column_styles,
                         text_styles=text_styles,
                         html_frame_styles=html_frame_styles,
                         html_column_styles=html_column_styles,
                         html_text_styles=html_text_styles)

        for frame_set in frame_list:
            for frame_key, frame_item in frame_set.items():
                name = gen_frame_name(name=frame_key, type=frame_item.type, frame_dict=self._frame_list, ensure_unique=True)
                frame_item.name = name
                frame_item.args["name"] = name
                self._frame_list[name] = deepcopy(frame_item)
