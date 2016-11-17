# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LjESItem(scrapy.Item):
    region = scrapy.Field() #区域
    position = scrapy.Field()#位置

    title = scrapy.Field()
    total_price = scrapy.Field()  # 总价
    unit_price = scrapy.Field()  # 单价
    first_pay_fee = scrapy.Field()  # 首付
    # tax_fee = scrapy.Field()  # 税费
    house_year = scrapy.Field()  # 建成年代

    house_style = scrapy.Field()  # 户型
    house_area = scrapy.Field()  # 面积
    house_fact_area = scrapy.Field()  # 套内面积
    house_direction = scrapy.Field()  # 朝向
    house_decorate = scrapy.Field()  # 装修
    house_heating_type = scrapy.Field()  # 供暖方式
    house_floor = scrapy.Field()  # 楼层
    house_structure = scrapy.Field()  # 户型结构
    house_building_type=scrapy.Field()#建筑类型
    house_building_structure = scrapy.Field()#建筑结构
    house_elevator_ratio = scrapy.Field()#梯户比例
    house_elevator = scrapy.Field()# 配备电梯

    #transaction atrr
    house_begin_sell = scrapy.Field()  # 挂牌时间
    house_trans_ownership = scrapy.Field()  # 交易权属
    house_purpose = scrapy.Field()  # 房屋用途
    house_full_five = scrapy.Field()  # 满5年
    house_ownership = scrapy.Field()  # 产权所属
    morgage_info = scrapy.Field()  # 是否抵押

    community_name = scrapy.Field()  # 小区名称
    area_name = scrapy.Field()  # 地理位置
    ditei_info = scrapy.Field()#地铁信息

    core_selling_point=scrapy.Field()#核心卖点
    house_type_intro=scrapy.Field()#户型介绍
    arround_support=scrapy.Field()#周边配套
    traffic_info = scrapy.Field()#交通出行
    tax_intro = scrapy.Field()#税费解析
    decorate_desc = scrapy.Field()#装修描述
    community_intro = scrapy.Field()#小区介绍
    mortgage_ownership=scrapy.Field()#权属抵押

    page_url = scrapy.Field()  # 页面地址

class LjCjItem(scrapy.Item):
    page_url = scrapy.Field()  # url
    title = scrapy.Field()  # 小区 大小
    total_price = scrapy.Field()  # 总价
    unit_price = scrapy.Field()  # 单价
    house_style = scrapy.Field()  # 户型
    house_floor = scrapy.Field()  # 楼层
    house_direction = scrapy.Field()  # 朝向
    house_structure = scrapy.Field()  # 户型结构
    house_area = scrapy.Field()  # 面积
    house_year = scrapy.Field()  # 建成年代

    community_name = scrapy.Field()  # 小区名称
    area = scrapy.Field()  # 区域:东城 朝阳等
    location = scrapy.Field()  # 位置

    deal_data = scrapy.Field()  # 成交日期
    deal_house_txt = scrapy.Field()  # 满5年
    sell_flag = scrapy.Field()

