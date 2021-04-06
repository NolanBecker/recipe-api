from django.contrib import admin
from core import models


admin.site.register(models.Tag)
admin.site.register(models.Item)
admin.site.register(models.Recipe)
admin.site.register(models.Unit)
admin.site.register(models.Quantity)
