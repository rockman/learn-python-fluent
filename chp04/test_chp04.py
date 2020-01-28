
def test_encode_decode():
    s = 'café'
    b = s.encode('utf-8')

    assert len(s) == 4
    assert b == b'caf\xc3\xa9'
    assert len(b) == 5


def test_constructing_bytes():
    assert bytes('café', encoding='utf-8') == b'caf\xc3\xa9'

    import array
    byte_array = array.array('b', [-1, 0, 1])
    short_array = array.array('h', [-1, 0, 1])
    assert bytes(byte_array) == b'\xff\x00\x01'
    assert bytes(short_array) == b'\xff\xff\x00\x00\x01\x00'


def test_bytes_regex():
    import re

    tamil_numbers = '\u0bed\u0bee'

    assert len(re.findall(rb'\d', tamil_numbers.encode('utf-8'))) == 0
    assert len(re.findall(r'\d', tamil_numbers)) == 2
