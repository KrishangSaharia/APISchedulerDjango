# SchedulingAPIDjango

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
This project includes scheduling Django Rest APIs, it uses AdvancedPythonScheduler module for scheduling tasks in which a cron job is set.
This contains 2 endpoints - 
one for scheduling and other one is ping endpoint to check whether the server is alive or not .  
All api endpoints had been created in scheduler app under the root directory.  

### 1. Scheduling Endpoint :
This requires two arguements - first arguement will be datetime string in the format '%d/%m/%y %H:%M:%S (IST)' . For eg. 09/01/21 13:39:30 .  
and second arguement will be the url which is to be called through GET request at scheduled time (first arguement) . For eg. https://google.com .  
For eg . [ http://127.0.0.1:8000?url=https://google.com/?&datetime=09/02/21 13:39:30](http://127.0.0.1:8000?url=https://google.com/?&datetime=09/02/21%2013:39:30)

Response will JSON data with a message "Task Scheduled Successfully!" , if scheduling is successfull.
For eg. - 
```
{
    "message": "Task Scheduled Successfully!"
}
```
For eg-
[ http://127.0.0.1:8000?url=https://google.com/?&datetime=09/01/20 13:39:30](http://127.0.0.1:8000?url=https://google.com/?&datetime=09/01/20%2013:39:30).  
If datetime value sent is already past , then it throw an 400 Bad Request error, with a message in response.   
For eg-   
```
{
    "message": "Date sent had already passsed!"
}
```


### 2. Ping Endpoint -
This endpoint checks whether server is alive or not , and returns JSON message 'OK' is server is alive , otherwise returns 'Network Error'.
It takes a arguement named host ,to check whether the server is alive or not. For eg. host=google.com.  
[ http://127.0.0.1:8000/ping?host=localhost](http://127.0.0.1:8000/ping?host=localhost)
For eg. - 
```
{
    "status": "OK"
}
```

## Setup
To install all the dependencies run: 

```
$ pip install -r requirements.txt
```

## Run :
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## To start the server:
```
$ python manage.py runserver
```
### Now , you can start deploying at your local host.
At http://127.0.0.1:8000/



