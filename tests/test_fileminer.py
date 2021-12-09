import pytest
from fileminer.fileminer import rename, copy, dig_rename, dig_copy

from os import listdir
from os.path import isfile, join


# def test_something_else(self, tmp_path):
#    # create a file "myfile" in "mydir" in temp directory
#    f1 = tmp_path / "mydir/myfile"
#    f1.parent.mkdir()  # create a directory "mydir" in temp folder (which is the parent directory of "myfile"
#    f1.touch()  # create a file "myfile" in "mydir"
#    # write to file as normal
#    f1.write_text("text to myfile")
#    assert f1.read() == "text to myfile"


class TestRename(object):

    def test_one_file_with_good_type_is_renamed_and_one_other_file_is_not(self, tmp_path):
        # Create temp directory
        d1 = tmp_path / "mydir"
        d1.mkdir()
        # Create temp .txt file and .csv file
        filename1 = "f1.txt"
        f1 = d1 / f"{filename1}"
        f1.touch()
        filename2 = "f2.csv"
        f2 = d1 / f"{filename2}"
        f2.touch()
        # Rename .txt files
        rename(d1, 'txt')
        # Get the .txt file's new name
        listfiles = [f for f in listdir(d1) if isfile(join(d1, f))]
        newname1 = listfiles[0]
        newname2 = listfiles[1]
        # Assert that there is still two files
        assert len(list(d1.iterdir())) == 2
        # Assert that the new name of f1 is different than before
        assert filename1 != newname1
        # Assert that f2's name is still the same
        assert filename2 == newname2


class TestCopy(object):

    def test_two_files_with_good_type_are_copied_and_one_other_file_is_not(self, tmp_path):
        # Create tmp directory "src" and "dst"
        src = tmp_path / "src"
        src.mkdir()
        dst = tmp_path / "dst"
        dst.mkdir()
        # Create 2 tmp .txt file and one .csv file in "src"
        f1 = src / "f1.txt"
        f1.touch()
        f2 = src / "f2.txt"
        f2.touch()
        f3 = src / "f3.csv"
        f3.touch()
        # Verify number of files in "src" and "dst"
        nb_files_dst1 = len(list(dst.iterdir()))
        # Copy
        copy(src, dst, 'txt')
        # Count number of files in "dst"
        nb_files_dst2 = len(list(dst.iterdir()))
        # assert number of files in "dst" different than before
        assert nb_files_dst1 != nb_files_dst2
        # assert number of files in "dst" is equal to 2
        assert nb_files_dst2 == 2


class TestDigRename(object):

    def test_two_nested_directories_with_a_file_to_rename_and_a_file_to_keep(self, tmp_path):
        # Create 2 temp directories one into the other
        d1 = tmp_path / "d1"
        d1.mkdir()
        d2 = d1 / "d2"
        d2.mkdir()
        # Create temp .txt file and .csv file in d1 and d2
        filename1 = "f1.txt"
        f1 = d1 / f"{filename1}"
        f1.touch()
        filename2 = "f2.csv"
        f2 = d1 / f"{filename2}"
        f2.touch()
        filename3 = "f3.txt"
        f3 = d2 / f"{filename3}"
        f3.touch()
        filename4 = "f4.csv"
        f4 = d2 / f"{filename4}"
        f4.touch()
        # Rename .txt files
        dig_rename(d1, 'txt')
        # Get the .txt file's new name
        listfilesd1 = [f for f in listdir(d1) if isfile(join(d1, f))]
        listfilesd2 = [f for f in listdir(d2) if isfile(join(d2, f))]
        newname1 = listfilesd1[0]
        newname2 = listfilesd1[1]
        newname3 = listfilesd2[1]
        newname4 = listfilesd2[0]
        # Assert that there is still two files in each directory
        assert len(list(d1.iterdir())) == 3
        assert len(list(d2.iterdir())) == 2
        # Assert that the new names of f1 and f3 are different than before
        assert filename1 != newname1
        assert filename3 != newname3
        # Assert that f2 and f4's names are still the same
        assert filename2 == newname2
        assert filename4 == newname4


class TestDigCopy(object):

    def test_two_nested_dir_with_one_file_to_copy_and_one_to_not_touch_and_a_third_dst_folder(self, tmp_path):
        # Create 2 temp source directories one into the other
        d1 = tmp_path / "d1"
        d1.mkdir()
        d2 = d1 / "d2"
        d2.mkdir()
        # Create temp .txt file and .csv file in d1 and d2
        filename1 = "f1.txt"
        f1 = d1 / f"{filename1}"
        f1.touch()
        filename2 = "f2.csv"
        f2 = d1 / f"{filename2}"
        f2.touch()
        filename3 = "f3.txt"
        f3 = d2 / f"{filename3}"
        f3.touch()
        filename4 = "f4.csv"
        f4 = d2 / f"{filename4}"
        f4.touch()
        #Create dst folder and verify it is empty
        d3 = tmp_path / 'd3'
        d3.mkdir()
        # Copy .txt files from d1 and nested d2
        dig_copy(d1, d3, 'txt')
        # Get the new content of d3
        listfilesd3 = [f for f in listdir(d3) if isfile(join(d3, f))]
        print(listfilesd3)
        #Assert d3 changed with dig_copy with 2 new files
        assert len(listfilesd3) == 2

        # Assert that the new files in d3 are the same .txt as d1 and d2
        assert filename1 == listfilesd3[0]
        assert filename3 == listfilesd3[1]
