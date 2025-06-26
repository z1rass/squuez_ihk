import os
import requests
import json
from app.untisScrapper import get_themes_from_untis
from playwright.sync_api import sync_playwright
from app.ihk import get_date
from app.untisScrapper import get_themes_from_untis

with sync_playwright() as playwright:
    date = get_date(playwright).split(".")
    print(get_themes_from_untis(playwright, date))
