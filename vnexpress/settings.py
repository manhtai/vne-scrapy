# -*- coding: utf-8 -*-

BOT_NAME = 'vnexpress'

SPIDER_MODULES = ['vnexpress.spiders']
NEWSPIDER_MODULE = 'vnexpress.spiders'

CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED=False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'vi,en-US',
}

ITEM_PIPELINES = {
   'vnexpress.pipelines.RequiredFieldsPipeline': 200,
   'vnexpress.pipelines.MakeStringsPipeline': 400,
   'vnexpress.pipelines.MysqlPipeline': 600,
}

# Dynamic throttle
AUTOTHROTTLE_ENABLED=True
AUTOTHROTTLE_START_DELAY=2
AUTOTHROTTLE_MAX_DELAY=60
AUTOTHROTTLE_DEBUG=False

# MySQL
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'vne'
MYSQL_USER = 'vne'
MYSQL_PASSWD = ''
