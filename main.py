"""
This is the code lad. Here. Now.

TODO - maybe log some shit as atm its kind of garbage
"""
import os
from params import (
    RELATIVE_PATH,
    TARGET_PATH,
    FFMPEG_PATH,
)
from folder_editor import FolderEditor
from music_converter import MusicConverter


if __name__ == "__main__":
    if FFMPEG_PATH not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + FFMPEG_PATH  # point to the ffmpeg executable

    folders_list = FolderEditor(RELATIVE_PATH, TARGET_PATH).get_repeat_folder_structure()
    MusicConverter(RELATIVE_PATH, TARGET_PATH, folders_list).convert_files()
