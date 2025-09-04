import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Target website (example: BBC News front page)
URL = "https://www.bbc.com/news"

# Fetch page
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines
headlines = []
for h in soup.select("h2"):  # BBC uses <h2> for many headlines
    text = h.get_text(strip=True)
    if text:
        headlines.append(text)

# Save to CSV
df = pd.DataFrame(headlines, columns=["Headline"])
filename = f"headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False, encoding="utf-8")

print(f"✅ Scraped {len(headlines)} headlines and saved to {filename}")
