from playwright.sync_api import sync_playwright, expect

with (sync_playwright() as playwright):
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
    wait_until='networkidle'        # Ждем полной загрузки страницы
    )

##### 1
####page.evaluate(
####    """
####    const title = document.getElementById('authentication-ui-course-title-text')
####    title.textContent = 'New Text'
####    """
####)

##### 2
####text = 'New Text'
####
####page.evaluate(
####    f"""
####    const title = document.getElementById('authentication-ui-course-title-text')
####    title.textContent = '{text}'
####    """
####)
####
#####    const replaceTitle = (text) => {                                                       #
#####        const title = document.getElementById('authentication-ui-course-title-text')       #   Так делается в
#####        title.textContent = text                                                           #   Браузере
#####    }                                                                                      #   (КОНСОЛЬ)
#####   replaceTitle = ('123123123')                                                            #

    # 3
    new_text = 'New Text'

    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        new_text)

    page.wait_for_timeout(5000)
