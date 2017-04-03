#!/usr/bin/env python
# -*- conding: utf-8 -*-


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w")

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1px'>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td border='1px' style='padding:10px;width: 18%'><a href='{0}'>{1}</a></td>".format(
                data["url"].encode("utf-8"), data["title"].encode("utf-8")))
            fout.write("<td border='1px' style='padding:10px;width: 82%'>{0}</td>".format(
                data["summary"].encode("utf-8")))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
