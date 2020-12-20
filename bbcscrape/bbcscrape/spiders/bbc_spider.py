import scrapy
from ..items import BbcscrapeItem


class BBCSpider(scrapy.Spider):
    name = 'bbc'
    start_urls = [
        'https://www.bbc.com/'
    ]

    def parse(self, response):

        items = BbcscrapeItem()
        all_media = response.css('ul.media-list')
        for i in all_media:

            title = i.css('.media__link::text').extract()
            summary = i.css('.media__summary::text').extract()
            tags = i.css('.tag--news::text').extract()

            items['title'] = title
            items['summary'] = summary
            items['tags'] = tags

            yield items

