# coding: utf-8

import re, urllib2, urlparse, os, time, random
import sys, traceback

from lxml import html

from model.product import Product

class Page:

    def __init__(self, crawlable, url):
        self.crawlable = crawlable
        self.main_url = crawlable.get_home_page()
        self.url = url
        self.html_source_code = self.download(url)
        self.product_url_regex = crawlable.get_product_pages()
        self.is_product = bool(re.match(self.product_url_regex, url))
        
    def download(self, url, num_retries=2):
        print('Downloading: ' + url)
        try:
            html_response = urllib2.urlopen(url).read()
        except urllib2.URLError as e:
            print('Download error:',e.reason)
            html_response = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    html_response = self.download(url, num_retries-1)
        return html_response
    
    def get_page_links(self):
        page_links_list = []
        for link in self.get_links():
            if re.match(self.product_url_regex, link):
                link = urlparse.urljoin(self.main_url, link)
                page_links_list.append(link)
        return page_links_list
        
    def get_product(self):
        parsed_html = html.fromstring(self.html_source_code)
        return Product(
                    name = parsed_html.xpath(self.crawlable.get_product_name())[0],
                    title= parsed_html.xpath(self.crawlable.get_product_title())[0],
                    url  = self.url,
                )
    
    def get_links(self):
        webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
        return webpage_regex.findall(self.html_source_code)
        
    def get_main_crawling_pages(self):
        parsed_html = html.fromstring(self.html_source_code)
        category_page_list = parsed_html.xpath(self.crawlable.get_category_pages())
        seed_url = [self.main_url]
        for category_page in category_page_list:
            seed_url.append(urlparse.urljoin(self.main_url, category_page))

        return list(set(seed_url))
