import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_verdictum():
    url = "https://t.me/s/verdictumlegalupdates"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    message_wrappers = soup.find_all('div', class_='tgme_widget_message_wrap')
    
    updates = []
    for wrap in message_wrappers:
        text_element = wrap.find('div', class_='tgme_widget_message_text')
        date_element = wrap.find('time', class_='time')
        link_element = wrap.find('a', class_='tgme_widget_message_date')
        
        if text_element:
            updates.append({
                "date": date_element['datetime'] if date_element else "N/A",
                "text": text_element.get_text(separator="\n").strip(),
                "url": link_element['href'] if link_element else "#"
            })

    # 1. Save to v.json
    with open('v.json', 'w', encoding='utf-8') as f:
        json.dump(updates, f, ensure_ascii=False, indent=4)
    
    # 2. Save to v.md (Newest Updates at the top)
    with open('v.md', 'w', encoding='utf-8') as f:
        f.write("# Verdictum Legal Updates\n\n")
        f.write(f"*Last Updated: {updates[-1]['date'] if updates else 'N/A'}*\n\n---\n\n")
        
        for up in reversed(updates):
            f.write(f"### {up['date']}\n")
            f.write(f"{up['text']}\n\n")
            f.write(f"[Source
