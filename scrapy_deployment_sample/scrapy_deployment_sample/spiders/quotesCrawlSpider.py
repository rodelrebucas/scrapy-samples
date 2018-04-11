# -*- coding: utf-8 -*-

# Using a generic spider

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
from scrapy.http import FormRequest

class QuotesSpider(CrawlSpider):
    name = 'quotesCs'
    allowed_domains = ['toscrape.com', 'goodreads.com']
    login_url = ['http://quotes.toscrape.com/login']
    start_urls = ['http://quotes.toscrape.com']
    rules = [
        Rule(LxmlLinkExtractor(allow=(r'http://goodreads.com/author/show/\d+[\w\.]+')), callback='parse_goodreads_author'),
        Rule(LxmlLinkExtractor(allow=(r'/author/[\w\.]+')), callback='parse_quotes_author')
    ]


    # Override the start_requests method
    # to start with the login_url
    def start_request(self, response):
        yield Request(
            url=self.login_url,
            callback=self.login)


    def login(self, response):
        payload = {
            'username': 'scraper',
            'password': 'password'
        }
        yield FormRequest.from_response(
            response,
            formdata=payload,
            callback=super().start_request(response) 
            # Call the original start_request
            # to start processing start_urls 
        )


    def parse_goodreads_author(self, response):
        
        author_name = response.xpath('//h1[@class="authorName"]/span/text()').extract_first()        
        yield {
            'author_name_goodreads': author_name
        } 

    def parse_quotes_author(self, response):
        author_name = response.xpath('//h3[@class="author-title"]/text()').extract_first().strip()        
        yield {
            'author_name': author_name
        } 