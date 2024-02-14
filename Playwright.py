import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.flipkart.com/")
    page.get_by_placeholder("Search for Products, Brands").click()
    page.get_by_placeholder("Search for Products, Brands").fill("iphone 15 pro max")
    page.get_by_placeholder("Search for Products, Brands").press("Enter")
    time.sleep(3)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Apple iPhone 15 Pro Max (Natural Titanium, 256 GB) Add to Compare Apple iPhone").click()
    page1 = page1_info.value
    page1.get_by_placeholder("Enter Delivery Pincode").click()
    time.sleep(3)
    page1.get_by_placeholder("Enter Delivery Pincode").fill("560002")
    page1.get_by_text("Check", exact=True).click()
    time.sleep(3)
    page1.get_by_role("button", name="Add to cart").click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
