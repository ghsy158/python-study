# -*-coding:utf8-*-

import scrapy
from scrapy.spiders import CrawlSpider,Rule
from tutorials.items import LjESItem
from scrapy.linkextractors import LinkExtractor

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

    # rules = (
    #     Rule(LinkExtractor(allow='ershoufang', ), follow=True),
    #     Rule(LinkExtractor(allow='chengjiao/[a-zA-Z0-9]*/', ), callback='parseList', follow=True),
    #     Rule(LinkExtractor(allow='ershoufang/[0-9]*\.html', ), callback='parseDetail', follow=True),
    # )

    def parse(self, response):
        regionList = response.css(".position>dl:nth-child(2) > dd > div:nth-child(1) > div:nth-child(1)>a")
        baseUrl = 'http://bj.lianjia.com'
        for region in regionList:
            regionName = region.css("::text").extract()[0]
            url = region.css("::attr(href)").extract()[0]
            pageUrl = baseUrl+url
            print("当前区域:",regionName,pageUrl)
            request = scrapy.Request(pageUrl,callback=self.parsePosition)
            item = LjESItem()
            item['region'] = regionName
            request.meta['item']=item #相当于放到了session里面
            yield request
            # yield scrapy.Request(pageUrl, callback=lambda response,regionName=regionName: self.parsePosition(response,regionName))

    def parsePosition(self,response):
        positionList = response.css("body > div.m-filter > div.position > dl:nth-child(2) > dd > div:nth-child(1) > div:nth-child(2)>a")
        baseUrl = 'http://bj.lianjia.com'
        item = response.meta['item']
        for position in positionList:
            positionName = position.css("::text").extract()[0]
            positionUrl = position.css("::attr(href)").extract()[0]
            positionUrl = baseUrl+positionUrl
            print("当前位置:", positionName, positionUrl)

            request = scrapy.Request(positionUrl, callback=self.parseList)
            item['position'] = positionName
            request.meta['item'] = item
            yield request
            # yield scrapy.Request(positionUrl, callback=lambda response,regionName=regionName,positionName=positionName: self.parseList(response, regionName,positionName))

    def parseList(self, response):
        # print(response.body)
        lists = response.css('ul[class="sellListContent"] li')
        item = response.meta['item']
        for list in lists:
            # url = list.css("a[class='img']::attr(href)").extract()[0]
            detail_url = list.css("div.info.clear > div.title > a::attr(href)").extract()[0]
            ## 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
            # self.log('process_url:', url)
            request = scrapy.Request(detail_url, callback=self.parseDetail)
            request.meta['item'] = item
            yield request
            # yield scrapy.Request(url, callback=self.parseDetail)

        ## 是否还有下一页，如果有的话，则继续
        pageData = response.css(".house-lst-page-box::attr(page-data)").extract()[0]
        page = json.loads(pageData)
        totalPage = page['totalPage']
        curPage = page['curPage']
        if totalPage != curPage:
            nextPage = "http://bj.lianjia.com/ershoufang/pg" + str(curPage + 1)
            print("当前页数:", nextPage)
            yield scrapy.Request(nextPage, callback=self.parseList)

    def parseDetail(self, response):
        # self.log('ershoufang_detail_url:', response.url)
        print("当前解析页面:", response.url)
        item = response.meta['item']
        # item = LjESItem()
        # item['regionName']=regionName
        # item['positionName']=positionName

        item['title'] = response.css("div[class='content']").css("div[class='title']").css(
            "h1[class='main']::text").extract()[0]

        item['total_price'] = response.css(".total::text").extract()[0] + "万"
        item['unit_price'] = response.css(".unitPriceValue::text").extract()[0] + '元/平米'
        item['first_pay_fee'] = response.css(".tax>span::text")[0].extract()
        if response.css(".area>.subInfo::text").extract()[0].split('/')[0]:
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

        moreList = response.css(".showbasemore>.baseattribute")
        for info in moreList:
            name = info.css(".name::text").extract()[0]
            content = info.css(".content::text").extract()[0].replace(" ", "").replace("\n", "")

            if name == "核心卖点":
                item['core_selling_point'] = content
            elif name == "户型介绍":
                item['house_type_intro'] = content
            elif name == "周边配套":
                item['arround_support'] = content
            elif name == "交通出行":
                item['traffic_info'] = content
            elif name == "税费解析":
                item['tax_intro'] = content
            elif name == "装修描述":
                item['decorate_desc'] = content
            elif name == "小区介绍":
                item['community_intro'] = content
            elif name == "权属抵押":
                item['mortgage_ownership'] = content

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
