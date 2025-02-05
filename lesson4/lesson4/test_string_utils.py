import pytest
from string_utils import StringUtils

"""
сapitilize
Позитивные проверки
"""
@pytest.mark.parametrize('a, b', [ ('latin', 'Latin'),
                                   ('кириллица', 'Кириллица'),
                                   ('123', '123'),
                                   ('l atin', 'L atin') ])
def test_capititlize_positive(a, b):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(a)
    assert res == b

"""
сapitilize
Негативные проверки
"""

@pytest.mark.parametrize('a, b', [ ('', ''),
                                   (' ', ' ') ])
def test_capititlize_negative(a, b):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(a)
    assert res == b




"""
trim
Позитивные проверки
"""
@pytest.mark.parametrize('a, b', [ ('latin', 'latin'),
                                   ('кириллица', 'кириллица'),
                                   ('123', '123'), (' latin', 'latin'),
                                   (' l atin', 'l atin'),
                                   (' 123', '123') ])
def test_trim_positive(a, b):
    stringUtils = StringUtils()
    res = stringUtils.trim(a)
    assert res == b

"""
trim
Негативные проверки
"""

@pytest.mark.parametrize('a, b', [ ('', ''),
                                   (' ', '') ])
def test_trim_negative(a, b):
    stringUtils = StringUtils()
    res = stringUtils.trim(a)
    assert res == b

"""
to_list
Позитивные проверки
"""
@pytest.mark.parametrize('a, delimeter, expect', [('а.б.в.г.д.е', '.' , ['а','б','в','г','д','е'])])
def test_to_list_positive(a, delimeter, expect):
    stringUtils = StringUtils()
    res = stringUtils.to_list(a, delimeter)
    assert res == expect

@pytest.mark.parametrize('a, expect', [('а,б,в,г,д,е', ['а','б','в','г','д','е']),
                                       ('a,b,c,d,e,f', ['a','b','c','d','e','f'])])
def test_to_list_positive(a, expect):
    stringUtils = StringUtils()
    res = stringUtils.to_list(a)
    assert res == expect

"""
to_list
Негативные проверки
"""
@pytest.mark.parametrize('a, expect', [('', []),
                                       (' ', []),
                                       (' , ', [' ',' '])])
def test_to_list_negative(a, expect):
    stringUtils = StringUtils()
    res = stringUtils.to_list(a)
    assert res == expect

"""
contains
Позитивные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'a', True),
                                          ('абв', 'а', True),
                                          ('123', '1', True)])
def test_contains_positive(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.contains(a, b)
    assert res == expect



"""
contains
Негативные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'с', False),
                                          ('', '', True)])
def test_contains_negativee(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.contains(a, b)
    assert res == expect

"""
delete_symbol
Позитивные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'a', 'sd'),
                                          ('абв', 'а', 'бв'),
                                          ('123', '1', '23')])
def test_delete_symbol_positive(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(a, b)
    assert res == expect

"""
delete_symbol
Негативные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'с', 'asd'),
                                          ('', '', '')])
def test_delete_symbol_negative(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(a, b)
    assert res == expect

"""
starts_with
Позитивные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'a', True),
                                          ('абв', 'а', True),
                                          ('123', '1', True),
                                          ('asd', 's', False)])
def test_starts_with_positive(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(a, b)
    assert res == expect

"""
starts_with
Негативные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('', 'a', False),
                                          (' ', 'а', False),
                                          ('', '', True)])
def test_starts_with_negative(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(a, b)
    assert res == expect

"""
end_with
Позитивные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('asd', 'd', True),
                                          ('абв', 'в', True),
                                          ('123', '3', True),
                                          ('asd', 's', False)])
def test_end_with_positive(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.end_with(a, b)
    assert res == expect

"""
end_with
Негативные проверки
"""

@pytest.mark.parametrize('a, b, expect', [('', 'a', False),
                                          (' ', 'а', False),
                                          ('', '', True)])
def test_end_with_negative(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.end_with(a, b)
    assert res == expect

"""
is_empty
Позитивные проверки
"""

@pytest.mark.parametrize('a, expect', [('', True),
                                          (' ',True)])
def test_is_empty_positive(a, expect):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(a)
    assert res == expect

"""
is_empty
Негативные проверки
"""

@pytest.mark.parametrize('a, expect', [('asd', False),
                                       ('абв',False),
                                       ('123',False)])
def test_is_empty_negative(a, expect):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(a)
    assert res == expect

"""
list_to_string
Позитивные проверки
"""

@pytest.mark.parametrize('a, b, expect', [(['a', 'b', 'c',], ', ', 'a, b, c'),
                                          (['а', 'б', 'в',], ', ', 'а, б, в'),
                                          (['1', '2', '3',], ', ', '1, 2, 3')])
def test_list_to_string_positive(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(a, b)
    assert res == expect

"""
list_to_string
Негативные проверки
"""

@pytest.mark.parametrize('a, b, expect', [(['a', 'b', 'c',], '', 'abc'),
                                          (['а', 'б', 'в',], ' ', 'а б в'),
                                          (['', '', '',], ',', ',,')])
def test_list_to_string_negative(a, b, expect):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(a, b)
    assert res == expect