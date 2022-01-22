import os
from config.celery import app
from config.settings import REDIS_URL
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
    CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

import json
from celery import shared_task
import httpx
import re
from datetime import datetime

from core.models import Report, Url

SIGNATURE = "9j/4AAQSkZJRgABAQAAAQABAAD/4QCgRXhpZgAATU0AKgAAAAgAAwEoAAMAAAABAAEAAAITAAMAAAABAAEAAIglAAQAAAABAAAAMgAAAAAABAABAAIAAAACTgAAAAACAAUAAAADAAAAaAADAAIAAAACRQAAAAAEAAUAAAADAAAAgAAAAAAAAAA0AAAAAQAAAAwAAAABAAEE0QAACGUAAAAVAAAAAQAAAAAAAAABAACKAQAABBH/"
    
def task1():
    print("GO task")
    #print(Report.object.get(pk=1))

    #Report.object.create(
    #    url=Url.objects.get(pk=1),
    #    status="LIVE")

@shared_task(name="check_url")
def check_url():
    urls = Url.objects.all()
    for url in urls:
        requst_text = ""
        try:
            result = httpx.get(url.path, follow_redirects=True)
            status_code = result.status_code
            requst_text = result.text
        except Exception:
            status_code = 600

        if len(re.findall(SIGNATURE, requst_text)) > 0:
            status = "HACKED"
        elif status_code < 300:
            status = "LIVE"
        elif status_code == 403:
            status = "BLOCKED"
        else:
            status = "RESTRICTED"

        Report.objects.create(
            url=url,
            date=datetime.now().date(),
            time=datetime.now().time(),
            status=status,
        )