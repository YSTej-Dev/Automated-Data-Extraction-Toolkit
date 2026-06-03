from playwright.sync_api import sync_playwright
import time

print("=== AUTOMATED AUTHENTICATION BOT ===")

with sync_playwright() as p:
    print("⚙️ Initializing Chromium browser engine...")
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page()

    print("🌐 Navigating to secure portal...")
    page.goto("https://practicetestautomation.com/practice-test-login/")

    print("⌨️ Injecting authorized credentials...")
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")

    print("🖱️ Executing login sequence...")
    page.locator("#submit").click()
    
    print("⏳ Waiting for server verification...")
    try:
        # Smart wait: waits exactly until the URL changes, up to 5 seconds
        page.wait_for_url("**/logged-in-successfully/", timeout=5000)
        print("✅ SUCCESS: Security bypassed. Access granted.")
    except:
        print("❌ FAILED: Authentication rejected by server or timed out.")

    print("Terminating browser session...")
    time.sleep(2)
    browser.close()