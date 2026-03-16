from fastapi import FastAPI, Query
from playwright.async_api import async_playwright
import uvicorn

app = FastAPI()

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

@app.get('/scrape')
async def scrape(url: str = Query(...)):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel="chrome",
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-extensions",
                "--disable-infobars",
                "--disable-notifications",
            ]
        )
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale='en-AU',
            viewport={'width': 1366, 'height': 768},
            extra_http_headers={
                "Accept-Language": "en-AU,en;q=0.9",
                "Upgrade-Insecure-Requests": "1",
            },
        )
        page = await context.new_page()
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)
        html = await page.content()
        await context.close()
        await browser.close()
        return {'html': html}
    
if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8000)