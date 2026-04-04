import requests
from bs4 import BeautifulSoup
import csv
import time
import sys

headers = {
    "User-Agent": "Mozilla/5.0"
}
count=0

if len(sys.argv)<3:
    print("usage: python scraper.py <query> <pages>")
    sys.exit()

query=sys.argv[1]
pages=int(sys.argv[2])
with open(f"{query}_books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Author", "Year", "Link"])

    for page in range(1,pages+1):
        url = f"https://openlibrary.org/search?q={query}&page={page}"
        print(f"\nScraping page {page}...")
        try:
            response=requests.get(url,headers=headers,timeout=15)
            response.raise_for_status()
        except Exception as e:
            print("Error:",e)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("li", class_="searchResultItem")
        for book in books:
            try:
                title_tag = book.find("a",class_="results")
                if not title_tag:
                    continue 
                
                title = title_tag.text.strip()

                link = "https://openlibrary.org" + title_tag["href"]

                author_tag = book.find("span", class_="bookauthor")
                author = author_tag.text.replace("by","").strip() if author_tag else "N/A"

                year_tag = book.find("span", class_="publishedYear")
                year = year_tag.text.strip() if year_tag else "N/A"

                print(title, "-", author)

                writer.writerow([title, author, year, link])
                count+=1
            except Exception as e:
                print("Skipping:", e)
        time.sleep(1)
        

print(f"Total books scraped: {count}")    
print("Data saved successfully!")
