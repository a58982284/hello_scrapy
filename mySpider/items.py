import scrapy


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    #level = scrapy.Field()
    info = scrapy.Field()
