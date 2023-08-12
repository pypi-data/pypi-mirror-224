from tablate.classes.bases.TablateApiBase import TablateApiBase


class TablateApiItem(TablateApiBase):

    @property
    def name(self):
        """

        Returns: The name of the frame.

        """
        return list(self._frame_list.items())[0]

    @name.setter
    def name(self, name: str):
        self.rename(name)

    def rename(self, new_name: str):
        """
        Renames the frame.
        Args:
            new_name: The new name set on the frame.
        """
        if new_name is not None:
            frame_key, frame_item = list(self._frame_list.items())[0]
            frame_item.name = new_name
            self._frame_list[new_name] = frame_item
            del self._frame_list[frame_key]

    def to_dict(self):
        """

        Returns: A Pandas compatible dict.

        """
        frame_key, frame_item = list(self._frame_list.items())[0]
        if frame_item.type == "text":
            return {
                "text": [frame_item.args["text"]]
            }
        if frame_item.type == "grid":
            return_dict = {}
            for column_index, column_item in enumerate(frame_item.args["columns"]):
                return_dict[column_index] = [column_item["string"]]
            return return_dict
        if frame_item.type == "table":
            return_dict = {}
            for column_item in frame_item.args["columns"]:
                return_dict[column_item["key"]] = []
                for row_item in frame_item.args["rows"]:
                    return_dict[column_item["key"]].append(row_item[column_item["key"]])
            return return_dict
