import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
    name = "test"


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
