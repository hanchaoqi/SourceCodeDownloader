# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from Downloader.items import DownloaderItem


class QemuSpider(CrawlSpider):
    name = 'qemu'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/qemu/qemu/releases']

    rules = (
        Rule(LinkExtractor(allow=r'/qemu/qemu/archive/.*\.tar\.gz'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://github.com/qemu/qemu/releases\?.*',restrict_xpaths='//div[@class="pagination"]/a[contains(.,"Next")]'),follow=True),
    )

    def parse_item(self, response):
        i = DownloaderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
