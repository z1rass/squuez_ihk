from app.config import *
from playwright.sync_api import Playwright


def write_berufschule(playwright: Playwright, text) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://tibros.ihk-koeln.de/tibrosBB/BB_auszubildende.jsp")
    page.fill("input[name='login']", AZUBI_NUMMER)
    page.fill("input[name='pass']", PASSWORD)
    page.locator("button.btnLogin.oneTimeButton").click()

    page.get_by_role("link", name="Ausbildungsnachweise").click()

    page.locator("button[name='neu']").nth(0).click()
    page.locator('input[name="ausbabschnitt"]').first.fill("IT")
    page.locator('input[name="ausbMail"]').fill(AUSBILDER_MAIL)
    page.locator('input[name="ausbMail2"]').fill(AUSBILDER_MAIL)
    page.locator('textarea[name="ausbinhalt3"]').fill(text)
    page.get_by_role("button", name="Speichern", exact=True).click()
    context.close()
    browser.close()
