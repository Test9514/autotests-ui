from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f'Request: {request.url}')

# Логирование ответов
def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')         # {response.status} - Показывает код выполнения


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request)                     # Добавление Обработчик события отправки запроса
#    page.remove_listener('request', log_request)        # Убираем обработчик
    page.on('response', log_response)                   # Обработчик события получения ответа

    page.wait_for_timeout(5000)
