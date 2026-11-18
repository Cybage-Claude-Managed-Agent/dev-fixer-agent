from src.strutils import slugify, truncate, word_count


def test_slugify():
    assert slugify("Hello World") == "hello-world"


def test_slugify_punctuation():  # TST-5
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("Release 2 notes") == "release-2-notes"
    assert slugify("  -- Hello -- World --  ") == "hello-world"


def test_truncate():
    assert truncate("hello world", 5) == "hello..."
    assert truncate("hi", 5) == "hi"


def test_truncate_whole_words():  # TST-10
    assert truncate("hello wonderful world", 12) == "hello..."
    assert truncate("hello", 12) == "hello"


def test_word_count():
    assert word_count("one  two   three") == 3


def test_word_count_empty():  # TST-4
    assert word_count("") == 0


def test_word_count_whitespace():  # TST-8
    assert word_count("one\ttwo\nthree") == 3
    assert word_count("  one two  ") == 2
