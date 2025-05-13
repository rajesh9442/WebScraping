# Scrapy item definitions placeholder
import scrapy

class JobItem(scrapy.Item):
    id = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    posted_date = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    metadata = scrapy.Field()
