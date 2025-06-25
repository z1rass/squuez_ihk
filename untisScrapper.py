import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os


def runs(playwright: Playwright) -> None:
    load_dotenv()
    WEB_UNTIS_USERNAME = os.getenv("WEB_UNTIS_USERNAME")
    WEB_UNTIS_PASSWORD = os.getenv("WEB_UNTIS_PASSWORD")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hektor.webuntis.com/WebUntis/?school=K175055#/basic/login")
    page.get_by_role("link", name="Office 365 Anmeldung").click()
    page.get_by_role("textbox", name="Enter your email, phone, or").fill(
        WEB_UNTIS_USERNAME
    )
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Username or email").fill("matvii.k4")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(WEB_UNTIS_PASSWORD)

    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_role("link", name="Mein Stundenplan").click()
    page.get_by_test_id("date-picker-with-arrows-previous").click()
    page.get_by_test_id("date-picker-with-arrows-previous").click()
    page.get_by_test_id("date-picker-with-arrows-previous").click()

    page.wait_for_selector(".timetable-grid-card", timeout=15000)
    cards = page.locator(".timetable-grid-card")
    count = cards.count()
    texts = ""
    for i in range(count):
        cards.nth(i).click()
        time.sleep(2)
        locator = page.locator("textarea.ant-input-disabled")

        if locator.count() > 0:
            lessonName = (
                page.locator("div.active-container span.element").nth(1).inner_text()
            )
            text = locator.first.input_value()
            texts = texts + f"{text}, "
            print(f"{text}\n")
        else:
            pass
        page.go_back()

    # ---------------------
    context.close()
    browser.close()
    return texts
