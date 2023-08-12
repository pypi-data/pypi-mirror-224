from tablate.library.ascii.chars.line_v import v_line
from tablate.library.ascii.chars.matrix_side import left_side_matrix, right_side_matrix
from tablate.type.primitives import FrameDivider
from tablate.type.type_global import Globals


def row_outer_border(row_string: str, global_options: Globals, row_divider: FrameDivider = None) -> str:

    container_padding = global_options.console.outer_styles.container_padding
    container_border = global_options.console.outer_styles.container_border

    left_border = left_side_matrix[container_border][row_divider] if row_divider else v_line[container_border]
    right_border = right_side_matrix[container_border][row_divider] if row_divider else v_line[container_border]

    grid_line_inner = f"{left_border}{row_string}{right_border}"
    return_string = f"{' ' * container_padding}{grid_line_inner}\n"

    return return_string
