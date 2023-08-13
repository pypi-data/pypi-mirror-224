from tablate.library.checkers.set_key_resolver import set_key_resolver
from tablate.type.type_input import HtmlContainerStylesInput
from tablate.type.type_style import HtmlContainerStyles


def html_outer_input_to_style(html_container_styles_input: HtmlContainerStylesInput) -> HtmlContainerStyles:

    html_container_styles_input = html_container_styles_input if html_container_styles_input is not None else {}

    html_container_border_weight = set_key_resolver(instance=html_container_styles_input, key="html_frame_divider_style", default=None)
    html_container_border_style = set_key_resolver(instance=html_container_styles_input, key="html_container_border_style", default=None)
    html_container_border_color = set_key_resolver(instance=html_container_styles_input, key="html_container_border_color", default=None)
    html_container_padding = set_key_resolver(instance=html_container_styles_input, key="html_container_padding", default=None)
    html_container_width = set_key_resolver(instance=html_container_styles_input, key="html_container_width", default=None)
    html_px_multiplier = set_key_resolver(instance=html_container_styles_input, key="html_px_multiplier", default=None)
    html_default_colors = set_key_resolver(instance=html_container_styles_input, key="html_default_colors", default=None)

    return HtmlContainerStyles(
        html_container_border_weight=html_container_border_weight,
        html_container_border_style=html_container_border_style,
        html_container_border_color=html_container_border_color,
        html_container_padding=html_container_padding,
        html_container_width=html_container_width,
        html_px_multiplier=html_px_multiplier,
        html_default_colors=html_default_colors
    )