import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_telegram():
    url = "https://t.me/s/livelawindia"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    messages = []
    # Telegram web preview uses this class for message containers
    message_wrappers = soup.find_all('div', class_='tgme_widget_message_wrap')
    
    for wrap in message_wrappers:
        text_element = wrap.find('div', class_='tgme_widget_message_text')
        date_element = wrap.find('time', class_='time')
        link_element = wrap.find('a', class_='tgme_widget_message_date')
        
        if text_element:
            messages.append({
                "date": date_element['datetime'] if date_element else "N/A",
                "text": text_element.get_text(separator="\n").strip(),
                "url": link_element['href'] if link_element else "N/A"
            })
    
    # Save to ll.json
    with open('ll.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape_telegram()
