from django.db import models


class Url(models.Model):
    path = models.CharField(max_length=255)

    def __str__(self):
        return str(self.path)


class Report(models.Model):

    URL_STATUSES = (
        ("LIVE", "Live"),
        ("BLOCKED", "Blocked"),
        ("RESTRICTED", "Restricted"),
    )

    date = models.DateField()
    time = models.TimeField()

    url = models.ForeignKey(
        "Url", on_delete=models.DO_NOTHING, related_name="reports"
    )  # noqa
    status = models.CharField(max_length=255, choices=URL_STATUSES)

    def __str__(self):
        return " ".join((str(self.date), " ", str(self.time)))
