import requests
from bs4 import BeautifulSoup
import csv

print("=== DIRECTORY LEAD EXTRACTOR ===")
print("Initializing connection to target directory...")

# Target URL (Sandbox)
url = "http://books.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
    print("Connection established. Parsing HTML matrix...")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Open CSV with professional naming convention
    with open('extracted_leads.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Item Name', 'Data Value']) 
        
        # Target specific HTML containers
        items = soup.find_all("article", class_="product_pod")
        
        for item in items:
            name = item.h3.a["title"]
            value = item.find("p", class_="price_color").text
            writer.writerow([name, value])
            
    print(f"✅ PROCESS COMPLETE: {len(items)} records successfully saved to extracted_leads.csv")
else:
    print(f"❌ ERROR: Server returned status code {response.status_code}")