import pytest
from phones import is_phone_number, get_region
from random import randint

VALID_TEST_NUMBER = 20

start = 1000000000
end = 9999999999
test_database = 'test_db.txt'

valid_regions = (
    ('88129137552', 'Saint_Petersburg'),
    ('88629137552', 'Krasnodar_region'),
    ('83839137552', 'Novosibirsk_region'),
    ('88559137552', 'Naberezhnye_Chelny'),
    ('+78129137552', 'Saint_Petersburg'),
    ('+78629137552', 'Krasnodar_region'),
    ('+73839137552', 'Novosibirsk_region'),
    ('+78559137552', 'Naberezhnye_Chelny')
)

invalid_regions = (
    ('88129137552', '812 not defined'),
    ('88629137552', '862 not defined'),
    ('83839137552', '383 not defined'),
    ('88559137552', '855 not defined'),
    ('+78129137552', '812 not defined'),
    ('+78629137552', '862 not defined'),
    ('+73839137552', '383 not defined'),
    ('+78559137552', '855 not defined')
)

valid_phones = []
for _ in range(VALID_TEST_NUMBER):
    number = str(randint(start, end))
    valid_phones.append(f'+7{number}')
    valid_phones.append(f'8{number}')


invalid_phones = ('+89493687126', 
                  ' ', 
                  '2341+2', 
                  'dsaw')


@pytest.mark.parametrize('phone', valid_phones)
def test_valid_phones(phone: str):
    assert is_phone_number(phone)


@pytest.mark.parametrize('phone', invalid_phones)
def test_invalid_phones(phone: str):
    assert not is_phone_number(phone)


@pytest.mark.parametrize('number, expected', valid_regions)
def test_valid_regions(number: str, expected: str):
    assert get_region(number, test_database) == expected


@pytest.mark.parametrize('number, expected', invalid_regions)
def test_invalid_regions(number: str, expected: str):
    assert not get_region(number, test_database) == expected


@pytest.mark.xfail(raises=Exception)
def test_exception_regions():
    get_region('dsafigyoeiu', 'test_db.txt')