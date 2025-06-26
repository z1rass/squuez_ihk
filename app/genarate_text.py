from app.config import *
from google import genai
from google.genai import types


def get_gen_text(text):
    studies = text

    client = genai.Client(api_key=GEMINI_API_TOKEN)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "Du bist ein KI-Assistent. Verfasse einen kurzen, formellen Wochenbericht für das Berufskolleg, wie er im IHK-Ausbildungsnachweis-Heft verwendet wird. "
            "Nutze 1–2 vollständige bis 100 tokens, sachliche Sätze im Präsens oder Präteritum. "
            "Gib ausschließlich die folgenden Themen wieder, ohne Erklärungen, Floskeln oder persönliche Anrede: "
            f"{studies}. "
            "Vermeide Ausschmückungen, Meinungen, E-Mail-Form, Begrüßungen wie 'Sehr geehrte Damen und Herren' oder Abschlüsse wie 'Mit freundlichen Grüßen'. "
            "Der Text soll neutral und direkt sein, nur die Unterrichtsinhalte beschreiben."
        ),
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            max_output_tokens=100,
        ),
    )
    return response.text
