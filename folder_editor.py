"""
Code for handling folder replication process for the bois. split out to be parent class just because it was hard to
read else wise, might just have this as a separate object entirely rather than parent? who's to be sure...
"""
import os
from typing import List


class FolderEditor:

    def __init__(
        self,
        relative_path: str,
        target_path: str,
    ):
        """Initialise class attributes

        Parameters
        ----------
        relative_path : Path to iTunes music folder where all the bastard files live.
        target_path : Path to desired folder to save mp3 files into
        """
        self.relative_path = relative_path
        self.target_path = target_path
        self.files_list = []  # set up dummy var

    def get_repeat_folder_structure(self) -> List[str]:
        """Get the folder structure in the itunes folder and replicate it in the target destination.

        Returns
        -------
        List[str]
            Fantastic list of files and where to find them.
        """
        self.get_folder_structure()
        self.repeat_folder_structure()

        return self.files_list

    def repeat_folder_structure(self) -> None:
        """Repeat the folder structure found in the itunes folder in the target destination.

        Notes
        -----
        Forced to use ch(92) as f strings for some reason don't allow backslashes lol - this bit of the code is just
        used to ensure the repeated folder structure does not include folders that are the names of the m4a files.
        """
        [os.makedirs(f"{self.target_path}/{folder_path.rsplit(chr(92), 1)[0]}", exist_ok=True)
         for folder_path in self.files_list]

    def get_folder_structure(self) -> None:
        """Create a list of all files in some structure

        Notes
        -----
        Maybe it should be more of a dictionary than a list...?
        """
        for root, dirs, file_names in os.walk(self.relative_path):
            for file in file_names:
                if ".m4a" in file:
                    self.files_list.append(os.path.join(root, file).replace(self.relative_path, ""))
