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


Tablate = import_module('tablate.api.Tablate')
Text = import_module('tablate.api.modules.Text')
Grid = import_module('tablate.api.modules.Grid')
Table = import_module('tablate.api.modules.Table')
concat = import_module('tablate.api.functions.concat')



# from tablate.type.type_input import HtmlOuterStylesInput, FrameStylesInput, HtmlFrameStylesInput, ColumnStylesInput, \
#     TextStylesInput, HtmlColumnStylesInput, HtmlTextStylesInput, RowsStylesInput, HtmlRowsStylesInput, \
#     HtmlColumnInput, BaseColumnInput, GridColumnInput, TableColumnInput, TableRowsInput, BaseStylesInput, \
#     TableHeaderFrameStylesInput, TableBodyFrameStylesInput, HtmlStylesInput, HtmlTextFrameStylesInput, \
#     HtmlGridStylesInput, HtmlTableStylesInput, HtmlTableHeaderStylesInput, HtmlTableBodyStylesInput

########################################################################################################################
########################################################################################################################
########################################################################################################################


# This will import the modules without causing a circular import error.

try:
    __version__ = version('tablate')
except ModuleNotFoundError:
    pass
