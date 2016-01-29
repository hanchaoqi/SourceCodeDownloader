# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from subprocess import Popen,PIPE
from multiprocessing.dummy import Pool as ThreadPool
from urlparse import urljoin

def communicate(commandLine):
    process = Popen(commandLine,stdout=PIPE,stderr=PIPE,shell=True)
    return process.communicate()

class TcpdumpSpider(scrapy.Spider):
    name = 'tcpdump'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/the-tcpdump-group/tcpdump/releases']

    def parse(self,response):
        domain = 'https://github.com'
        sel = Selector(response)
        urls = sel.xpath('//ul[@class="tag-references"]/li[3]/a/@href').extract()
        for url in urls:
            command = "wget -P tcpdump " + urljoin(domain,url)
            self.log(command)
            communicate(command)
        pages = sel.xpath('//div[@class="pagination"]/a[contains(.,"Next")]/@href').extract()
        for page in pages:
            yield scrapy.Request(page,callback=self.parse)
