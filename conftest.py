import pytest


@pytest.fixture()
def set_up():
    print('Start test') # Все, что до слова yield - будет происходить до теста
    yield # Проходит сам тест
    print('Finish test')


@pytest.fixture(scope='module') #Сделали определенную текстуру прямо под модуль
def set_group(): # группа тестов ,которые касаются того или иного модуля
    print('Enter system')
    yield
    print('Exit system')