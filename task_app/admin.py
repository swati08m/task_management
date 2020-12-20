from django.contrib import admin
from task_app.models import ProjectDetails, ProjectTasks


# Register your models here.
admin.site.register(ProjectDetails)
admin.site.register(ProjectTasks)