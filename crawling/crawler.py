# coding: utf-8

import os, time, random
import sys, traceback

from model.page import Page

class Crawler:
    
    def crawl(self, crawlable_list, max_delay=None):
        product_dict = {}
        for crawlable in crawlable_list:
            product_dict[crawlable.get_crawlable_name()] = self.link_crawler(crawlable, max_delay) 
        return product_dict

    def link_crawler(self, crawlable, max_delay):
        main_url, product_url_regex = crawlable.get_home_page(), crawlable.get_product_pages()

        main_page = Page(crawlable, main_url)
        main_crawling_pages = main_page.get_main_crawling_pages()
        crawl_queue = main_crawling_pages[:]
        current_main_page = 0
        main_pages_length = len(main_crawling_pages)
        
        all_visited, product_list = [], []
        products_visited = []

        while crawl_queue:
            url = crawl_queue.pop()
            
            try:
                if url not in all_visited:
                    if url in main_crawling_pages:
                        current_main_page += 1
                        print('\n%d out of %d main pages\n' % (current_main_page, main_pages_length))
                    
                    if max_delay and max_delay > 0:
                        time.sleep(random.randint(0,max_delay)) #Making a little bit more difficult to be caught
                    
                    page = Page(crawlable, url)
                    all_visited.append(url)
                    
                    if page.is_product and page.url not in products_visited:
                        product_list.append(page.get_product())
                        products_visited.append(page.url)
                    
                    page_links = page.get_page_links()
                    for link in page_links:
                        if link not in all_visited:
                            crawl_queue.append(link)

            except Exception as e:
                traceback.print_exc(file=sys.stdout)
                if url not in all_visited:
                    all_visited.append(url)
                    
        print(str(len(product_list)) + ' products found.')            
        return product_list