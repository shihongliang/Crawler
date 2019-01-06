# -*- coding: utf-8 -*-

# Scrapy settings for Crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Crawler'

SPIDER_MODULES = ['Crawler.spiders']
NEWSPIDER_MODULE = 'Crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
   #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
   #':authority' : 'www.zhihu.com'
   #'authorization': 'oauth c3cef7c66a1843fs8b3a9e6a1e3160e20',
   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   #'Accept-Language': 'en',
   #'Host' : 'www.zhihu.com',
   #'Referer' : 'https://www.zhdihu.com/topic/19555033/hot',
   #'cookie' : 'd_c0="AICCsdGr5AuPTjb-gEkUnAbY6qnX2F1_VSc=|1497104423"; _zap=1c4ef2ab-a297-4a4f-83ff-828189c952a7; q_c1=3ba974113ee94b0586a59420f1b9b269|1507877490000|1497104406000; __DAYU_PP=aZ3zI7IiaVraYIfInNzF25e200a969d6; _xsrf=xXUB8DXrbjdKlDAQqlQPc7MtHtzgvfyc; z_c0="2|1:0|10:1542877129|4:z_c0|92:Mi4xeHNGcEFRQUFBQUFBZ0lLeDBhdmtDeVlBQUFCZ0FsVk55YjNqWEFDYXp5aUhCbFpOSVdldTRHY0YyZjBQSFJ5V2xR|4b78813560f0ffac4ce268512ab12b80aa0d05eb918f580bd00bfea64dc52460"; tst=r; q_c1=3ba974113ee94b0586a59420f1b9b269|1543115002000|1497104406000; __utmv=51854390.100-1|2=registration_date=20150428=1^3=entry_date=20150428=1; __utma=51854390.1196758070.1544272036.1544272036.1544342570.2; __utmz=51854390.1544342570.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; tgw_l7_route=156dfd931a77f9586c0da07030f2df36'
#}
DEFAULT_REQUEST_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'Crawler.middlewares.CrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Crawler.middlewares.CrawlerDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Crawler.pipelines.CrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

ITEM_PIPELINES = {
   'Crawler.pipelines.zhihuPipeline': 300,
   #'Crawler.pipelines.doubanPipeline': 300,
}

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
