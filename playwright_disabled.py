from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).not_to_be_disabled()   # Проверяем, что кнопка задизейблена

    page.wait_for_timeout(5000)
