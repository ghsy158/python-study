# -*-coding:utf8-*-

import scrapy
from scrapy.spiders import CrawlSpider
from tutorials.items import LjItem
import json

# Some User Agents
headers = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}, \
           {
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}, \
           {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}, \
           {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}, \
           {
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}, \
           {
               'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
           {
               'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
           {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}, \
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}, \
           {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}, \
           {
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}, \
           {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'}, \
           {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ['http://bj.lianjia.com/ershoufang/']

    def parse(self, response):
        # self.log("=========parse url ", response.url)
        lists = response.css('ul[class="listContent"] li')
        for list in lists:
            url = list.css("a[class='img']::attr(href)").extract()[0]
            ## 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
            # self.log('process_url:', url)
            yield scrapy.Request(url, callback=self.parse_content)

        ## 是否还有下一页，如果有的话，则继续
        pageData = response.css(".house-lst-page-box::attr(page-data)").extract()[0]
        page = json.loads(pageData)
        totalPage = page['totalPage']
        curPage = page['curPage']
        if totalPage != curPage:
            nextPage = "http://bj.lianjia.com/ershoufang/pg" + str(curPage+1)
            print("当前页面:", nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)

    def parse_content(self, response):
        # self.log('ershoufang_detail_url:', response.url)
        item = LjItem()
        introContent = response.css("div[class='introContent']")
        baseInfo = introContent.css("div[class='base']")
        item['page_url'] = response.url
        item['house_style'] = baseInfo.css("div[class='content'] li::text")[0].extract()
        item['house_area'] = baseInfo.css("div[class='content'] li::text")[2].extract()
        item['title'] = response.css("div[class='content']").css("div[class='title']").css(
            "h1[class='main']::text").extract()[0]
        # print("item===", item)
        yield item
