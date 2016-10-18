# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
import sys
import os

# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# from scrapy import logging
import logging
# from w3school.items import W3schoolItem
from w3school.items import W3SchoolItem

logger = logging.getLogger("W3schoolSpider")

class W3schoolSpider(Spider):
    """爬取w3school标签"""
    # log.start("log",loglevel='INFO')
    name = "w3school"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]

    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        items = []

        for site in sites:
            item = W3SchoolItem()

            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('a/@title').extract()

            print("title==", title)
            print("link==", link)
            print("desc==", desc)

            # item['title'] = [title]
            # item['link'] = [link]
            # item['desc'] = [desc]
            item['title'] = [t.encode('utf-8') for t in title]
            item['link'] = [l.encode('utf-8') for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            items.append(item)

            # 记录
            logger.info("Appending item...")
            # logging.log("Appending item...", level='INFO')
            # log.msg("Appending item...", level='INFO')
        logger.info("Append done.")
            # logging.log("Append done.", level='INFO')
        return items
