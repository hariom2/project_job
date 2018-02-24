# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from .views import KingsListView
urlpatterns = [
    url(
        regex=r'^kings-list/$',
        view=KingsListView.as_view(),
        name='kings-list'
    ),

    # url(r'^account/password/reset/complete/$','django.contrib.auth.views.password_reset_complete'),
]
