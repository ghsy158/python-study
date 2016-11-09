# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()  # 主题
    publish = scrapy.Field()  # 发布时间
    involves = scrapy.Field()  # 参与人数
    comments = scrapy.Field()  # 评论人数
    keywords = scrapy.Field()  # 新闻关键词
    pic_title = scrapy.Field()  # 图片标题
    author = scrapy.Field()  # 文章作者
    hot = scrapy.Field()  # 热度


class SpecItem(scrapy.Item):
    url = scrapy.Field()
    kind = scrapy.Field()
    rank = scrapy.Field()
    gold = scrapy.Field()
    silver = scrapy.Field()
    bronze = scrapy.Field()
    total = scrapy.Field()
    country = scrapy.Field()


class ZpItem(scrapy.Item):
    url = scrapy.Field()
    zwmc = scrapy.Field()
    zwfl = scrapy.Field()
    zwlb = scrapy.Field()
    zwyx = scrapy.Field()
    zwnx = scrapy.Field()
    fbrq = scrapy.Field()
    gshy = scrapy.Field()
    gsxz = scrapy.Field()
    gsgm = scrapy.Field()
    yx_low = scrapy.Field()
    yx_high = scrapy.Field()
    yx_avg = scrapy.Field()
    gsmc = scrapy.Field()
    gsdz = scrapy.Field()
    gzdd = scrapy.Field()
    gzjy = scrapy.Field()
    xl = scrapy.Field()
    jy_low = scrapy.Field()
    jy_high = scrapy.Field()
    jy_avg = scrapy.Field()


class ZlzpItem(scrapy.Item):
    zwmc = scrapy.Field()  # 职位名称
    zwyx = scrapy.Field()  # 职位月薪
    zwnx = scrapy.Field()  # 职位年薪
    gzdd = scrapy.Field()  # 工作地点
    fbrq = scrapy.Field()  # 发布日期
    gzjy = scrapy.Field()  # 工作经验
    zdxl = scrapy.Field()  # 最低学历
    gzxz = scrapy.Field()  # 工作性质
    zwlb = scrapy.Field()  # 职位类别
    gsmc = scrapy.Field()  # 公司名称
    gsgm = scrapy.Field()  # 公司规模
    gsxz = scrapy.Field()  # 公司性质
    gshy = scrapy.Field()  # 公司行业
    gszy = scrapy.Field()  # 公司主页
    gsdz = scrapy.Field()  # 公司地址
    url = scrapy.Field()  # 页面地址


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class CjHouseItem(scrapy.Item):
    page_url = scrapy.Field()  # url
    title = scrapy.Field()  # 小区 大小
    house_info = scrapy.Field()  # 朝向 装修
    deal_data = scrapy.Field()  # 成交日期
    total_price = scrapy.Field()  # 总价
    position_icon = scrapy.Field()  # 低楼层 2007年 塔楼
    unit_price = scrapy.Field()  # 单价
    deal_house_txt = scrapy.Field()  # 满5年
    sell_flag = scrapy.Field()


class HouseItem(scrapy.Item):
    total_price = scrapy.Field()  # 总价
    unit_price = scrapy.Field()  # 单价
    down_payment = scrapy.Field()  # 首付
    tax = scrapy.Field()  # 税费
    house_type = scrapy.Field()  # 居室
    house_year = scrapy.Field()
    house_layout = scrapy.Field()  # 楼层
    house_direction = scrapy.Field()  # 朝向
    house_decorate = scrapy.Field()  # 装修
    house_area = scrapy.Field()  # 面积
    house_fact_area = scrapy.Field()  # 实际面积
    house_begin_sell = scrapy.Field()  # 挂牌时间
    house_purpose = scrapy.Field()  # 房屋用途
    house_transacton = scrapy.Field()  # 交易权属
    house_full_five = scrapy.Field()  # 满5年
    house_unique = scrapy.Field()  # 是否唯一
    community_name = scrapy.Field()  # 小区名称
    area_name = scrapy.Field()  # 地理位置
    school_name = scrapy.Field()  # 学校
    morgage = scrapy.Field()  # 是否抵押
    sell_flag = scrapy.Field()
    page_url = scrapy.Field()


class LjESItem(scrapy.Item):
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

