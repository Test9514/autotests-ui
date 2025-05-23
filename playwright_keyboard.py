from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.focus()

    # Для каждого символа имитируем нажатие клавиш # ввода текста
    for char in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.type(char, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(5000)

