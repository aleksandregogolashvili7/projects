from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("ghtrk") == "ghtrk"

def test_shorten_only_vowels():
    assert shorten("aeiouAEIOU") == ""
def test_shorten_space():
    assert shorten("hello world") == "hll wrld"

def vowels():
    assert shorten("a") == ""
def test_shorten_empty():
    assert shorten("") == ""
def test_shorten_NUMBERS():
    assert shorten("CS50") == "CS50"
def test_shorten_PUNCTUATIONS():
    assert shorten("CS,,,50") == "CS,,,50"