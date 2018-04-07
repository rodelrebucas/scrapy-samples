# -*- coding: utf-8 -*-

# a standalone spider
# generated with:
#   $scrapy genspider spider_name domain_name
# run with:
#   $scrapy runspider spider_name 
import scrapy
from bs4 import BeautifulSoup, SoupStrainer

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.logger.info('Crawling this website: ' + response.url)


        # obtaining listing details
        # get the author details url
        author_urls = response.css('.author + a::attr(href)').extract()
        for url in author_urls
            author_abs_url = response.joinurl(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

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

        # following pagination
        # joining next url with the base url
        next_page = response.css('li.next > a::attr(href)').extract_first()
        
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)