"""
This is the code lad
"""
from params import (
    RELATIVE_PATH,
    TARGET_PATH,
)
from folder_editor import FolderEditor
from music_converter import MusicConverter


if __name__ == "__main__":
    folders_list = FolderEditor(RELATIVE_PATH, TARGET_PATH).get_repeat_folder_structure()
    MusicConverter(RELATIVE_PATH, TARGET_PATH, folders_list).convert_files()
