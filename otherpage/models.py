from django.db import models
from django.db.models.fields import DateField, IntegerField, IntegerField


class Statistics(models.Model):
    id2 = IntegerField(primary_key=True)
    emo_date = models.DateField(null=False)
    positive = models.IntegerField(default=0, null=True)
    negative = models.IntegerField(default=0, null=True)
    neutral = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'statistics'
        managed = False
