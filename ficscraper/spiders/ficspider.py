import scrapy
from ficscraper.items import FicItem

class FicspiderSpider(scrapy.Spider):
    name = "ficspider"
    allowed_domains = ['archiveofourown.org']
    start_urls = ['https://archiveofourown.org/tags/Re:%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E5%A7%8B%E3%82%81%E3%82%8B%E7%95%B0%E4%B8%96%E7%95%8C%E7%94%9F%E6%B4%BB%20%7C%20Re:Zero%20Starting%20Life%20in%20Another%20World%20(Anime)/works']
    custom_settings = {
        'FEEDS': {
            'ficsdata.json': {'format': 'json', 'overwrite': True},
        }
    }
    def parse(self, response):
        fics = response.css('li.work.blurb.group')
        for fic in fics:
            fic_item = FicItem()
            fic_item['name'] = fic.css('div h4 a::text').get(),
            fic_item['author'] = fic.css('div h4 a[rel="author"]::text').get(),
            fic_item['date'] = fic.css('div p::text').get(),
            fic_item['url'] = fic.css('div h4 a').attrib['href'],
            fic_item['language'] = fic.css('dl dd.language::text').get(),
            fic_item['words'] = fic.css('dl dd.words::text').get(),
            fic_item['chapters'] = fic.css('dl dd.chapters a::text').get(),
            fic_item['comments'] = fic.css('dl dd.comments a::text').get(),
            fic_item['kudos'] = fic.css('dl dd.kudos a::text').get(),
            fic_item['bookmarks'] = fic.css('dl dd.bookmarks a::text').get(),
            fic_item['hits'] = fic.css('dl dd.hits::text').get(),
            yield fic_item
        #nextPage = response.css('li.next a ::attr(href)').get()
        #if nextPage is not None:
            #nextPageURL = 'https://archiveofourown.org' + nextPage
            #yield response.follow(nextPageURL, callback= self.parse)