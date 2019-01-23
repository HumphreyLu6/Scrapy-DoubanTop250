# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import sys
sys.path.append('C:\Python27amd64\Scripts\scrapy')
import scrapy

def mysplit(info):
    return info.split('/')


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field(output_processor = Join())
    movie_directors = scrapy.Field(output_processor = Join())
    movie_actors = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join('/'))
    movie_type = scrapy.Field(output_processor = Join())
    movie_showdate = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    movie_runtime = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    movie_showplace = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    movie_language = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    movie_othername = scrapy.Field(input_processor = MapCompose(mysplit, str.strip), output_processor = Join())
    movie_score = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    movie_vote = scrapy.Field(input_processor = MapCompose(str.strip), output_processor = Join())
    
