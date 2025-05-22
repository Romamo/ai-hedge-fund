import os
import json
from .cache import Cache

# Change: store cache files in root/data/cache
CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/cache'))

class FileCache(Cache):
    """File cache for API responses (persistent)."""
    def __init__(self):
        super().__init__()
        os.makedirs(CACHE_DIR, exist_ok=True)
        self._load_all()

    def _get_cache_path(self, cache_name: str) -> str:
        return os.path.join(CACHE_DIR, f"{cache_name}.json")

    def _save_cache(self, cache_name: str, cache_data: dict):
        with open(self._get_cache_path(cache_name), "w") as f:
            json.dump(cache_data, f)

    def _load_cache(self, cache_name: str) -> dict:
        path = self._get_cache_path(cache_name)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def _load_all(self):
        self._prices_cache = self._load_cache("prices")
        self._financial_metrics_cache = self._load_cache("financial_metrics")
        self._line_items_cache = self._load_cache("line_items")
        self._insider_trades_cache = self._load_cache("insider_trades")
        self._company_news_cache = self._load_cache("company_news")

    def set_prices(self, ticker: str, data: list[dict[str, any]]):
        super().set_prices(ticker, data)
        self._save_cache("prices", self._prices_cache)

    def set_financial_metrics(self, ticker: str, data: list[dict[str, any]]):
        super().set_financial_metrics(ticker, data)
        self._save_cache("financial_metrics", self._financial_metrics_cache)

    def set_line_items(self, ticker: str, data: list[dict[str, any]]):
        super().set_line_items(ticker, data)
        self._save_cache("line_items", self._line_items_cache)

    def set_insider_trades(self, ticker: str, data: list[dict[str, any]]):
        super().set_insider_trades(ticker, data)
        self._save_cache("insider_trades", self._insider_trades_cache)

    def set_company_news(self, ticker: str, data: list[dict[str, any]]):
        super().set_company_news(ticker, data)
        self._save_cache("company_news", self._company_news_cache)
