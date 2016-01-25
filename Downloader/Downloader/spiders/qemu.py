# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
#from Downloader.items import DownloaderItem
from subprocess import Popen,PIPE
from multiprocessing.dummy import Pool as ThreadPool
from urlparse import urljoin

def communicate(commandLine):
    process = Popen(commandLine,stdout=PIPE,stderr=PIPE,shell=True)
    return process.communicate()

class QemuSpider(CrawlSpider):
    name = 'qemu'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/qemu/qemu/releases']

    rules = (
        #Rule(LinkExtractor(allow=r'/qemu/qemu/archive/.*\.tar\.gz'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://github.com/qemu/qemu/releases\?.*',restrict_xpaths='//div[@class="pagination"]/a[contains(.,"Next")]'),callback='prase_item',follow=True),
    )

    def parse_item(self, response):
        domain = 'https://github.com'
        sel = Selector(response)
        urls = sel.xpath('//ul[@class="tag-references"]/li[3]/a/@href').extract()
        for url in urls:
            command = "wget -P qemu " + url
            self.logger.info(command)
            communicate(command)
        return 
