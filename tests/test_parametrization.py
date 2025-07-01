import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f' Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperation:
    #    @pytest.mark.parametrize('user', ['Alice', 'Zara'])
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'user with operations: {user}')

    #    @pytest.mark.parametrize('user', ['Alice', 'Zara'])
    def test_user_without_operations(self, user: str):
        print(f'user without operations: {user}')


#   ПРИМЕР 1
@pytest.mark.parametrize(
    'phone_number',
    ['+70000000011', '+70000000022', '+70000000033'],
    ids=[
        'User with money on bank account',
        'User without money on bank account',
        'User without operations on bank account'
    ]
)
def test_identifiers_1(phone_number: str):
    ...


#   ПРИМЕР 2 С ЛЯМБДОЙ (КОНТЕКСТНАЯ Ф-ЦИЯ)
#   В ДАННОМ ВАРИАНТЕ ЛУЧШЕ ТАКОЙ ВАРИАНТ ИСПОЛЬЗОВАТЬ
users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User without operations on bank account',
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers_2(phone_number: str):
    ...


#   ПРИМЕР 3 С ОБЫЧНОЙ ФУНКЦИЕЙ
users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User without operations on bank account',
}


def format_phone_number(phone_number: str) -> str:
    return f'{phone_number}: {users[phone_number]}'


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=format_phone_number
)
def test_identifiers_3(phone_number: str):
    ...
