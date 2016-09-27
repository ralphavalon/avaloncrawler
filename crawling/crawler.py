# coding: utf-8

import re, urllib2, urlparse, os, time, random
import sys, traceback

from lxml import html

from model.product import Product

class Crawler:
    
    def get_product(self, crawlable, html_response, link):
        parsed_html = html.fromstring(html_response)
        return Product(
                    name = parsed_html.xpath(crawlable.get_product_name())[0],
                    title= parsed_html.xpath(crawlable.get_product_title())[0],
                    url  = link,
                )

    def crawl(self, crawlable_list):
        product_dict = {}
        for crawlable in crawlable_list:
            product_dict[crawlable.get_crawlable_name()] = self.link_crawler(crawlable) 
        return product_dict

    def download(self, url, num_retries=2):
        print 'Downloading:', url
        try:
            html_response = urllib2.urlopen(url).read()
        except urllib2.URLError as e:
            print 'Download error:', e.reason
            html_response = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # retry 5XX HTTP errors
                    html_response = self.download(url, num_retries-1)
        return html_response

    def link_crawler(self, crawlable):
        main_url, link_regex = crawlable.get_home_page(), crawlable.get_product_pages()
        
        parsed_html = html.fromstring(self.download(main_url))
        category_page_list = parsed_html.xpath(crawlable.get_category_pages())
        seed_url = [main_url]
        for category_page in category_page_list:
            seed_url.append(urlparse.urljoin(main_url, category_page))

        crawl_queue = seed_url
        seen = set(crawl_queue)
        is_product = False
        product_list = []

        while crawl_queue:
            url = crawl_queue.pop()
            try:
                time.sleep(random.randint(1,5)) #Making a little bit more difficult to be caught
                html_response = self.download(url)
                if is_product:
                    if link not in seed_url:
                        product_list.append(self.get_product(crawlable,html_response, link))
                    is_product = False
                
                for link in self.get_links(html_response):
                    if re.match(link_regex, link):
                        link = urlparse.urljoin(seed_url[0], link)
                        is_product = True
                        
                        if link not in seen:
                            seen.add(link)
                            crawl_queue.append(link)
            except Exception as e:
                traceback.print_exc(file=sys.stdout)
                is_product = False
                if url not in seen:
                    seen.add(link)
                    
        return product_list

    def get_links(self, html):
        webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
        return webpage_regex.findall(html)