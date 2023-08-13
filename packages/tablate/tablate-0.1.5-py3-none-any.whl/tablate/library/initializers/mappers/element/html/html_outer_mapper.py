from tablate.library.checkers.set_attr_resolver import set_attr_resolver
from tablate.type.defaults import html_container_width_default, html_px_multiplier_default, container_border_default, \
    container_padding_default, html_divider_weight_default, html_padding_default, \
    html_default_colors_default, html_divider_color_default
from tablate.type.primitives import HtmlPxMultiplier, HtmlDefaultColors
from tablate.type.type_style import HtmlContainerStyles, OuterStyles


def html_outer_mapper(html_outer_input: HtmlContainerStyles = None,
                      html_outer_defaults: HtmlContainerStyles = None,
                      base_outer_defaults: OuterStyles = None,
                      html_default_colors: HtmlDefaultColors = None,
                      html_px_multiplier: HtmlPxMultiplier = html_px_multiplier_default) -> HtmlContainerStyles:
    html_container_border_weight = set_attr_resolver(
        instance=html_outer_input,
        attr="html_container_border_weight",
        default=set_attr_resolver(
            instance=html_outer_defaults,
            attr="html_container_border_weight",
            default=html_divider_weight_default))
    html_container_border_style = set_attr_resolver(
        instance=html_outer_input,
        attr="html_container_border_style",
        default=set_attr_resolver(
            instance=html_outer_defaults,
            attr="html_container_border_style",
            default=set_attr_resolver(
                instance=base_outer_defaults,
                attr="container_border",
                default=container_border_default)))
    html_container_border_color = set_attr_resolver(
        instance=html_outer_input,
        attr="html_container_border_color",
        default=set_attr_resolver(
            instance=html_outer_defaults,
            attr="html_container_border_color",
            default=html_divider_color_default))
    html_container_padding = set_attr_resolver(
        instance=html_outer_input,
        attr="html_container_padding",
        default=set_attr_resolver(
            instance=html_outer_defaults,
            attr="html_container_padding",
            default=set_attr_resolver(
                instance=base_outer_defaults,
                attr="container_padding",
                default=container_padding_default) * html_padding_default))
    html_container_width = set_attr_resolver(
        instance=html_outer_input,
        attr="html_container_width",
        default=set_attr_resolver(
            instance=html_outer_defaults,
            attr="html_container_width",
            default=html_container_width_default))
    html_default_colors = set_attr_resolver(
        instance=html_outer_input,
        attr="html_default_colors",
        default=html_default_colors if html_default_colors is not None else html_default_colors_default)

    html_outer_return = HtmlContainerStyles(html_container_border_weight=html_container_border_weight,
                                        html_container_border_style=html_container_border_style,
                                        html_container_border_color=html_container_border_color,
                                        html_container_padding=html_container_padding,
                                        html_container_width=html_container_width,
                                        html_px_multiplier=html_px_multiplier,
                                        html_default_colors=html_default_colors)

    return html_outer_return
