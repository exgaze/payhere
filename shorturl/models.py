from django.db import models

class ShortURL(models.Model):
    urlorigin  = models.URLField(max_length = 200)
    urlshorten = models.URLField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    valid      = models.BooleanField(default = True)

    class Meta:
        db_table = 'shorturl'
