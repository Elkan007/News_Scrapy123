# -*- coding: utf-8 -*-

# Scrapy settings for News_Scrapy project

BOT_NAME = 'News_Scrapy'

SPIDER_MODULES = ['News_Scrapy.spiders']
NEWSPIDER_MODULE = 'News_Scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News_Scrapy (+http://www.yourdomain.com)'

ITEM_PIPELINES={
    'News_Scrapy.pipelines.NewsScrapyPipeline':300,
}
LOG_LEVEL='DEBUG'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'python'
MONGODB_COLLECTION = 'test'
