# QuoteByte

QuoteByte is a modern quote subscription landing page built with Flask. It combines a quotes scraper with a premium one-page user experience where visitors can preview curated quotes, refresh quotes a limited number of times, and subscribe for daily inspiration.

## Features

- Quotes scraper that collects quotes into CSV
- Premium one-page landing page
- Random quote preview
- Smooth in-page quote refresh
- Limited free refresh system
- Subscription form with duplicate email protection
- Responsive layout for desktop and mobile
- Animated UI elements and subscribe prompt overlay

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- BeautifulSoup
- CSV

## Project Structure

text
QuoteByte/
├── app.py
├── quotes.csv
├── subscribers.csv
├── templates/
│   └── index.html
├── static/ or public/
│   └── style.css
└── scraper/
    └── main.py

## 🌐 Live Demo

[🚀 View Live App](https://quote-byte.vercel.app/)


## How It Works

1. Quotes are scraped and saved into quotes.csv


2. The Flask app loads a random quote from the CSV


3. Users can refresh quotes a limited number of times


4. After the free refresh limit is reached, a subscribe prompt appears


5. Users can enter their email to subscribe



## Run Locally

1. Clone the repository



git clone https://github.com/NhartyInnovate/QuoteByte.git
cd QuoteByte

2. Install dependencies



pip install -r requirements.txt

3. Run the app



python app.py

4. Open in browser



http://127.0.0.1:5000


## Future Improvements

- Real daily email delivery

- Curated quote categories

- Admin dashboard for quote management

- Better subscriber storage

- Quote history and favorites


## Author

Nathaniel Katugwa

## License

This project is for learning, experimentation, and portfolio use.
