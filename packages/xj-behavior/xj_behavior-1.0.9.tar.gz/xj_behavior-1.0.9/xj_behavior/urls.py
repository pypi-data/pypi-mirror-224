# _*_coding:utf-8_*_
from django.urls import re_path

from .apis.homepage_statistics_apis import HomepageStatisticsApis
from .apis.standing_book_apis import StandingBookApis

app_name = 'xj_behavior'

# 应用路由
urlpatterns = [
    re_path(r'data?$', StandingBookApis.as_view(), ),
    re_path(r'standing_book_v2?$', StandingBookApis.standing_book_v2, ),
    re_path(r'statistics?$', HomepageStatisticsApis.statistics, ),
]
