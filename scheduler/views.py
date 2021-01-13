from django.shortcuts import render

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests
import os
import platform

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def call_url(url):
    r = requests.get('{0}'.format(url))
    print('status code', r.status_code)


@api_view(['GET'])
def schedule_url(request):
    url = request.GET['url']
    stamp = request.GET['datetime']
    stamp = datetime.strptime(stamp, '%d/%m/%y %H:%M:%S')

    scheduler = BackgroundScheduler()
    scheduler.add_job(call_url, 'cron', args=[url], second = stamp.second, minute = stamp.minute, hour = stamp.hour, day = stamp.day, month = stamp.month, year = stamp.year)
    scheduler.start()

    return Response({'message': 'Task Scheduled Successfully!'}, status = status.HTTP_200_OK)


@api_view(['GET'])
def ping_status(request):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = os.system("ping " + param + " 1 " + request.GET['host'])

    if response == 0:
        pingstatus = "OK"
    else:
        pingstatus = "Network Error"

    data = {
        'status': pingstatus
    }

    return Response(data, status = status.HTTP_200_OK)
