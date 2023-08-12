from __future__ import annotations

import sys
from importlib.metadata import version
import importlib

def import_module(module_name):
  """Imports a module without causing a circular import error."""
  if module_name in sys.modules:
    return sys.modules[module_name]

  module = importlib.import_module(module_name)
  sys.modules[module_name] = module

  return module


tablate_module = import_module('tablate.api.Tablate')
text_modules = import_module('tablate.api.modules.Text')
grid_module = import_module('tablate.api.modules.Grid')
table_module = import_module('tablate.api.modules.Table')

concat_module = import_module('tablate.api.functions.concat')

Tablate = tablate_module.Tablate
Text = text_modules.Text
Grid = grid_module.Grid
Table = table_module.Table
concat = concat_module.concat

from tablate.type.type_input import HtmlContainerStylesInput, FrameStylesInput, HtmlFrameStylesInput, ColumnStylesInput, \
    TextStylesInput, HtmlColumnStylesInput, HtmlTextStylesInput, RowsStylesInput, HtmlRowsStylesInput, \
    HtmlColumnInput, BaseColumnInput, GridColumnInput, TableColumnInput, TableRowsInput, BaseStylesInput, \
    TableHeaderFrameStylesInput, TableBodyFrameStylesInput, HtmlStylesInput, HtmlTextFrameStylesInput, \
    HtmlGridFrameStylesInput, HtmlTableFrameStylesInput, HtmlTableHeaderStylesInput

########################################################################################################################
########################################################################################################################
########################################################################################################################


# This will import the modules without causing a circular import error.

try:
    __version__ = version('tablate')
except ModuleNotFoundError:
    pass
