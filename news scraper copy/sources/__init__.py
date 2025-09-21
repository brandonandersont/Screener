from .cnbcindonesia import CNBCIndonesia
from .detikfinance import DetikFinance
from .emitennews import EmitenNews
from .idxchannel import IDXChannel
from .kontan import Kontan


SCRAPERS = [CNBCIndonesia, DetikFinance, EmitenNews, IDXChannel, Kontan]
SCRAPER_MAP = {
    "cnbc": CNBCIndonesia,
    "detikfinance": DetikFinance,
    "emitennews": EmitenNews,
    "idxchannel": IDXChannel,
    "kontan": Kontan,
   
}

__all__ = ["CNBCIndonesia", "DetikFinance", "EmitenNews", "IDXChannel", "Kontan", "SCRAPERS", "SCRAPER_MAP"]
