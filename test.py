from google import genai
from google.genai import types

studies = (
    "IP-Adressen für Firma Huber, Notenbesprechung, Führungsstile, Rückblick auf LS 5.3: typisches Vorgehen in der SW-Entwicklung vom Problem zur Spezifikation, "
    "Review und Überarbeitung der eigenen Userstories mithilfe einer Userstory eines anderen Couples, Sicherung unter Teams als Version 1.1, "
    "Video KH zu Use-Case-Diagrammen, Erstellung eines UC-Diagramms mithilfe des Lastenhefts und der eigenen Userstory (teilweise unter Teams gesichert), "
    "Gespräche zur Leistungsbewertung begonnen, nächstes Mal: UC als PDF ablegen lassen, Input zu Reviews und Review der vorliegenden UC-Diagramme, "
    "Überarbeitung der UC-Diagramme zu V1.1, Tag der Ausbildung laut Sonderstundenplan für Freitag und Samstag."
)


client = genai.Client(api_key="TOKEN")
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
        max_output_tokens=100,  # Disables thinking
    ),
)
print(response.text)
