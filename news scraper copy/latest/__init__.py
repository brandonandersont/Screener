from .cnbcindonesia_lastest import CNBCIndonesia_latest

SCRAPERS = [CNBCIndonesia_latest]
SCRAPER_MAP = {
    "cnbcindonesia_latest": CNBCIndonesia_latest,
}   

__all__ = ["CNBCIndonesia_latest", "SCRAPERS", "SCRAPER_MAP"]
