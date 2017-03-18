# -*-coding:utf8-*-

import scrapy
from scrapy.spiders import CrawlSpider
from tutorials.items import LjCjItem
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
    name = "lianjiaCj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ['http://bj.lianjia.com/chengjiao/']

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
            nextPage = "http://bj.lianjia.com/ershoufang/pg" + str(curPage + 1)
            print("当前页数:", nextPage)
            yield scrapy.Request(nextPage, callback=self.parse)

    def parse_content(self, response):
        # self.log('ershoufang_detail_url:', response.url)
        print("当前解析页面:", response.url)
        item = LjCjItem()
        item['title'] = response.css("div[class='content']").css("div[class='title']").css(
            "h1[class='main']::text").extract()[0]

        item['total_price'] = response.css(".total::text").extract()[0] + "万"
        item['unit_price'] = response.css(".unitPriceValue::text").extract()[0] + '元/平米'
        item['first_pay_fee'] = response.css(".tax>span::text")[0].extract()
        item['house_year'] = response.css(".area>.subInfo::text").extract()[0].split('/')[0]

        introContent = response.css("div[class='introContent']")
        baseInfo = introContent.css("div[class='base']")

        item['house_style'] = baseInfo.css("div[class='content'] li::text")[0].extract()
        item['house_area'] = baseInfo.css("div[class='content'] li::text")[2].extract()
        item['house_fact_area'] = baseInfo.css("div[class='content'] li::text")[4].extract()
        item['house_direction'] = baseInfo.css("div[class='content'] li::text")[6].extract()
        item['house_decorate'] = baseInfo.css("div[class='content'] li::text")[8].extract()
        item['house_heating_type'] = baseInfo.css("div[class='content'] li::text")[10].extract()
        item['house_floor'] = baseInfo.css("div[class='content'] li::text")[1].extract()
        item['house_structure'] = baseInfo.css("div[class='content'] li::text")[3].extract()
        item['house_building_type'] = baseInfo.css("div[class='content'] li::text")[5].extract()
        item['house_building_structure'] = baseInfo.css("div[class='content'] li::text")[7].extract()
        item['house_elevator_ratio'] = baseInfo.css("div[class='content'] li::text")[9].extract()
        item['house_elevator'] = baseInfo.css("div[class='content'] li::text")[11].extract()

        transInfo = introContent.css("div[class='transaction']")

        item['house_begin_sell'] = transInfo.css("div[class='content'] li::text")[0].extract()  # 挂牌时间
        item['house_trans_ownership'] = transInfo.css("div[class='content'] li::text")[1].extract()  # 交易权属
        item['house_purpose'] = transInfo.css("div[class='content'] li::text")[3].extract()  # 房屋用途
        item['house_full_five'] = transInfo.css("div[class='content'] li::text")[4].extract()  # 满5年
        item['house_ownership'] = transInfo.css("div[class='content'] li::text")[5].extract()  # 产权所属
        item['morgage_info'] = transInfo.css("div[class='content'] li")[6].css("span::text")[1].extract()  # 抵押信息

        item['community_name'] = response.css(".communityName>a::text").extract()[0]  # 小区名称
        if response.css(".supplement::text").extract():
            item['ditei_info'] = response.css(".supplement::text").extract()[0]  # 地铁信息

        areaList = response.css(".areaName>.info>a")
        areaName = ""
        for areaInfo in areaList:
            area = areaInfo.css("::text").extract()[0]
            areaName += area + ' '
        item['area_name'] = areaName  # 区域
        item['page_url'] = response.url

        # print("item===", item)
        yield item
