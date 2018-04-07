import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotesjs'
    

    def parse(self, response):
        self.logger.info('Crawling this website: ' + response.url)



        # Using css selectors
        # extract all quotes from the page
        # but yield each data individually
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tag': quote.css('a.tag::text').extract()
            }   
            yield item
