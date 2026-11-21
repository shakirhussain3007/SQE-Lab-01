# SQE Lab 01 — Selenium Browser Navigation

## Requirements
- Python 3
- Google Chrome
- Selenium

## Install Selenium
```bash
python -m pip install -U selenium
```

## Run an exercise
Open a terminal in this folder and run one file at a time:
```bash
python Exercise_3_Three_Website_Navigation.py
python Exercise_4_Browser_History.py
python Exercise_5_Refresh_Verification.py
python Exercise_6_Complete_Navigation_Test.py
```

Selenium Manager normally handles the Chrome driver automatically in a standard setup.

## Files
- Exercise 3: visits three websites, prints title and URL, then uses Back and Forward.
- Exercise 4: demonstrates browser history with Back and Forward.
- Exercise 5: compares the page title before and after refresh.
- Exercise 6: maximizes Chrome and demonstrates navigation, history, refresh, and page information.

Each program uses `try/finally` so `driver.quit()` runs even if an error occurs.
