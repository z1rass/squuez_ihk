from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
import os
import requests
import json
from untisScrapper import get_themes_from_untis

load_dotenv()
AZUBI_NUMMER = os.getenv("AZUBI_NUMMER")
PASSWORD = os.getenv("PASSWORD")
MAIL = os.getenv("AZUBI_MAIL")
API_TOKEN = os.getenv("API_TOKEN")


def run(playwright: Playwright, themes) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://tibros.ihk-koeln.de/tibrosBB/BB_auszubildende.jsp")
    page.fill("input[name='login']", AZUBI_NUMMER)
    page.fill("input[name='pass']", PASSWORD)
    page.locator("button.btnLogin.oneTimeButton").click()

    page.get_by_role("link", name="Ausbildungsnachweise").click()

    page.locator("button[name='neu']").nth(0).click()

    value = page.locator('input[name="edtvon"]').nth(0).get_attribute("value")
    print("Значение поля edtvon:", value)
    page.fill("input[name='ausbabschnitt']", "IT")
    page.fill("input[name='ausbMail']", MAIL)
    page.fill("input[name='ausbMail2']", MAIL)

    url = "https://api.awanllm.com/v1/chat/completions"
    studies = themes
    messages = [
        {
            "role": "system",
            "content": (
                "Du bist ein KI-Assistent. Verfasse einen kurzen, formellen Wochenbericht für das Berufskolleg, wie er im IHK-Ausbildungsnachweis-Heft verwendet wird. "
                "Nutze 1–2 vollständige, sachliche Sätze im Präsens oder Präteritum. "
                "Gib ausschließlich die folgenden Themen wieder, ohne Erklärungen, Floskeln oder persönliche Anrede: "
                f"{studies}. "
                "Vermeide Ausschmückungen, Meinungen, E-Mail-Form, Begrüßungen wie 'Sehr geehrte Damen und Herren' oder Abschlüsse wie 'Mit freundlichen Grüßen'. "
                "Der Text soll neutral und direkt sein, nur die Unterrichtsinhalte beschreiben."
            ),
        }
    ]

    payload = json.dumps(
        {
            "model": "Meta-Llama-3-70B-Instruct",
            "messages": messages,
            "repetition_penalty": 1.1,
            "temperature": 0.5,
            "top_p": 0.8,
            "top_k": 40,
            "max_tokens": 200,
            "stream": False,
        }
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }

    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)

    content = response.json()["choices"][0]["message"]["content"]
    cleaned = content.replace(
        "<|start_header_id|>assistant<|end_header_id|>", ""
    ).strip()

    page.fill("textarea[name='ausbinhalt3']", cleaned)
    page.click("button.addAzubiHeftButton")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    themes = get_themes_from_untis(playwright, ["2025", "03", "02"])
    run(playwright, themes)
