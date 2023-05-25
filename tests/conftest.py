import pytest

@pytest.fixture()
def set_up():
    print("\n" + "Вход в систему выполнен")
    yield
    print("\n" + "Выход из системы")

@pytest.fixture(scope="function")
def some():
    print("\n" + "Начало")
    yield
    print("\n" + "Конец")


def idfn(val):
    return "params: {0}".format(str(val))


@pytest.fixture(params=[("morpheus","leader"), ("shmorpheus", "shleader")], ids=idfn)
def users(request):
    return request.param

@pytest.fixture(params=["1","2","3"], ids=idfn)
def pages(request):
    return request.param

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
