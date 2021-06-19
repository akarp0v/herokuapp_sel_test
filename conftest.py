from pytest import fixture
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--headless', default="no", help="Headless mode")


@fixture(scope="session")
def browser(request):
    headless = request.config.getoption("headless")
    options = Options()
    if headless in ('yes', 'y', '1', 'true'):
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    print("\nstart browser...")
    browser = webdriver.Chrome(executable_path=binary_path, options=options)

    yield browser

    print("\nquit browser...")
    browser.quit()
