import os
import pytest

from words import counter_words


def test_fail_not_exist_file_to_count_words():
    with pytest.raises(FileNotFoundError) as excep_getting:
        counter_words("no_file.txt")
    assert str(excep_getting.value) == "Try again with existent file"


def test_fail_words_not_match_to_count_words():
    with pytest.raises(ValueError) as excep_getting:
        counter_words("wrong_format.txt")
    assert (
        str(excep_getting.value)
        == "The number of words does not match the one indicated in the file"
    )


def test_succes_count_words():
    counter_words("words.txt")
    created_file = open(
        os.path.dirname(__file__) + "/words_counted.txt", "r", encoding="utf-8"
    )
    words = created_file.readlines()

    assert int(words[0]) == 3
    assert words[1] == "2 1 1 "
