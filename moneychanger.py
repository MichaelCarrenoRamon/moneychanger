from typing import Tuple, Dict
import dotenv
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
EXCHANGERATE_API_KEY = os.getenv('EXCHANGERATE_API_KEY')

def get_exchange_rate(base: str, target: str, amount: str) -> Tuple:
    """Return a tuple of (base, target, amount, conversion_result (2 decimal places))"""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/pair/{base}/{target}/{amount}"
    response = json.loads(requests.get(url).text)
    return (base, target, amount, f'{response["conversion_result"]:.2f}')

print(get_exchange_rate("USD", "GBP", "350"))