import pytest


@pytest.mark.order(1)
@pytest.mark.dependency()
def test_login():
    print("Login")


@pytest.mark.order(2)
@pytest.mark.dependency(depends=["test_login"])
def test_search():
    print("Search")


@pytest.mark.order(3)
@pytest.mark.dependency(depends=["test_search"])
def test_payment():
    print("Payment")
