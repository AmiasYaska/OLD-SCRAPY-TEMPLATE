import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"
    allowed_domains = ["exampe.com"]
    start_urls = ["https://exampe.com"]

    def parse(self, response):
        pass
