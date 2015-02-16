# Scrapy settings for hrtencent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'segment'

SPIDER_MODULES = ['segment.spiders']
NEWSPIDER_MODULE = 'segment.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hrtencent (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    'segment.pipelines.JsonWithEncodingPipeline': 300,
}

LOG_LEVEL = 'INFO'

