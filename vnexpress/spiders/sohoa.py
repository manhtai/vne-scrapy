# -*- coding: utf-8 -*-
import scrapy
from vnexpress.items import VnexpressItem
import httplib2
import json


class SohoaSpider(scrapy.Spider):
    name = "sohoa"
    allowed_domains = ["sohoa.vnexpress.net"]
    start_urls = (
        'http://sohoa.vnexpress.net/',
    )

    def parse(self, response):
        # Parse articles
        for article_url in response.xpath(
            '//a[contains(@href, "sohoa.vnexpress.net")]/@href'
        ).re(r'.*-\d{7,}\.html$'):
            yield scrapy.Request(article_url,
                                 callback=self.parse_article_contents)

        # Parse pages
        for page in response.xpath('//a[contains(@href, "page")]/@href'
                                   ).extract():
            yield scrapy.Request(page, self.parse)

    def parse_article_contents(self, response):
        item = VnexpressItem()
        post_date = response.css('div.block_timer::text'
                                 ).extract()
        item['post_date'] = [p.strip() for p in post_date]
        item['title'] = response.xpath('//div[@class="title_news"]/h1/text()'
                                       ).extract_first().strip()
        item['short_intro'] = response.css('div.short_intro::text'
                                           ).extract_first().strip()
        item['long_content'] = response.xpath(
            '//div[contains(@class, "fck_detail")]//p//text()'
        ).extract()

        site_id = response.xpath('//meta[@name="tt_site_id"]/@content'
                                 ).extract_first()
        article_id = response.xpath('//meta[@name="tt_article_id"]/@content'
                                    ).extract_first()

        item['comments'] = self.parse_comment(site_id=site_id,
                                              article_id=article_id)

        item['tags'] = response.xpath('//a[@class="tag_item"]//text()'
                                      ).extract()
        yield item

    def parse_comment(self, article_id, site_id, limit=24):
        # Send GET request to get comments
        URL = ('http://usi.saas.vnexpress.net/index/get?offset=0&limit={limit}'
               '&sort=like&objectid={article_id}&objecttype=1&siteid={site_id}'
               ).format(limit=limit, article_id=article_id, site_id=site_id)
        h = httplib2.Http()
        __, cont = h.request(URL)
        return self.extract_comment(cont)

    @staticmethod
    def extract_comment(cont):
        cont = json.loads(cont)
        # If error, return nothing
        if cont.get('error') != 0:
            return ''
        # Else processing comments
        lis = []
        items = cont['data']['items']
        for i in items:
            lis.append(i['content'])
            if i.get('replys'):
                lis = lis + [r['content'] for r in i['replys']['items']]
        return lis
