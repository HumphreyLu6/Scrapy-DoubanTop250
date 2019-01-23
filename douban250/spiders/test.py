# -*- coding: utf-8 -*-
#import imp
#scrapy = imp.load_source('scrapy', 'C:\Python27amd64\Scripts\scrapy.exe')
#from C:\Python27amd64\Scripts import scrapy
import sys
sys.path.append('C:\Python27amd64\Scripts\scrapy')
import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    #allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        list_a = response.xpath('//div[@class = "hd"]/a')

        for a in list_a:
            print(a.xpath('span[1]/text()').extract(), a.xpath('@href').extract())

        nextpage = response.xpath('//span[@class = "next"]/a/@href').extract()

        if nextpage:
            nexturl = 'https://movie.douban.com/top250%s'%nextpage[0]

            yield Request(url = nexturl, callback = self.parse)

