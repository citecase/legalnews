import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_telegram():
    url = "https://t.me/s/livelawindia"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    messages = []
    message_wrappers = soup.find_all('div', class_='tgme_widget_message_wrap')
    
    # 1. Prepare Data
    for wrap in message_wrappers:
        text_element = wrap.find('div', class_='tgme_widget_message_text')
        date_element = wrap.find('time', class_='time')
        link_element = wrap.find('a', class_='tgme_widget_message_date')
        
        if text_element:
            messages.append({
                "date": date_element['datetime'] if date_element else "N/A",
                "text": text_element.get_text(separator="\n").strip(),
                "url": link_element['href'] if link_element else "#"
            })
    
    # 2. Save to ll.json
    with open('ll.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)
        
    # 3. Save to ll.md (Markdown Format)
    with open('ll.md', 'w', encoding='utf-8') as f:
        f.write("# LiveLaw India Latest Updates\n\n")
        f.write(f"*Last Updated: {messages[0]['date'] if messages else 'N/A'}*\n\n---\n\n")
        
        for msg in messages:
            f.write(f"### {msg['date']}\n")
            f.write(f"{msg['text']}\n\n")
            f.write(f"[Read on Telegram]({msg['url']})\n\n")
            f.write("---\n")

if __name__ == "__main__":
    scrape_telegram()
