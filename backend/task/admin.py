from django.contrib import admin
from .models import Message, Task, Rating, TaskTransaction

admin.site.register(Message)
admin.site.register(Task)
admin.site.register(TaskTransaction)
admin.site.register(Rating)

# Register your models here.
