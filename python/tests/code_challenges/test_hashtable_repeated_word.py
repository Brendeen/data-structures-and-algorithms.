import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word
# from code_challenges.hashtable_repeated_word import first_repeated_word
#
#
# @pytest.mark.skip("TODO")
# def test_blank():
#     actual = first_repeated_word("")
#     expected = None
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_no_repeat():
#     actual = first_repeated_word("nobody here but us chickens")
#     expected = None
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_a_a():
#     actual = first_repeated_word("apple apple")
#     expected = "apple"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_a_b_a():
#     actual = first_repeated_word("apple banana apple")
#     expected = "apple"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_a_b_a_b():
#     actual = first_repeated_word("apple banana apple banana")
#     expected = "apple"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_a_b_b_a():
#     actual = first_repeated_word("apple banana banana apple")
#     expected = "banana"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_ignore_case():
#     actual = first_repeated_word("apple banana BANANA apple")
#     expected = "banana"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_ignore_case_flipped():
#     actual = first_repeated_word("apple BANANA banana apple")
#     expected = "banana"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_punctuation():
#     actual = first_repeated_word("apple? BANANA! banana, apple.")
#     expected = "banana"
#     assert actual == expected
#
#
# @pytest.mark.skip("TODO")
# def test_punctuation_joins():
#     txt = """
#   apple
#   apple.apple-apple
#   banana
#   apple?apple
#   banana
#   """
#
#     actual = first_repeated_word(txt)
#     expected = "banana"
#     assert actual == expected

import pytest

def test_first_repeated_word():
    # Test case with a repeated word
    string1 = "Bruh Bruh"
    assert first_repeated_word(string1) == "Bruh"

    # Test case with no repeated words
    string2 = "Hello World"
    assert first_repeated_word(string2) == False

    # Test case with an empty string
    string3 = ""
    assert first_repeated_word(string3) == False

    # Test case with a single word
    string4 = "Hello"
    assert first_repeated_word(string4) == False

    # Test case with multiple repeated words
    string5 = "Python is awesome Python is fun"
    assert first_repeated_word(string5) == "Python"

    # Test case with punctuation and case sensitivity
    string6 = "Hello, hello, world"
    assert first_repeated_word(string6) == "hello"


