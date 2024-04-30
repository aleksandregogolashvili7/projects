from plates import is_valid_license_plate
def main():
    is_valid_license_plate()

def test_valid():
    assert is_valid_license_plate('CS50') == True
    assert is_valid_license_plate('CS05') == False
    assert is_valid_license_plate('CS50P') == False
    assert is_valid_license_plate('HANCOCK') == False
    assert is_valid_license_plate('HELLO') == True
    assert is_valid_license_plate('30192') == False
    assert is_valid_license_plate('CS50.,') == False



if __name__=='__main__':
    main()