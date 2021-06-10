"""
Module.

<To be updated by developer>
"""

# from .web_scraper import WebScraper, WebScraper
# from .web_scraper import requestLink, requestLink

try:
    from .web_scraper import WebScraper, WebScraper
    from .web_scraper import requestLink, requestLink
#     from .web_scraper import request, WebScraper
#     from .web_scraper import parse, WebScraper
#     from .web_scraper import output, WebScraper
except ImportError:  # pragma: no cover
    from web_scraper import WebScraper, WebScraper
    from web_scraper import requestLink, requestLink
#     from web_scraper import request, WebScraper
#     from web_scraper import parse, WebScraper
#     from web_scraper import output, WebScraper

