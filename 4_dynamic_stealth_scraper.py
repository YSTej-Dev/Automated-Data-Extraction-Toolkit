from playwright.sync_api import sync_playwright
import csv
import time

print("=== DYNAMIC STEALTH SCRAPER ===")
print("Initializing secure extraction protocol...")

with open('stealth_extracted_data.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Target Title', 'Value Metric']) 
    
    with sync_playwright() as p:
        print("⚙️ Launching physical browser instance to bypass standard security...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("🌐 Connecting to target domain...")
        page.goto("http://books.toscrape.com/")
        
        # Wait for dynamic JavaScript elements to fully render
        time.sleep(2) 
        
        print("🛠️ Scanning DOM for target elements...")
        # Locate specific elements directly on the rendered page
        items = page.locator("article.product_pod").all()
        
        for item in items:
            title = item.locator("h3 a").get_attribute("title")
            value = item.locator("p.price_color").inner_text()
            writer.writerow([title, value])
            
        print(f"✅ PROCESS COMPLETE: {len(items)} elements cleanly extracted to stealth_extracted_data.csv")
        
        print("Shutting down browser engine...")
        browser.close()