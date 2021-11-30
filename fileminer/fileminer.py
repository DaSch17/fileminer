"""
Functions to copy files of a certain type from a folder (only it or also its children)
to another folder and rename it

By default the 'rename' functions rename files by adding "[RENAMED]" at the end.
To change the behavior of all 'rename' functions ('rename' and 'dig_rename'), you need
to change only the 'rename' function. Others will call it to work.
"""

import glob
import os
import shutil


# Functions:
def copy(src_fldr, dst_fldr, typefile):
    """Copy files of a certain type from a source folder to a destination folder

    Parameters
    ----------
    src_fldr : raw string (r"")
    source folder

    dst_fldr : raw string (r"")
    destination folder

    typefile : type of the files you want to copy
    (ex. of input: 'mp3')


    Returns
    -------


    """
    typefile = fr'*.{typefile}'
    for path_and_filename in glob.iglob(os.path.join(src_fldr, typefile)):
        shutil.copy2(path_and_filename, dst_fldr)


def rename(fldr, typefile):
    """Rename files of a certain type from a input folder
    By default the 'rename' functions rename files by keeping only the 3 first characters

    Parameters
    ----------
    fldr : Folder where the files will be renamed

    typefile : Type of the files who will be renamed
    (ex. of input: 'mp3')

    Returns
    -------


    """
    typefile = fr'*.{typefile}'
    for path_and_filename in glob.iglob(os.path.join(fldr, typefile)):
        title, ext = os.path.splitext(os.path.basename(path_and_filename))
        # Where to modify title (aka name of files)
        title = title + "[RENAMED]"
        # End of name's modifications
        os.rename(path_and_filename, os.path.join(fldr, title + ext))


def dig_copy(src_fldr, dst_fldr, typefile):
    """Copy files of a certain type from a source folder and all its children
    to a destination folder.
    Need the 'copy' function to work.

    Parameters
    ----------
    src_fldr : Source folder (all the children folders will be considered)

    dst_fldr : Destination folder

    typefile : type of the files you want to copy
    (ex. of input: 'mp3')

    Returns
    -------


    """
    copy(src_fldr, dst_fldr, typefile)
    for root, dirs, _ in os.walk(src_fldr):
        for name in dirs:
            full_dir_path = os.path.join(root, name)
            copy(full_dir_path, dst_fldr, typefile)


def dig_rename(fldr, typefile):
    """Rename files of a certain type from a input folder and all its children
    By default the 'rename' functions rename files by keeping only the 3 first characters.
    Need the 'rename' function to work.

    Parameters
    ----------
    fldr : Folder where the files will be renamed (all the children folders will be considered)

    typefile : Type of the files that will be renamed
    (ex. of input: 'mp3')

    Returns
    -------

    """
    rename(fldr, typefile)
    for root, dirs, _ in os.walk(fldr):
        for name in dirs:
            full_dir_path = os.path.join(root, name)
            rename(full_dir_path, typefile)
