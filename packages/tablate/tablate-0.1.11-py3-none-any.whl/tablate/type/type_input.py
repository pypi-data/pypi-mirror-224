from typing import TypedDict, Dict, Optional

from tablate.type.primitives import TextString, FrameDivider, ColumnWidth, TextStyle, TextAlign, Background, \
    ColumnPadding, TextColor, ColumnDivider, HtmlDividerWeight, HtmlColumnDividerStyle, HtmlColumnPadding, \
    HtmlTextStyle, HtmlTextAlign, HtmlTextColor, HtmlBackground, BackgroundPadding, HtmlTextSize, MaxLines, \
    Multiline, HtmlFrameDivider, HtmlContainerBorder, HtmlContainerPadding, HtmlContainerWidth, HtmlDividerColor


class HtmlContainerStylesInput(TypedDict, total=False):  # HtmlContainerBase
    html_container_border_weight: HtmlDividerWeight
    html_container_border_style: HtmlContainerBorder
    html_container_border_color: HtmlDividerColor
    html_container_padding: HtmlContainerPadding
    html_container_width: HtmlContainerWidth


########################################################################################################################

class FrameStylesInput(TypedDict, total=False):  # FrameBase
    frame_divider: FrameDivider
    max_lines: MaxLines
    multiline: Multiline
    background: Background


class HtmlFrameStylesInput(TypedDict, total=False):  # HtmlFrameBase
    html_frame_divider_style: HtmlFrameDivider
    html_frame_divider_weight: HtmlDividerWeight
    html_frame_divider_color: HtmlDividerColor
    html_max_lines: MaxLines
    html_multiline: Multiline
    html_background: HtmlBackground


########################################################################################################################

class ColumnStylesInput(TypedDict, total=False):  # ColumnBase
    column_divider: ColumnDivider
    padding: ColumnPadding
    background_padding: BackgroundPadding


class TextStylesInput(TypedDict, total=False):  # TextBase
    text_style: TextStyle
    text_align: TextAlign
    text_color: TextColor


class HtmlColumnStylesInput(TypedDict, total=False):  # HtmlColumnBase
    html_column_divider_style: HtmlColumnDividerStyle
    html_column_divider_weight: HtmlDividerWeight
    html_column_divider_color: HtmlDividerColor
    html_padding: HtmlColumnPadding


class HtmlTextStylesInput(TypedDict, total=False):  # HtmlTextBase
    html_text_style: HtmlTextStyle
    html_text_align: HtmlTextAlign
    html_text_color: HtmlTextColor
    html_text_size: HtmlTextSize

    
class RowsStylesInput(TypedDict, total=False):  # TableRowsBase
    row_line_divider: FrameDivider
    odds_background: Background
    evens_background: Background

    
class HtmlRowsStylesInput(TypedDict, total=False):  # HtmlTableRowsBase
    html_row_line_divider_weight: HtmlDividerWeight
    html_row_line_divider_style: HtmlFrameDivider
    html_row_line_divider_color: HtmlDividerColor
    html_odds_background: HtmlBackground
    html_evens_background: HtmlBackground


########################################################################################################################
########################################################################################################################
########################################################################################################################

class HtmlColumnInput(TypedDict, total=False):
    padding: HtmlColumnPadding
    divider_style: HtmlColumnDividerStyle
    divider_weight: HtmlDividerWeight
    divider_color: HtmlDividerColor
    text_style: HtmlTextStyle
    text_align: HtmlTextAlign
    text_color: HtmlTextColor
    background: HtmlBackground


class BaseColumnInput(TypedDict, total=False):
    width: ColumnWidth
    padding: ColumnPadding
    divider: ColumnDivider
    text_style: TextStyle
    text_align: TextAlign
    text_color: TextColor
    background: Background
    html_styles: Optional[HtmlColumnInput]


class GridColumnInput(BaseColumnInput):
    string: TextString


class BaseTableColumnInput(BaseColumnInput, total=False):
    string: TextString


class TableColumnInput(BaseTableColumnInput):
    key: str


TableRowsInput = Dict[str, TextString]


########################################################################################################################
########################################################################################################################
########################################################################################################################


class BaseStylesInput(TypedDict, total=False):
    frame_styles: FrameStylesInput
    column_styles: ColumnStylesInput
    text_styles: TextStylesInput
#
#
# GridStylesInput = BaseStylesInput
#
#
TableHeaderFrameStylesInput = BaseStylesInput


class TableBodyFrameStylesInput(BaseStylesInput, total=False):
    row_styles: RowsStylesInput


########################################################################################################################


class HtmlStylesInput(TypedDict, total=False):
    html_frame_styles: HtmlFrameStylesInput
    html_column_styles: HtmlColumnStylesInput
    html_text_styles: HtmlTextStylesInput


class HtmlTextFrameStylesInput(TypedDict, total=False):
    html_frame_styles: HtmlFrameStylesInput
    html_text_styles: HtmlTextStylesInput


HtmlGridFrameStylesInput = HtmlStylesInput


class HtmlTableFrameStylesInput(HtmlStylesInput, total=False):
    html_row_styles: HtmlRowsStylesInput


HtmlTableHeaderStylesInput = HtmlStylesInput

# HtmlTableBodyStylesInput = HtmlTableStylesInput

########################################################################################################################
########################################################################################################################
########################################################################################################################

