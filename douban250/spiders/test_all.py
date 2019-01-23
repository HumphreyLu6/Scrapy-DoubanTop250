import sys
sys.path.append('C:\Python27amd64\Scripts\scrapy')
import scrapy

class TestSpider(scrapy.Spider):
    name = 'test_all'
    start_urls = ['http://movie.douban.com/top250']

    def parse(self,response):
        list_a = response.xpath('//div[@class = "hd"]/a')

        for a in list_a:
            href = a.xpath('@href').extract()[0]
            movie_name = a.xpath('span[1]/test()').extract()[0]
            dinfo = {'movie_name': movie_name}

            yield Request(url = href, meta=dinfo, callback = self.detail_parse)

        nextpage = response.xpath('//span[@class = "next"]/a/@href').extract()[0]
        if nextpage:
            nexturl = nextpage[0]
            nexturl = 'http://movie.douban.com/top250%s'%nextpage

            yield Request(url=nexturl, callback = self.parse)

    def getinfobyre(self,instr, restr):
        m = re.search(restr, instr, re.S)

        if m:
            info = m.groups()[0]
        else:
            info = ""

        return info

    def details_parse(self, response):
        dinfo = response.meta
        iteml = ItemLoader(item = Douban250Item(), response = response)
        item.add_value('movie_name',dinfo['movie_name'])
        item.add_xpath('movie_directors', '//a[@rel = "v:directedBy"]/text()')
        item.add_xpath('movie_actors', '//a[@rel = "v:starring"]/text()')
        item.add_xpath('movie_type', '//span[@property = "v:genre"]/text()')
        item.add_xpath('movie_showdate', '//span[@property = "v:initialReleaseDate"]/text()')
        item.add_xpath('movie_runtime', '//span[@property = "v:runtime"]/text()')
        showplace = self.getifobyre(response.text,r'制片国家/地区：</span>(.+?)<br/>')
        item.add_value('movie_showplace',showplace)
        language = self.getinfobyre(response.text, r'语言：</span>(.+?)<br/>')
        item.add_value('movie——language',language)
        language = self.getinfobyre(response.text, r'又名：</span>(.+?)<br/>')
        item.add_value('movie_othername',othername)
        item.add_xpath('movie_score', '//strong[@property = "v:average"]/text()')
        item.add_xpath('movie_vote', '//span[@property = "v:votes"]/text()')
        return iteml.load_item()
        