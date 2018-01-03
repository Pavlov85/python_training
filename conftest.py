import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    # Если фикстуры нет, то инициализируем новую и выполняем логин
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        # Проверка на валидность фикстуры
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
        request.addfinalizer(fin)
    return fixture