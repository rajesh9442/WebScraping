# MongoDB pipeline logic placeholder
import pymongo
from scrapy.exceptions import DropItem

class MongoPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["scraper_db"]
        self.collection = self.db["jobs"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.collection.find_one({"id": item["id"]}):
            raise DropItem("Duplicate item found.")
        self.collection.insert_one(dict(item))
        return item
