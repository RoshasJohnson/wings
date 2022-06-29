from django.db import models

# Create your models here.


class  Report (models.Model):
    reported_item = models.CharField(max_length=200)
    reported_item_id = models.IntegerField()
    reporter = models.CharField(max_length=200)
    report_reason = models.CharField(max_length=200)
    report_date = models.DateTimeField(auto_now_add=True)
    report_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.reported_item


   