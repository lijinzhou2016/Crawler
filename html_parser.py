#!/usr/bin/env python
# -*- conding: utf-8 -*-

import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    

    def _get_new_urls(self, page_url, soup):
        # print "_get_new_urls"
        new_urls = set()
        try:
            links  = soup.find_all("a", href=re.compile(r"/item"))
            for link in links:
                new_url = link["href"]
                new_full_url = urlparse.urljoin(page_url, new_url)
                # print new_full_url
                new_urls.add(new_full_url)
        except BaseException as e:
            print e
            return None
        return new_urls


    def _get_new_data(self, page_url, soup):
        # print "_get_new_data"
        res_data = {}

        res_data['url'] = page_url
        try:
            title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
            res_data["title"] = title_node.get_text()

            summary_node = soup.find("div", class_="para")
            res_data["summary"] = summary_node.get_text()
        except BaseException as e:
            print e
            return None

        return res_data

    def parse(self, page_url, html_cont):
        # print "parse"
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
