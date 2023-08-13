from copy import deepcopy
from typing import Union

from tablate.classes.bases.TablateApiBase import TablateApiBase
from tablate.classes.classes import TablateUnion
from tablate.classes.helpers.get_frame import get_frame
from tablate.classes.helpers.list_frame import list_frames
from tablate.library.calcs.gen_frame_name import gen_frame_name


class TablateApiSet(TablateApiBase):

    def list_frames(self):
        """
        List the frames in the Tablate container instance with some details about each frame.
        """
        list_frames(self._frame_list, self._globals_store.store)

    def get_frame(self, selector: Union[int, str], apply_globals: bool = False):
        """
        Gets a frame from the Tablate container instance and returns it as a TablateItem.
        Args:
            selector: The index or name of the frame to select.
            apply_globals: Whether to apply the global defaults and container styles to the returned TablateItem.

        Returns:

        """
        if apply_globals:
            return deepcopy(get_frame(frame_list=self._frame_list, selector=selector, global_options=self._globals_store.args))
        else:
            return deepcopy(get_frame(frame_list=self._frame_list, selector=selector))

    def remove_frame(self, selector: Union[int, str]):
        """
        Deletes a frame.
        Args:
            selector: The index or name of the frame to delete.
        """
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if (type(selector) == int and selector == frame_index) or (type(selector) == str and selector == frame_key):
                del self._frame_list[frame_key]
                break

    def replace_frame(self, selector: Union[int, str], new_frame: TablateUnion, new_name: str = None):
        """
        Replaces a frame with another frame.
        Args:
            selector: The index or name of the frame to replace.
            new_frame: A Tablate Container instance to replace the frame with (if more than one frame in the Tablate container instance, only the first frame will be used).
            new_name: (Optional) The new name of the frame.
        """
        new_frame = deepcopy(new_frame)
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if (type(selector) == int and selector == frame_index) or (type(selector) == str and selector == frame_key):
                new_frame_key, new_frame_item = list(new_frame._frame_list.items())[0]
                new_name = new_name if new_name is not None else new_frame_key
                new_name = gen_frame_name(name=new_name, type=new_frame_item.type, frame_dict=self._frame_list, ensure_unique=True)
                new_frame_item.name = new_name
                new_frame_item.args["name"] = new_name
                self._frame_list = {key if key != frame_key else new_name: value for key, value in self._frame_list.items()}
                self._frame_list[new_name] = new_frame_item

    def rename_frame(self, selector: Union[int, str], new_name: str):
        """
        Renames a frame.
        Args:
            selector: The index or name of the frame to rename.
            new_name: The new name to apply to the frame.
        """
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if (type(selector) == int and selector == frame_index) or (type(selector) == str and selector == frame_key):
                self._frame_list = {key if key != frame_key else new_name: value for key, value in self._frame_list.items()}
                break

    def move_frame(self, from_selector: Union[int, str], to_index: int):
        """
        Move a frame within a Tablate container instance to a new index.
        Args:
            from_selector: The index or name of the frame to move.
            to_index: The index to which the selected frame should be moved.
        """
        selected_frame = get_frame(frame_list=self._frame_list, selector=from_selector, global_options=self._globals_store.args).name[1]
        new_frame_list = {}
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if to_index == frame_index and selected_frame is not None:
                new_frame_list[selected_frame.name] = selected_frame
            if (type(from_selector) == int and from_selector == frame_index) or (type(from_selector) == str and from_selector == frame_key):
                to_index += 1
            else:
                new_frame_list[frame_key] = frame_item
        self._frame_list = new_frame_list

    def insert_frame(self, insert_index: int, new_frame: TablateUnion, new_name: str = None):
        """
        Insert a frame into a Tablate container instance at a specified index.
        Args:
            insert_index: The index at which the new frame should be inserted.
            new_frame: The Tablate container instance to insert.
            new_name: (Optional) The name to apply to the inserted frame.
        """
        new_frame = deepcopy(new_frame)
        new_frame_list = {}
        for frame_index, (frame_key, frame_item) in enumerate(self._frame_list.items()):
            if insert_index == frame_index:
                new_frame_key, new_frame_item = list(new_frame._frame_list.items())[0]
                new_name = new_name if new_name is not None else new_frame_key
                new_name = gen_frame_name(name=new_name, type=new_frame_item.type, frame_dict=self._frame_list, ensure_unique=True)
                new_frame_item.name = new_name
                new_frame_item.args["name"] = new_name
                new_frame_list[new_name] = new_frame_item
            new_frame_list[frame_key] = frame_item
        self._frame_list = new_frame_list


