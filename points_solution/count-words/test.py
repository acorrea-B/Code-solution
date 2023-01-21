import os
import pytest

from count_words import count_words


def test_fail_not_exist_file_to_count_words():
    with pytest.raises(FileNotFoundError) as exec:
        count_words("no_file.txt")
    assert str(exec.value) == "Try again with existent file"


def test_fail_words_not_match_to_count_words():
    with pytest.raises(ValueError) as exec:
        count_words("wrong_format.txt")
    assert (
        str(exec.value)
        == "The number of words does not match the one indicated in the file"
    )


def test_succes_count_words():
    count_words("words.txt")
    created_file = open(os.path.dirname(__file__) + "/words_counted.txt", "r")
    words = created_file.readlines()

    assert int(words[0]) == 3
    assert words[1] == "2 1 1 "
