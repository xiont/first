#encoding:utf-8
from scrapy.spider import Spider  
from scrapy.selector import Selector   
from first.items import TaobaoItem  
  
class DmozSpider(Spider):  
    name = "Taobao"  
    allowed_domains = ["zhihu.com"]  
    start_urls = [  
        "https://www.zhihu.com/" 
    ]  
    def start_requests(self):  
        for url in self.start_urls:          
            yield Request(url, cookies={'z_c0': 'Mi4wQURBQWJKamF1Z29BRU1DRHF5ZS1DUmNBQUFCaEFsVk5lNTh5V0FDeWpDMUdzRGV5RHdzQktiSElRM0Q2cjd1WXVR',
                                        'login':'MDRkZjI2NWQ3ZmQ5NDUxMjhhNDFiOTgyNjJjMDgzNjA',
                                        'l_n_c':'1',
                                        'a_t':'2.0ADAAbJjaugoXAAAAe58yWAAwAGyY2roKABDAg6snvgkXAAAAYQJVTXufMlgAsowtRrA3sg8LASmxyENw'})  
      
    def parse(self, response):  
        sel = Selector(response)  
        sites = sel.xpath('/html/body')  
        items = []  
        for site in sites:  
            item = TaobaoItem()  
            item['content'] = site.xpath('//title/text()').extract()  
            #item['url'] = site.xpath('@href').extract()  
            items.append(item)  
        return items  
