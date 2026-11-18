from src import strutils


def test_title_case():  # TST-9
    assert strutils.title_case("hello world") == "Hello World"


def test_title_case_small_words():  # TST-9
    assert strutils.title_case("the lord of the rings") == "The Lord of the Rings"
    assert strutils.title_case("a tale of an island") == "A Tale of an Island"
