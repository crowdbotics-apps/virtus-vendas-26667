from django.contrib import admin
from .models import TaskerSkill, BusinessPhoto, Timeslot, TaskerAvailability

admin.site.register(TaskerAvailability)
admin.site.register(TaskerSkill)
admin.site.register(BusinessPhoto)
admin.site.register(Timeslot)

# Register your models here.
