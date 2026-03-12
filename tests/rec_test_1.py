import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Accept all").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_text("Miss Zagreb").click()
    page.locator("iframe[name=\"a-nn03j4m2ren5\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)