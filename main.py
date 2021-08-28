import scrapy
from scrapy.crawler import CrawlerProcess


SEARCH_URL = "https://th.indeed.com/jobs?q=%22data+engineer%22&l=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3"


class MySpider(scrapy.Spider):
    name = "indeed_spider"
    start_urls = [SEARCH_URL,]

    def parse(self, response):
        job_links = response.css("#mosaic-provider-jobcards a")
        for each in job_links:
            if "id" not in each.attrib:
                continue

            url = each.attrib["href"]
            jk = url.split("&")[0].split("=")[1]
            job_url = f"{SEARCH_URL}&vjk={jk}"

            title = each.css(".jobTitle span::attr(\"title\")").get()
            company_name = each.css(".companyName::text").get()
            company_location = each.css(".companyLocation::text").get()

            print(title, company_name, company_location, job_url)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
