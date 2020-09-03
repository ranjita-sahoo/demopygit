import re
import dateparser

DM_DMY_PATTERN = r"\s\d{1,2}[-/.](?:\d{1,2}[-/.])?\d{1,4}\s"
D_MONTH_Y_PATTERN = r"(\d{1,2}(?:rd|th)?\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s(?:\d{2,4})?)"
PRICE_PATTERN = r"\d+[.\d+]?[,\d+]*"
CURRENCY_PRICE_PATTERN = r"({0}\s?" + PRICE_PATTERN + "|" + PRICE_PATTERN + "\s?{0})"

class Cycle:
    def __init__(self, frame, handle_bar_brakes, seating, wheels, dates, prices):
        self.frame = frame
        self.handle_bar_brakes = handle_bar_brakes
        self.seating = seating
        self.wheels = wheels
        self.dates = dates
        self.prices = prices
def extract_dates(text):
    all_results = []
    all_results.extend(re.findall(DM_DMY_PATTERN, text))
    all_results.extend(re.findall(D_MONTH_Y_PATTERN, text))
    parsed_results = []
    for result in all_results:
        try:
            valid_date = dateparser.parse(result, settings={'DATE_ORDER': 'DMY'})
            parsed_results.append(valid_date)
        except ValueError:
            pass
    return parsed_results

def extract_prices(text):
    currencies_list = ["€", "\$", "euro", "dollars"]
    tot_results = []
    for currency in currencies_list:
        results = re.findall(CURRENCY_PRICE_PATTERN.format(currency), text, re.IGNORECASE)
        tot_results.extend(results)
    return tot_results

if __name__ == "__main__":
    print("Enter text and I will extract prices and dates (Q for exit):")
    new_price = input("> ")
    while new_price != "Q":
        print(extract_prices(new_price))
        print(extract_dates(new_price))
        new_price = input("> ")
