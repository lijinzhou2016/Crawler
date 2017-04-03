#!/usr/bin/env python
# -*- conding: utf-8 -*-

# pip install requests

import requests

class HtmlDownloader(object):
    
    def download(self, url):
        # print "download"
        if url is None:
            return

        r=requests.get(url)
        if r.status_code != 200:
            return None

        # 设置成utf-8编码
        r.encoding = "utf-8"
        return r.text