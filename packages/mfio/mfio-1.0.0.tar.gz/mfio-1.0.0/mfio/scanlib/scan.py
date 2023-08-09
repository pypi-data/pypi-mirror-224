# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       yunhgu
# Date:         2023/8/3
# -------------------------------------------------------------------------------
import os
from pathlib import Path


class Scan:
    """
    文件检索
    """

    _file_dic = {}

    def __init__(self, path, suffixs: list = None) -> None:
        """_summary_

        Args:
            path: 文件路径
            suffixs: 文件后缀,['.png','.json']. Defaults to None.
        """
        self._path = path
        self._suffixs = suffixs

    @property
    def path(self):
        return self._path

    @property
    def suffixs(self):
        return self._suffixs

    @property
    def files(self):
        return self._file_dic

    @staticmethod
    def parent_name(file_path, parent_num=2):
        file_path = Path(file_path)
        return f"{'/'.join(file_path.parts[-parent_num:-1])}/{file_path.stem}"

    @classmethod
    def scan_files(cls, path, suffixs: list = None, parent_num: int = 2):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = Path(os.path.join(root, file))
                cls._file_dic.setdefault(file_path.suffix, {})
                cls._file_dic[file_path.suffix][cls.parent_name(file_path, parent_num)] = file_path
        return cls(path, suffixs)

    @classmethod
    def match_file(cls, file, suffix):
        return cls._file_dic.get(suffix, {}).get(cls.parent_name(file))
