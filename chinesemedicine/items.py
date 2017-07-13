# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field
class ChinesemedicineItem(Item):
        medicineName = Field()  # 药名
        overView = Field()#概述
        basicInfo = Field()#基本信息
        subTitle= Field()
