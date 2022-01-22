import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('tasks', backend='redis://localhost:6379/')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, add.s(16,32), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, add.s(16,16), expires=10)

@app.task
def test(arg):
    print(arg)
    #test2()
    #print(Url.objects.get(pk=1))

@app.task
def add(x, y):
    z = x + y
    print(z)

