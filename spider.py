#!/usr/bin/python
#encoding:utf-8
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u",  dest="url",
                  help=u"指定爬虫开始地址", metavar="http://xxx")
parser.add_option("-d",  dest="deep", type="int",
                  help=u"指定爬虫深度", metavar="n")
parser.add_option("--dbfile",dest="dbfile",
      help=u"存放结果数据到指定的数据库（sqlite）文件中", metavar="FILE")

parser.add_option("--thread", dest="threadNumber",type="int",default=10,
      help=u"指定线程池大小，多线程爬取页面，可选参数，默认10", metavar="n")
parser.add_option("--key", dest="key",metavar="KEY",
      help=u"页面内的关键词，获取满足该关键词的页面，可选参数，默认为所有页面")
parser.add_option("-f",dest="logfile",default="spider.log",metavar="FILE",
      help=u"指定日志文件，可选参数，默认spider.log")
parser.add_option("-l",dest="loglevel",type="int",default=1,metavar="n",
      help=u"日志记录文件记录详细程度，数字越大记录越详细，可选参数，默认1")
parser.add_option("--testself",dest="testself",
      help=u"程序自测，可选参数",action="store_true",default=False)

(options,args) = parser.parse_args()
if options.url == None or options.deep == None or options.dbfile == None:
    print("-u,-d,--dbfile 不是可选参数")
    sys.exit(0)


