# Basic Settings
BOT_NAME = 'scrapy_scraper'

SPIDER_MODULES = ['scrapy_scraper.spiders']
NEWSPIDER_MODULE = 'scrapy_scraper.spiders'

# Obey robots.txt
ROBOTSTXT_OBEY = True

# Download delay for rate limiting (anti-ban)
DOWNLOAD_DELAY = 3  # seconds
RANDOMIZE_DOWNLOAD_DELAY = True

# Concurrency
CONCURRENT_REQUESTS = 8

# User-Agent Rotation Middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy_scraper.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy_scraper.middlewares.ProxyMiddleware': 410,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# List of User Agents
USER_AGENTS_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    # Add more as needed
]

# List of Proxies
PROXY_LIST = [
    "http://proxy1.example.com:8000",
    "http://proxy2.example.com:8000",
    # Add actual working proxies
]

# Pipeline Configuration
ITEM_PIPELINES = {
    'scrapy_scraper.pipelines.MongoPipeline': 300,
}

# MongoDB Configuration
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'scraper_db'
MONGO_COLLECTION = 'jobs'

# AutoThrottle (adaptive rate limiting)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0

# HTTP Caching (optional)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 24 hours
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [403, 429]

# Logging
LOG_LEVEL = 'INFO'
