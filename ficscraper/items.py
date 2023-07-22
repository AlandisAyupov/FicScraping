import scrapy


class ScraperItem(scrapy.Item):
    name = scrapy.Field()
    pass

class FicItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    language = scrapy.Field()
    words = scrapy.Field()
    chapters = scrapy.Field()
    comments = scrapy.Field()
    kudos = scrapy.Field()
    bookmarks = scrapy.Field()
    hits = scrapy.Field()
