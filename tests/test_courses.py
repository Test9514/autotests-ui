import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_title).to_be_visible()  # Проверяем наличие
    expect(toolbar_title).to_have_text('Courses')  # Проверяем текст

    empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()  # Проверяем наличие

    title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_text).to_be_visible()  # Проверяем наличие
    expect(title_text).to_have_text('There is no results')  # Проверяем текст

    description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()  # Проверяем наличие
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
    # Проверяем текст

#    chromium_page_with_state.wait_for_timeout(5000)
