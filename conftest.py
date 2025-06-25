import pytest
from time import sleep
from app.application import Application

@pytest.fixture(scope='function')
def app(request):
    app = Application()
    yield app
    sleep(5)
    app.driver.quit()


#MODIFIYING THE TITLE OF HTML REPORT
def pytest_html_report_title(report):
    report.title = "Automation Test Results"
