import os
import requests
import json
from app.untisScrapper import get_themes_from_untis
from playwright.sync_api import sync_playwright
from app.ihk import get_date
from app.untisScrapper import get_themes_from_untis
from app.genarate_text import get_gen_text
from app.write_berufschule import write_berufschule

with sync_playwright() as playwright:
    date = get_date(playwright).split(".")
    themes = get_themes_from_untis(playwright, date)
    (
        write_berufschule(playwright, "Ferien")
        if themes == "Ferien"
        else write_berufschule(playwright, get_gen_text(themes))
    )
