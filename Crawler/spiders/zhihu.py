import json
import scrapy
import urllib.parse
from scrapy import Spider, Request
from Crawler.items import UserItem
import time
class zhihuSpider(scrapy.Spider):
    print("============")
    name = "zhihu"
    allowed_domains = ['zhihu.com']
    #start_urls = ['https://www.zhihu.com']
    start_user = '19555033'
    followers_url = 'https://www.zhihu.com/api/v4/topics/{user}/followers?include={include}&limit={limit}&offset={offset}'
    followers_query = 'data[*].gender,answer_count,articles_count,follower_count,is_following,is_followed'
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followees_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
   # print(Request(followers_url.format(user = start_user, include = followers_query, limit = 20, offset = 0)))
    #url = 'https://www.zhihu.com/api/v4/topics/19555033/followers?include=data[*].gender,answer_count,articles_count,follower_count,is_following,is_followed&limit=20&offset=0'
    #print("=====================", Request(url))

    def start_requests(self):
        print("------------------")
        yield Request(self.followers_url.format(user = self.start_user, include = self.followers_query, limit = 20, offset = 0),callback=self.parse_followers)

    def parse_followers(self, response):
        results = json.loads(response.text)
        #print('===============', results)
        if 'data' in results.keys():
            for result in results.get('data'):   # json 解析
                item = UserItem()
                for field in item.fields:
                    if field in result.keys():
                        item[field] = result.get(field)
                yield item
                #print( "================", result.get("url_token"))
                #yield Request(self.followees_url.format(user=result.get("url_token"),include=self.followees_query,offset=0,limit=20),callback=self.parse_followee)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = urllib.parse.unquote(results.get('paging').get('next'))
            yield Request(next_page, self.parse_followers)


    def parse_followee(self, response):
        time.sleep(3)
        results = json.loads(response.text)
        if "data" in results.keys():
            for result in results.get('data'):
                item = UserItem()
                for field in item.fields:
                    if field in result.keys():
                        item[field] = result.get(field)
                yield item
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = urllib.parse.unquote(results.get('paging').get('next'))
            yield Request(next_page, self.parse_followee)






