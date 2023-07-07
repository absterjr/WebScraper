
# Web Scraper

This is a Python script called "scraper.py" that performs web scraping and text processing tasks using various libraries.
The script extracts text from a list of URLs, cleans the text, and outputs the cleaned text to a file.

## Getting Started

To use this script, follow the instructions below:

### Prerequisites

Make sure you have the following libraries installed:

- pandas
- spacy
- goose3
- textblob

You can install these libraries using pip:

```bash
pip install pandas spacy goose3 textblob
```

### Usage

1. Clone the repository or download the "scraper.py" file to your local machine.
2. Create a file named "URL.txt" and add the list of URLs you want to scrape, each URL on a separate line.
3. Open a terminal or command prompt and navigate to the directory where the "scraper.py" file is located.
4. Run the script using the following command:

```bash
python scraper.py
```

5. The script will extract the text from each URL, clean it, and print the cleaned text to the console.
6. The cleaned text will also be saved in a file named "Output.txt" in the same directory.

## Notes

- Make sure you have a stable internet connection to access the URLs.
- The script uses the "en_core_web_sm" model from spaCy for text processing. If you don't have it downloaded, the script will download it automatically.
- Feel free to modify the code to suit your specific requirements or add more functionalities.

## License

This project is licensed under the [MIT License](LICENSE).
