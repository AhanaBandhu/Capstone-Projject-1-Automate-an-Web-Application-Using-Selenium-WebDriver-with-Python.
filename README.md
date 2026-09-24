# E-Commerce Web Automation — Selenium WebDriver + Python

## **🎥 Project Video Demonstration**

[▶️ Watch Project Video](https://drive.google.com/file/d/1AUknmQfgIVlgE7nL3TIUxPnU6T6F1QBo/view?usp=sharing)
Capstone Assignment 1: End-to-end automation of a public e-commerce demo
site (OpenCart demo — https://tutorialsninja.com/demo/) using the
Page Object Model (POM) design pattern.

## Automated Flow

1. Launch browser (Chrome, via WebDriver Manager — no manual driver download)
2. Login to the application (auto-registers a new account on first run if
   the configured credentials don't exist yet)
3. Search for a product
4. Add the product to the cart
5. Update the quantity in the cart
6. Verify cart details (product name, quantity, line total)
7. Capture screenshots at every major step
8. Read test data from an external JSON file (`data/testdata.json`) —
   an Excel reader (`utils/excel_reader.py`) is also included and used
   automatically if `data/testdata.xlsx` is present
9. Handle JavaScript popups/alerts if the site raises any
10. Generate an HTML execution report (`reports/execution_report.html`)
    with pass/fail status, timestamps, duration and screenshots for
    every step

## Project Structure

```
ecommerce_automation/
├── main.py                     # Entry point — runs the full flow
├── requirements.txt
├── README.md
├── config/
│   └── config.py               # URLs, timeouts, browser settings
├── data/
│   ├── testdata.json           # Test data (credentials, product, qty)
│   └── testdata.xlsx.md        # Note: how to add an optional Excel file
├── pages/                      # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── search_page.py
│   └── cart_page.py
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py       # WebDriver creation
│   ├── data_reader.py          # JSON + Excel test data reader
│   ├── screenshot_utils.py     # Screenshot capture helper
│   ├── alert_handler.py        # Popup/alert handling
│   └── report_generator.py     # HTML report generation
├── tests/
│   ├── __init__.py
│   └── test_ecommerce_flow.py  # unittest test case wiring it together
└── reports/
    ├── screenshots/             # Auto-populated at run time
    └── execution_report.html    # Auto-generated at run time
```

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

or, using the standard test runner:

```bash
python -m unittest tests/test_ecommerce_flow.py -v
```

Chrome is used by default and is run headless when `HEADLESS=true` is
set in `config/config.py` or as an environment variable — useful for CI.

## Notes

- Selenium 4's built-in Selenium Manager resolves the correct
  chromedriver automatically, so no separate driver binary/download is
  required.
- `tutorialsninja.com/demo` does not expose a fixed public login, so the
  framework registers a fresh throwaway account the first time it runs
  (using the name/email template in `testdata.json`) and reuses it on
  later runs. Swap in your own known-good credentials in
  `data/testdata.json` if you have an existing account.
