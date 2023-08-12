from copy import copy, deepcopy
from typing import Callable, Tuple
from tablate.classes.bases.TablateBase import TablateBase
from tablate.library.initializers.processors.process_frame import process_frame_args
from tablate.library.initializers.globals_init import globals_init
from tablate.library.renderers.console.render_console import render_console
from tablate.library.renderers.html.render_html import render_html

from tablate.type.primitives import ContainerBorder, FrameDivider, ContainerWidth, ContainerPadding, Background, HtmlPxMultiplier, \
    BackgroundPadding, HtmlDefaultColors, FrameName, FrameType, GlobalArgs, FrameArgs
from tablate.type.type_global import GlobalsStore
from tablate.type.type_input import HtmlContainerStylesInput, ColumnStylesInput, TextStylesInput, \
    HtmlFrameStylesInput, HtmlColumnStylesInput, HtmlTextStylesInput
from tablate.type.type_store import FrameDict


class TablateApiBase(TablateBase):

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

        args = copy(locals())
        del args["self"]

        self._globals_store = GlobalsStore(args=args, store=globals_init(**args))
        self._css_injection = []
        self._frame_list = {}

    def apply(self, function: Callable[[FrameName, FrameType, FrameArgs, GlobalArgs], Tuple[FrameArgs, GlobalArgs]],
              raise_merge_error: bool = True):
        """
        Iterates over frame items and calls the passed function for on each iteration. Optionally, if the functions returns a valid frame options dict or global options dicts, these will be set to the internal store. If there is an error, trying to set the return objects, the `.apply()` method will break and reset the internal stores.

        Note:
            As a rule of thumb, the return objects should have the same form as the third (frame options) and forth (global options) arguments passed to the `.apply()` method.

        Args:
            function: A function called for each frame element. The function accepts four arguments: the frame type, the frame name, the frame options and the global options. The function may return a tuple containing the frame options and the global options. Tablate will attempt to apply the return values, if set, to its internal frame store and the global options store.
            raise_merge_error: If set to True, the apply function will raise an
        """
        frame_list_copy = deepcopy(self._frame_list)
        global_options_copy = deepcopy(self._globals_store)
        for frame_copy_key, frame_copy_item in frame_list_copy.items():
            try:
                return_result = function(frame_copy_key,
                                         frame_copy_item.type,
                                         deepcopy(frame_copy_item.args),
                                         deepcopy(global_options_copy.args))
                if return_result is not None:
                    return_frame_dict, return_global_dict = return_result
                    if global_options_copy is not None:
                        self._globals_store = GlobalsStore(args=return_global_dict,
                                                           store=globals_init(**return_global_dict))
                    if return_frame_dict is not None:
                        self._frame_list[return_frame_dict["name"]] = FrameDict(name=return_frame_dict["name"],
                                                                                type=frame_copy_item.type,
                                                                                args=return_frame_dict,
                                                                                store=process_frame_args(
                                                                                    frame_args=return_global_dict,
                                                                                    frame_type=frame_copy_item.type,
                                                                                    global_options=self._globals_store.store))

            except Exception as e:
                self._frame_list = frame_list_copy
                self._globals_store = global_options_copy
                if raise_merge_error:
                    raise Exception(f"Error merging result of apply on item: {frame_copy_key}.\n\t{e}")

    def apply_style(self, selector: str, css: str, sub_selector: str = None):
        """
        Applies custom CSS styling to the Tablate container instance. CSS stylings are scoped to the specific Tablate container instance.

        Args:
            selector: The HTML classnames within the Tablate container instance.
            css: The CSS style to be set (for instance: background-color: #FFFFFF).
            sub_selector: An additional selector appended immediately after the main selector block.
        """
        self._css_injection.append({"selector": selector, "css": css, "sub_selector": sub_selector})

    # @functools.cache
    def to_string(self) -> str:
        """
        Generates an ASCII rendering of the Tablate container instance.

        Returns: An ASCII rendering of the Tablate container instance.

        """
        return render_console(frame_list=self._frame_list, global_options=self._globals_store.store)

    # @functools.cache
    def print(self) -> None:
        """
        Prints an ASCII rendering of the Tablate container instance.
        """
        print(self.to_string())

    # @functools.cache
    def __str__(self) -> str:
        """

        Returns: An ASCII rendering of the Tablate container instance.

        """
        return self.to_string()

    # @functools.cache
    def to_html(self) -> str:
        """
        Generates an HTML rendering of the Tablate container instance.

        Returns: An HTML rendering of the Tablate container instance.

        """
        return render_html(frame_list=self._frame_list, global_options=self._globals_store.store,
                           css_injection=self._css_injection)

    # @functools.cache
    def _repr_html_(self) -> str:
        """

        Returns: An HTML rendering of the Tablate container instance.

        """
        return self.to_html()

    def __repr__(self) -> str:
        """

        Returns: A string to represent the Tablate container instance.

        """
        return f"Tablate ({len(list(self._frame_list.items()))} frame items)"
