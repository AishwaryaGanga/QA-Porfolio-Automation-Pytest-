import pytest
from time import sleep
from app.application import Application

@pytest.fixture(scope='function')
def app(request):
    app = Application()
    yield app
    sleep(5)
    request.addfinalizer(app.driver.quit)
    return app
