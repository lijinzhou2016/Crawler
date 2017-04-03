#!/usr/bin/env python
# -*- conding: utf-8 -*-


"""爬虫总调度模块

爬取百度百科词条及链接和概要
"""

import html_downloader
import html_parser
import html_outputer
import url_manager

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print u"craw %d : %s"%(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # 爬取词条的个数
                if count == 50:
                    break
                count += 1
            except basestring as e:
                print e
                print "craw faild"

        self.outputer.output_html()


if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
