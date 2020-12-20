# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from scrapy.exceptions import DropItem

class BbcscrapePipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://Gachengoh_001:CNnNy9zrDDCO9mp@cluster0.b1gxi.mongodb.net/bbcdb?retryWrites=true&w=majority")
        database = self.conn['bbcdb']
        self.collection = database['bbc_tb']

    def process_item(self, item, spider):

        self.collection.insert(dict(item))

        return item
