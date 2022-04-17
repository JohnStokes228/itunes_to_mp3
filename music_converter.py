"""
Code to convert m4a filetype into mp3, and save it in a sensible, respectable manner.

TODO: - fill in the empty functions
"""
import os
from typing import List


class MusicConverter:

    def __init__(
        self,
        relative_path: str,
        target_path: str,
        folders_list: List[str],
    ) -> None:
        """Initialise class attributes

        Parameters
        ----------
        relative_path : Path to iTunes music folder where all the bastard files live.
        target_path : Path to desired folder to save mp3 files into.
        folders_list : List of files and where they're stored lad.
        """
        self.relative_path = relative_path
        self.target_path = target_path
        self.folders_list = folders_list

    def convert_files(self):
        """The bit that actually converts the damn files.
        """
        pass

    def m4a_to_mp3(
        self,
        filename: str,
    ):
        """Convert a file from m4a to mp3 format, saving it to the destined folder

        Parameters
        ----------
        filename : Full file name of target m4a file.
        """
        pass

    @staticmethod
    def remove_m4a_file(filename: str):
        """Recycle the m4a file to avoid duplicate files eating memory on the machine.

        Possibly might maybe just outright delete this shitty function and do this as the last step of the duplication
        process anywho.

        Parameters
        ----------
        filename : Full name of target m4a file.
        """
        os.remove(filename)
