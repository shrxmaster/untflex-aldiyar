import urllib.request
import json
from urllib.error import URLError

EXCHANGE_RATES = {
    'EUR': {'USD': 1.11},
    'USD': {'EUR': 0.90},
}

def get_live_rate(from_currency: str, to_currency: str) -> float | None:
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
    try:
        with urllib.request.urlopen(url, timeout=3) as response:
            data = json.loads(response.read().decode())
            return data.get('result')
    except (URLError, ValueError, TimeoutError):
        return None

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    valid_currencies = {'EUR', 'USD'}
    if from_currency not in valid_currencies or to_currency not in valid_currencies:
        raise ValueError(f"Unsupported currency: {from_currency} or {to_currency}")

    if from_currency == to_currency:
        return amount

    rate = get_live_rate(from_currency, to_currency)
    if isinstance(rate, (int, float)):
        return amount * rate

    if to_currency in EXCHANGE_RATES.get(from_currency, {}):
        return amount * EXCHANGE_RATES[from_currency][to_currency]

    raise ValueError(f"No conversion rate available for {from_currency} to {to_currency}")
