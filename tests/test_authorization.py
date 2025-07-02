import pytest
from playwright.sync_api import expect, Page


### "@pytest.mark.parametrize('password')" Перемещен выше
### "@pytest.mark.parametrize('email')", чтобы вывод был:
###
### tests/test_authorization.py::test_wrong_email_or_password_authorization[email #1-password #1] PASSED
### tests/test_authorization.py::test_wrong_email_or_password_authorization[email #1-password #2] PASSED
### ...
### tests/test_authorization.py::test_wrong_email_or_password_authorization[email #3-password #3] PASSED
###
### Видеть email на первом месте, а потом password комфортнее для глаза
###

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    'email, password',
    [
        ('user.name@gmail.com', 'password'),
        ('user.name@gmail.com', '  '),
        ('  ', 'password')
    ]
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()

    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

#    chromium_page.wait_for_timeout(5000)

### СТАРЫЙ ТЕСТ (НЕ УДАЛЯЮ)

####@pytest.mark.regression
####@pytest.mark.authorization
####def test_wrong_email_or_password_authorization_old(chromium_page: Page):
####    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
####
####    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
####    email_input.fill('user.name@gmail.com')
####
####    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
####    password_input.fill('password')
####
####    login_button = chromium_page.get_by_test_id('login-page-login-button')
####    login_button.click()
####
####    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
####    expect(wrong_email_or_password_alert).to_be_visible()
####
####    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
####
#####        page.wait_for_timeout(5000)
####
##### Как было изначально можно посмотреть в --> playwright_authorization
###
###
