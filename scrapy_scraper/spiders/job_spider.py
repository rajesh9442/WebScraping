# Job spider code placeholder
import scrapy
from scrapy.http import Request
from hashlib import sha256
from datetime import datetime
from common.utils import generate_id, validate_item

class JobSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/jobs?page=1"]

    def parse(self, response):
        jobs = response.css("div.job-posting")
        for job in jobs:
            url = response.urljoin(job.css("a::attr(href)").get())
            title = job.css("a::text").get()
            item = {
                "source": "example.com",
                "url": url,
                "title": title,
                "description": job.css("p.description::text").get(),
                "posted_date": job.css("span.date::attr(datetime)").get(),
                "location": job.css("span.location::text").get() or "Remote",
                "company": job.css("span.company::text").get(),
                "salary": job.css("span.salary::text").get() or "N/A",
                "metadata": {
                    "scraped_at": datetime.utcnow().isoformat(),
                    "tags": ["full-time"]
                }
            }
            item["id"] = generate_id(url, title)
            if validate_item(item):
                yield item

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield Request(url=response.urljoin(next_page), callback=self.parse)
