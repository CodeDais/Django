from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.
def date_time_view(request):
    dt=datetime.datetime.now()
    data=f"""
    <html>
        <head>
            <title>
                Datetime Application
            </title>
        </head>
        <body>
            <h1>Current Date and Time Information</h1>
            <p>Date and Time : {dt}</p>
            <p>Month : {dt.month}</p>
            <p>Day : {dt.day}</p>
            <p>Hour : {dt.hour}</p>
            <p>Minute: {dt.minute}</p>
            <p>Second: {dt.second}</p>
            <p>Microsecond: {dt.microsecond}</p>
            <p>---------------</p>
            <p>Short Day Name : {dt.strftime('%a')}</p>
            <p>Full Day Name : {dt.strftime('%A')}</p>
            <p>Week Number : {dt.strftime('%W')}</p>
            <p>Day Number : {dt.strftime('%w')}</p>
            <p>Month Number : {dt.strftime('%m')}</p>
        </body>
    </html>
    """

    return HttpResponse(data)