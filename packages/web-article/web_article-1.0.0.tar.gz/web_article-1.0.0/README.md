# web_article: A Python Article Scraper and CLI Tool
> `web_article` is a Python package designed to scrape and parse articles from various web sources seamlessly. Accompanied by a command-line interface (CLI) tool, users can efficiently extract articles from given URLs and export them in multiple formats.

## Features
- Scrape articles from multiple supported URLs.
- Export articles to various formats: JSON, JL, and CSV.
- Intuitive command-line tool for quick extraction and export.
- Flexible output options, including encoding, indentation, and delimiters.

## Requirements
Python 3.x

## Installation
```bash
python3 -m pip install web_article
```

## Usage
> Using the web_article CLI tool is straightforward. Here are some common use cases:

1. Scraping a Single Article from URL:
```bash
web_article url1
```

2. Scraping Multiple Articles from URLs:
```
web_article url1 url2 url3
```

3. Scraping Articles from URLs Listed in a File:
```
web_article urls.txt
```

4. Exporting Articles in JSON Format:
```
web_article urls.txt -o out.json -f json
```

5. Exporting Articles in JSON Format with Indentation:
```
web_article urls.txt -o out.json -f json -i 2
```

6. Exporting Articles in CSV Format:
```
web_article urls.txt -o out.csv -f csv
```

7. Exporting in a Specific Encoding (e.g., UTF-8 with BOM for Office Excel):
```
web_article urls.txt -o out.csv -f csv -e utf-8-sig
```

#### Options:
```
-o, --outfile : The name of the output file. Defaults to standard output if not provided.

-f, --outfmt : The format for the output. Choices are 'jl', 'json', 'csv'. Defaults to 'jl'.

-d, --delimiter : Delimiter for CSV output. Default is ','.

-e, --encoding : Encoding for the output file. Default is 'utf-8'.

-i, --indent : Indentation for JSON output. An integer value.
```
