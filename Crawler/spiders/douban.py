import json
import scrapy
import urllib.parse
from scrapy import Spider, Request
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import re
import time

'''
from Crawler.items import DoubanItem
class doubanSpider(scrapy.Spider):
    print("---------------")
    name = "douban"
    allowed_domain = ['douban.com']
    offset = 0
    last_number = 67095
    time_count = 0
    base_url = "https://www.douban.com/group/douban_wow/members?start="
    start_urls = ["https://www.douban.com/group/douban_wow/members?start=0"]
    #html = Request(start_url)
    #print( html.body)


    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        names = soup.select(".article .mod .member-list .name a")
        locations = soup.select(".article .mod .member-list .name .pl")
        for name, location in zip(names, locations):
            item = DoubanItem()
            item['name'] = name.get_text()
            item['url'] = name.get('href')
            location_text = location.get_text()
            if len(location_text) > 0:
                item['location'] = ''.join(re.findall('\((.*?)\)',location_text))
            else:
                item['location'] = location_text
            yield item
        if self.offset < self.last_number:
            self.offset += 35
        self.time_count += 1
        if self.time_count == 5:
            self.time_count = 0
            time.sleep(3)
        next_url = self.base_url + str(self.offset)
        next_url = urllib.parse.unquote(next_url)
        yield scrapy.Request(next_url, callback=self.parse)

    def start_login(self, response):
        login_url = "https://www.douban.com/accounts/login"
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        if len(response.xpath("//img[@id='captcha_image']/@src")) >0:
            urlretrieve(response.xpath("//img[@id='captcha_image']/@src").extract()[0],
                        "./captcha.jpg")  #download pactcha
            authcode = input("输入验证码: ")
            capid = response.xpath("//input[@name='captcha-id']/@value").extract()[0]
            form_data = {
                "form_email": "",
                "form_password": "",
                "captcha-solution": authcode,
                "captcha-id": capid
            }
            return scrapy.FormRequest.from_response(response, formdata=form_data, callable = self.parse)
        else:
            form_data = {
                "form_email": "",
                "form_password": ""
            }
            return scrapy.FormRequest.from_response(response, formdata=form_data, callable=self.parse)


'''












