from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
AZUBI_NUMMER = os.getenv("AZUBI_NUMMER")
PASSWORD = os.getenv("PASSWORD")
MAIL = os.getenv("AZUBI_MAIL")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Открываем страницу и логинимся
    page.goto("https://tibros.ihk-koeln.de/tibrosBB/BB_auszubildende.jsp")
    page.fill("input[name='login']", AZUBI_NUMMER)
    page.fill("input[name='pass']", PASSWORD)
    page.locator("button.btnLogin.oneTimeButton").click()


    page.get_by_role("link", name="Ausbildungsnachweise").click()


    page.locator("button[name='neu']").nth(0).click()

    value = page.locator('input[name="edtvon"]').nth(0).get_attribute('value')
    print("Значение поля edtvon:", value)
    page.fill("input[name='ausbabschnitt']", "IT")
    page.fill("input[name='ausbMail']", MAIL)
    page.fill("input[name='ausbMail2']", MAIL)
    page.screenshot(path="nachweis.png")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
