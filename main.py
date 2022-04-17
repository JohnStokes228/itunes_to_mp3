"""
Code to convert m4a filetype into mp3, and save it in a sensible, respectable manner.

TODO: - Possibly will need to replace 'list_of_files' with a dictionary...? My thoughts are like, maybe it would be good
        to send each album separately to the converter so it can be to some extent parallelized? that would be like
        maybe on some level easier if it were a dict? I dunno I guess we'll bloody see for ourselves soon
      - fill in the empty functions
"""
import os
from typing import (
    Optional,
    List,
)
from params import (
    RELATIVE_PATH,
    TARGET_PATH,
)


class MusicConverter:

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
        self._files_list = []  # set up dummy var

    @property
    def files_list(self) -> Optional[List[str]]:
        """Getter for files_list attribute, so the errors work as desired.
        """
        if not self._files_list:
            raise AttributeError("Found no Files to convert")  # is this really an AttributeError here?
        return self._files_list

    @files_list.setter
    def files_list(
        self,
        list_of_files: List[str],
    ):
        """Set files_list attribute to given value.

        Parameters
        ----------
        list_of_files : some kind of list to set list_of_files to.
        """
        if type(list_of_files) != list:
            raise TypeError("Files list is not a list, what?")
        self._files_list = list_of_files

    def convert_files(self):
        """The bit that actually converts the damn files.
        """
        pass

    def get_repeat_folder_structure(self) -> None:
        """Get the folder structure in the itunes folder and replicate it in the target destination.
        """
        self.get_folder_structure()
        self.repeat_folder_structure()

    def repeat_folder_structure(self) -> None:
        """Repeat the folder structure found in the itunes folder in the target destination.

        Notes
        -----
        Forced to use ch(92) as f strings for some reason don't allow backslashes lol - this bit of the code is just
        used to ensure the repeated folder structure does not include folders that are the names of the m4a files.
        """
        [os.makedirs(f"{self.target_path}/{folder_path.rsplit(chr(92), 1)}", exist_ok=True)
         for folder_path in self.files_list]

    def get_folder_structure(self) -> None:
        """Create a list of all files in some structure

        Notes
        -----
        Maybe it should be more of a dictionary than a list...?
        """
        for root, dirs, file_names in os.walk(self.relative_path):
            for file in file_names:
                self.files_list.append(os.path.join(root, file).replace(RELATIVE_PATH, ""))

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

    def remove_m4a_file(
        self,
        filename: str,
    ):
        """Recycle the m4a file to avoid duplicate files eating memory on the machine.

        Parameters
        ----------
        filename : Full name of target m4a file.
        """
        pass


if __name__ == "__main__":
    MusicConverter(RELATIVE_PATH, TARGET_PATH).convert_files()
