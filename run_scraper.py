# Script to run the scraper
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_scraper.spiders.job_spider import JobSpider

process = CrawlerProcess(get_project_settings())
process.crawl(JobSpider)
process.start()
