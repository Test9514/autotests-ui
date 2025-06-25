import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):  # Создаем тестовую функцию
    # Все остальные действия остаются без изменений

    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()

    chromium_page.wait_for_timeout(5000)
# Как было изначально можно посмотреть в --> playwright_registration
