"""
Code to convert m4a filetype into mp3, and save it in a sensible, respectable manner. This was a right shag to get
working so hopefully it doesnt just break instantly...

TODO: - add a catch to the mp3 conversion for failures
      - log things as this could go horribly wrong
"""
import os
import subprocess
from multiprocessing import Pool
from typing import (
    List,
    Optional,
)


class MusicConverter:

    def __init__(
        self,
        relative_path: str,
        target_path: str,
        files_list: List[str],
    ) -> None:
        """Initialise class attributes

        Parameters
        ----------
        relative_path : Path to iTunes music folder where all the bastard files live.
        target_path : Path to desired folder to save mp3 files into.
        files_list : List of files and where they're stored lad.
        """
        self.relative_path = relative_path
        self.target_path = target_path
        self._files_list = files_list

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
    ) -> None:
        """Set files_list attribute to given value.

        Parameters
        ----------
        list_of_files : some kind of list to set list_of_files to.
        """
        if type(list_of_files) != list:
            raise TypeError("Files list is not a list, what?")
        self._files_list = list_of_files

    def convert_files(self) -> None:
        """Convert the files simultaneously perhaps if it works, but it also might not work so don't get too hyped.

        Notes
        -----
        It runs! but then the subprocess itself requires you to type 'Y' if the file already exists in target folder...
        Suggested fix is to drop file names from files_list if they already exist in the target destination. atm this is
        done in m4a_to_mp3, but I can't help but feel it would be better served to occur prior to being fed to that
        function.
        """
        pool = Pool(4)
        pool.map(self.m4a_to_mp3, self.files_list)

    def m4a_to_mp3(
        self,
        filename: str,
    ) -> None:
        """Convert a file from m4a to mp3 format, saving it to the destined folder before deleting the m4a file.

        Notes
        -----
        Off the back of a stack overflow response I've resorted to subprocess calling ffmpeg because the package doesn't
        work inline for m4a for some reason it seems. This does require ffmpeg to be pointed to in the environmental
        variable 'PATH'.

        Parameters
        ----------
        filename : Full file name of target m4a file.
        """
        filename = filename.replace('.m4a', '')

        if os.path.isfile(f"{self.target_path}/{filename}.mp3"):
            return  # ffmpeg is a bitch about overwriting :(

        subprocess.call(["ffmpeg", "-i", f"{self.relative_path}/{filename}.m4a", f"{self.target_path}/{filename}.mp3"])
        os.remove(f"{self.relative_path}/{filename}.m4a")

        print(f"converted {filename} successfully, bet you wish this was logged rather than printed ey ;)")
