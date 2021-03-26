LOG_LEVEL="WARNING"
USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

BOT_NAME = 'netbian'
SPIDER_MODULES = ['netbian.spiders']
NEWSPIDER_MODULE = 'netbian.spiders'

ROBOTSTXT_OBEY = False

# 使用scrapy内置的ImagesPipeline
ITEM_PIPELINES = {
   # 'bmw.pipelines.BmwPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1
}

# 使用无头浏览器处理js代码
# DOWNLOADER_MIDDLEWARES = {
#    'netbian.middlewares.SeleniumMiddleware': 543,
# }

# 配置文件的下载路径
IMAGES_STORE = r'D:\netbian\\'
