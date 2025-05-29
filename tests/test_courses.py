from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()  # Создание контекста
        # Открываем новую страницу в рамках контекста
        page = context.new_page()  # Создание страницы

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('email@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password = page.get_by_test_id('registration-form-password-input').locator('input')
        password.fill('Password')

        button_registration = page.get_by_test_id('registration-page-registration-button')
        button_registration.click()

        context.storage_state(path="browser-state.json")  # Сохраняем состояние браузера

        page.wait_for_timeout(5000)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(toolbar_title).to_be_visible()  # Проверяем наличие
        expect(toolbar_title).to_have_text('Courses')  # Проверяем текст

        empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_visible()  # Проверяем наличие

        title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_text).to_be_visible()  # Проверяем наличие
        expect(title_text).to_have_text('There is no results')  # Проверяем текст

        description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text).to_be_visible()  # Проверяем наличие
        expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
        # Проверяем текст

#        page.wait_for_timeout(5000)
