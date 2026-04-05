A simple and efficient CLI tool to extract book data from Open Library.

# 📚 Book Scraper CLI

A Python-based command-line tool to scrape book data from Open Library and export it into a CSV file.

## 🚀 Features

* 🔍 Search books using any keyword
* 📄 Pagination support (scrape multiple pages)
* 📊 Extracts:

  * Title
  * Author
  * Published Year
  * Book Link
* 💾 Saves results to CSV
* ⚠️ Handles missing data and errors gracefully

## 🛠️ Tech Stack

* Python
* requests
* BeautifulSoup

## ⚙️ Installation

```bash
git clone https://github.com/aditi-1731/book-scraper-cli.git
cd book-scraper-cli
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python scraper.py <query> <pages>
```

### Example

```bash
python scraper.py python 3
```

## 📁 Output

A CSV file will be generated in the format:

```
<query>_books.csv
```

## 💡 Sample Output

```
Learning Python — Mark Lutz  
Automate the Boring Stuff — Al Sweigart  
Python Crash Course — Eric Matthes
Total books found:10
```

## 📌 Notes

* Uses Open Library search pages
* Includes delay between requests to avoid overloading the server
* Designed as a CLI tool for quick data extraction

## 🔮 Future Improvements

* Add filters (year, author)
* Export to Excel format
* Convert into GUI application
* Use API-based approach for faster performance

## 👩‍💻 Author

**Aditi Tripathi**
