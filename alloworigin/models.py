from django.db import models


class Request(models.Model):
    ip = models.GenericIPAddressField()
    dest = models.URLField()
    date =  models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.dest
