import scrapy

# 彼岸图壁纸
from netbian.items import NetbianItem

class BianspiderSpider(scrapy.Spider):
    name = 'bianSpider'
    start_urls = ['https://pic.netbian.com/']
    url_tmp = 'https://pic.netbian.com/%s/index%s%s.html'
    zone = ''

    images = 0

    zones = [
        '4kfengjing',
        '4kmeinv',
        '4kyouxi',
        '4kdongman',
        '4kyingshi',
        '4kmingxing',
        '4kqiche',
        '4kdongwu',
        '4krenwu',
        '4kmeishi',
        '4kzongjiao',
        '4kbeijing'

    ]

    def __init__(self):
        print('下载专区: (默认下载所有专区)')
        z = input('1、风景, 2、美女, 3、游戏, 4、动漫, 5、影视, 6、明星, 7、汽车, 8、动物, 9、人物, 10、美食, 11、宗教, 12、背景\n')
        self.zone = self.zones[int(z)-1]

        s = int(input('起始页: '))
        self.start = s
        self.end = int(input('终止页: '))
        # 处理第一页
        if s==1:
            s = (self.zone, '', '')
        else: s = (self.zone, '_', s)
        self.start_urls = [self.url_tmp%s]
        print("下载中...%s"%self.start_urls)

    def parse(self, response):

        resp = response.xpath("//*[@id='main']//ul[@class='clearfix']")
        hrefs = resp.xpath("li/a/@href").extract()
        for href in hrefs:
            yield scrapy.Request(url=response.urljoin(href), callback=self.parse_detail)

        print('------------------------当前第%s页------------------------'%self.start)

        if self.start==self.end:
            return

        self.start += 1
        yield scrapy.Request(url=self.url_tmp%(self.zone, '_', self.start), callback=self.parse)

    # 图片详情页
    def parse_detail(self, response):
        self.images += 1
        src = response.xpath("//a[@id='img']/img/@src").extract_first()
        src = response.urljoin(src)
        item = NetbianItem()
        item['image_urls'] = [src]

        yield item


    @staticmethod
    def close(spider, reason):
        print('下载OK! %s张图片'%spider.images)
        return super().close(spider, reason)

