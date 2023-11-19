from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        # this is to change the display name from item(1), item(2) to the actual
        # name that we want to give to the item
        return self.name
