# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class NetbianPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        image_guid = "hello"
        filename = '{0}'.format(image_guid)
        print(filename)
        return filename

