#!/usr/bin/env python
#-*-coding:utf-8-*-

# python manage.py shell
# 相当于下面两句：
# python
# from minicms.wsgi import *

from minicms.wsgi import *
from news.models import Column, Article

def main():
    columns_urls = [
        ('体育新闻','sports'),
        ('社会新闻','society'),
        ('科技新闻','tech'),
    ]

    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]

        for i in range(1,11):
            article = Article.objects.get_or_create(
                title = '{}_{}'.format(column_name,i),
                slug = 'article_{}'.format(i),
                content = '新闻详细内容： {}  {}'.format(column_name,i)
            )[0]
            article.column.add(c)  #文章和栏目是一对多的关系，一篇文章可以对应多个栏目

if __name__=='__main__':
    main()
    print 'Done!'