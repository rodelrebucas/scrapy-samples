# -*- coding: utf-8 -*-

# Using a generic spider
# Extract and follow external links as long as it follow the Rule specified


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
        Rule(LxmlLinkExtractor(allow=(), process_value='external'), callback='parse_goodreads_author'),
        # for every response extract this pattern
        # if this link is extracted, should we follow again and proceed with parsing the next response? True
        # Rule(LxmlLinkExtractor(allow=(), restrict_xpaths=('//li[@class="next"]')), follow=True), 
        # for every response extract this link pattern
        # Rule(LxmlLinkExtractor(allow=(r'/author/[\w\.]+')), callback='parse_quotes_author')
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

    def external(value):
        self.logger.info('***** -->> %s' % value)
        

    def parse_goodreads_author(self, response):
        
        self.logger.info('********************')

        for link in LxmlLinkExtractor(allow=(r'http://goodreads.com/author/show/\d+\.[\w\_]+'),deny = self.allowed_domains).extract_links(response):
            self.logger.info('********** %s' % link.url)

        author_name = response.xpath('//h1[@class="authorName"]/span/text()').extract_first()        
        yield {
            'author_name_goodreads': author_name
        } 

    def parse_quotes_author(self, response):
        author_name = response.xpath('//h3[@class="author-title"]/text()').extract_first().strip()        
        yield {
            'author_name': author_name
        } 