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

class MySpider(scrapy.Spider):
    name = 'downloader'
    allowed_domains = ['github.com']
    def __init__(self,software,*args,**kwargs):
        super(MySpider,self).__init__(*args,**kwargs)
        if software == "v8":
            self.start_urls = ['https://github.com/v8/v8-git-mirror/releases']
        elif software == "tcpdump":
            self.start_urls = ['https://github.com/the-tcpdump-group/tcpdump/releases']
        elif software == "emacs":
            self.start_urls = ['https://github.com/emacs-mirror/emacs/releases']
        elif software == "openswan":
            self.start_urls = ['https://github.com/xelerance/Openswan/releases']
        elif software == "openjpeg":
            self.start_urls = ['https://github.com/uclouvain/openjpeg/releases']
        else:
            self.start_urls = ['https://github.com/%s/%s/releases' % (software,software)]

        self.software = software

    def parse(self,response):
        domain = 'https://github.com'
        sel = Selector(response)
        urls = sel.xpath('//ul[@class="tag-references"]/li[3]/a/@href').extract()
        for url in urls:
            basecommand = "wget -P %s " % self.software 
            command = basecommand + urljoin(domain,url)
            self.log(command)
            communicate(command)
        pages = sel.xpath('//div[@class="pagination"]/a[contains(.,"Next")]/@href').extract()
        for page in pages:
            yield scrapy.Request(page,callback=self.parse)
