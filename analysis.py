#! /usr/bin/env python
# coding: utf-8
# author: ruandao(ljy080829@gmail.com)
"""
Analysis 用来从页面中提取链接，过滤结果数据
"""

from bs4 import BeautifulSoup 
from urlparse import urljoin
import urllib2


class Analysis(object):
    """
    Analysis was use to filter content in web page, and log it
    >>> a = Analysis()
    >>> a.getAllLinks("http://hao123.com", "<a href='xdkfl'>xxdf</a><a href='/dfk'></a><a href='mailto:jubao@vip.163.com'></a><a href='http://xfd.com/dfkl'></a><a href='http://www.hao123.com/lkfd/dflk'></a>")
    ['http://hao123.com/xdkfl', 'http://hao123.com/dfk', 'http://xfd.com/dfkl', 'http://www.hao123.com/lkfd/dflk']
    """
    def __init__(self,saver=None,keyword=None):
        self.keyword=keyword
        self.saver = saver

    def filterContent(self, link, content):
        if self.saver is None:
            return
        d = {
            "keyword":self.keyword, 
            "link":link, 
            "content":content}
        if self.keyword is None or self.keyword in content:
            self.saver.saveContent(d)

    def getAllLinks(self,base_url, content):
        """
        就是提取页面的所有链接,要绝对链接的
        """

        soup = BeautifulSoup(content)
        links = [ link.get('href') for link in soup.find_all('a') if type(link.get('href'))== type('string') ]
        l = []
        for link in links:
            # 万恶的空格
            link = link.strip()
            link = link.split("#")[0]
            if len(link) == 0:
                continue
            link = link if link.startswith("http://") else "http://" + link
            link = urljoin(base_url,link)
            host = urllib2.Request(link).get_host()
            if host is None:
                # 防止像 mailto:jubao@vip.163.com 这样的伪链接
                continue
            l.append(link)
        

        links = l

        return links


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

