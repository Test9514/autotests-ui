import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    #        print("Before") Выполняется до
    yield browser.new_page()  # Открываем новую страницу в рамках контекста
    #        print("After")  Выполняется после
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()  # Создание контекста
    # Открываем новую страницу в рамках контекста
    page = context.new_page()  # Создание страницы

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('email@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password = page.get_by_test_id('registration-form-password-input').locator('input')
    password.fill('Password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    context.storage_state(path="browser-state.json")  # Сохраняем состояние браузера


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')  # Указываем файл с сохраненным состоянием
    yield context.new_page()
