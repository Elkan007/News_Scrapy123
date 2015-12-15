#!/usr/bin/env python
# coding=utf-8

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from News_Scrapy.items import NewsScrapyItem

class NetEaseSpider(CrawlSpider):
    name = "News_Scrapy"
    allowed_domains = ["news.163.com"]
    start_urls = ["http://news.163.com"]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'http://news.163.com/[a-zA-Z]/'))),
        Rule(SgmlLinkExtractor(allow=(r'http://news.163.com/[0-9]{2}/[0-9]{3,4}/[0-9]{1,2}/[a-zA-Z0-9]+.html')),callback="parse_item"),
    ]

    def parse_item(self,response):
        sel_resp = Selector(response)
        news_item = NewsScrapyItem()
        tmp = response.url.split("/")[2]
        news_item["news_type"] = tmp.split(".")[0]
        news_item["news_title"] = sel_resp.xpath('//*[@id="h1title"]/text()').extract()
        news_item["news_date"] = sel_resp.xpath('//*[@id="epContentLeft"]/div[1]/div[1]/text()').re(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}')
        news_item["news_source"] = sel_resp.xpath('//*[@id="ne_article_source"]/text()').extract()
        news_item["news_content"] = sel_resp.xpath('//*[@id="endText"]').extract()
        return news_item


