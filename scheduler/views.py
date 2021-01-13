from django.shortcuts import render

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests
import os
import platform

#imports from django_rest_frameowrk
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def call_url(url):

    ''' Function to be called on scheduled time 
        prints status code of response from the called api , in terminal '''
   
    r = requests.get('{0}'.format(url))
    print('status code', r.status_code)


@api_view(['GET'])
def ping_status(request):

    ''' Ping endpoint to check the status of server , whether it is alive or not 
    and returns {status: OK} , if server active , otehrwise Network Error ''' 

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


@api_view(['GET'])
def schedule_url(request):

    ''' Scheduling endpoint to schedule an api call 
    Needs a url and a datetime as GET parameter 
    to call a function call_url when current datetime equals passed datetime in request'''

    url = request.GET['url']
    stamp = request.GET['datetime']
    stamp = datetime.strptime(stamp, '%d/%m/%y %H:%M:%S')

    if stamp < datetime.now():

        ''' To check if datetime sent had already passes or not 
        If passes , it will return  400 Bad Request'''

        return Response({'message':'Datetime sent had already passsed!'}, status = status.HTTP_400_BAD_REQUEST)

    scheduler = BackgroundScheduler()
    scheduler.add_job(call_url, 'cron', args=[url], second = stamp.second, minute = stamp.minute, hour = stamp.hour, day = stamp.day, month = stamp.month, year = stamp.year)
    scheduler.start()

    return Response({'message': 'Task Scheduled Successfully!'}, status = status.HTTP_200_OK)