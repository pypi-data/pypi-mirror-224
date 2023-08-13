from shutil import get_terminal_size

from tablate.type.primitives import Colors, TextAlign, TextStyle, TextColor, HeaderAlignment, ContainerBorder, \
    ColumnDivider, HeaderColumnDivider, HideHeader, ColumnWidth, ColumnPadding, Background, FrameDivider, \
    MaxLines, Multiline, TruncValue, ContainerPadding, ContainerWidth, HtmlTextStyle, HtmlTextAlign, \
    HtmlTextColor, HtmlTextSize, HtmlColumnDividerStyle, HtmlColumnPadding, HtmlBackground, \
    HtmlFrameDivider, HtmlPxMultiplier, HtmlContainerBorder, HtmlContainerPadding, HtmlContainerWidth, FrameName, HtmlColumnWidth, \
    HtmlDefaultColors, HtmlDividerWeight

global_text_align_default: TextAlign = None
global_text_style_default: TextStyle = None
global_multiline_default: Multiline = None

############################################################################################

frame_name_default: FrameName = ""

colors_default: Colors = None

text_align_default: TextAlign = "left"
text_style_default: TextStyle = "normal"
text_color_default: TextColor = None

container_padding_default: ContainerPadding = 1
container_width_default: ContainerWidth = get_terminal_size((120 + (container_padding_default * 2), 0))[0] - (container_padding_default * 2)

container_border_default: ContainerBorder = "thick"
frame_divider_default: FrameDivider = "thick"
column_divider_default: ColumnDivider = "thin"

html_default_colors_default: HtmlDefaultColors = True

column_width_default: ColumnWidth = None
column_padding_default: ColumnPadding = 1
background_default: Background = None
background_padding_default = 1

max_lines_default: MaxLines = None
multiline_default: Multiline = True
trunc_value_default: TruncValue = "..."

############################################################################################

header_base_divider_default = "thin"

table_multiline_default: Multiline = False

table_header_text_style_default: TextStyle = "bold"
table_header_text_align_default: HeaderAlignment = "column"
table_header_column_divider_default: HeaderColumnDivider = "rows"

row_line_divider_default: FrameDivider = "thin"

hide_header_default: HideHeader = False

############################################################################################

html_padding_default = 6
html_divider_weight_default = 1
html_divider_color_default = 'black'
html_px_multiplier_default: HtmlPxMultiplier = 1
html_background_default: HtmlBackground = background_default

html_container_width_default: HtmlContainerWidth = "100%"
html_container_border_default: HtmlContainerBorder = container_border_default
html_container_padding_default: HtmlContainerPadding = html_padding_default

html_frame_divider_default: HtmlFrameDivider = frame_divider_default

html_column_width_default: HtmlColumnWidth = None
html_column_divider_style_default: HtmlColumnDividerStyle = column_divider_default
html_column_divider_weight_default: HtmlDividerWeight = html_divider_weight_default
html_column_padding_default: HtmlColumnPadding = column_padding_default

html_text_style_default: HtmlTextStyle = text_style_default
html_text_align_default: HtmlTextAlign = text_align_default
html_text_color_default: HtmlTextColor = text_color_default
html_text_size_default = 16

html_max_lines_default: MaxLines = max_lines_default
html_multiline_default: Multiline = multiline_default

html_row_line_divider_style_default: HtmlFrameDivider = row_line_divider_default
