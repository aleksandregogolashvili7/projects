from um import count
def test_count():
    assert count("um, um")==2
    assert count("um?")==1
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2
    assert count("Umbrella, thanks, um...")==1
    assert count("UM, um, Um") == 3
    assert count("uM, Mu") == 1
    assert count("Ummmmm, Mu") == 0
