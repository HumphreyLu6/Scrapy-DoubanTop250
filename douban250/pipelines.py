# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Douban250Pipeline(object):
    def open_spider(self, spider):
        self.save = open('top250.txt','w', encoding='utf-8')

    def close_spider(self, spider):
        self.save.close()


    def process_item(self, item, spider):
        info = ''
        for i in item.values():
            info += ',' + i

        self.save.write(info)
        self.save.write("\n")
        return item
