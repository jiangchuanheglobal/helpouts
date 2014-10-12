from django.contrib import admin

# Register your models here.
from helps.models import User,Honor,Task

admin.site.register(User)
admin.site.register(Honor)
admin.site.register(Task)