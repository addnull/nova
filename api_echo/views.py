# -*- coding: utf-8 -*-
import os

from django.conf.urls import url
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


def add_urlpatterns(urlpatterns):
    as_view = ViewSet.as_view({
        'get': 'echo',
    })

    urlpatterns += [
        url(r'^echo/$', as_view),
    ]


class ViewSet(viewsets.ViewSet):
    serializer_class = serializers.Serializer

    @staticmethod
    def echo(request):
        """
        ELB health check
        ---
        responseMessages:
        -
            code: 200
            message:
        -
            code: 404
            message:
        """
        if os.path.exists('/etc/nova/no_echo'):
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response()
