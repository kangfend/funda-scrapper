# Scrapy settings for funda project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'funda'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['funda.spiders']
NEWSPIDER_MODULE = 'funda.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
BASE_URL = 'http://www.funda.nl'
