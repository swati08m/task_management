from django.db import models

# Create your models here.
class ProjectDetails(models.Model):
    project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.project


class ProjectTasks(models.Model):
    task = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    project = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.task