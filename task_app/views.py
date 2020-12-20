from django.shortcuts import render
from rest_framework.decorators import api_view
from task_app.models import ProjectDetails, ProjectTasks
from utility.common_keys import *
from utility.response_utils import ok_response, error_response, headers_mapping
from utility.common_msgs import *
from requests import get as get_requests, post as post_requests
from os import path as ospath

# Create your views here.
"""
Purpose : Goto Index Page
"""
def indexpage(request):
    endpoint = "http://"+request.META.get("REMOTE_ADDR") +":"+port
    whole_endpoint = ospath.join(endpoint, "api", "projects")
    headers = headers_mapping["json"]
    response = get_requests(whole_endpoint, headers=headers)
    try:
        data = response.json()["data"]["projects_list"]
    except:
        data=[]
    return render(request, "index.html", {'records':data})


"""
Purpose : Get Projects data
"""
@api_view(['GET'])
def projectdetails(request):
    projectobj = ProjectDetails.objects.filter(is_active=True)
    projects_list = []
    for item in projectobj:
        project_dict = {}
        project_dict[projectid] = item.project
        project_dict[project_name] = item.project_name
        project_dict[description] = item.description
        project_dict[start_date] = item.start_date
        project_dict[end_date] = item.end_date
        projects_list.append(project_dict)
    data = {"projects_list":projects_list}
    return ok_response(data=data)



"""
Purpose : Get Tasks data as per Project
"""
@api_view(['POST'])
def tasks_deatils(request):
    project_id=request.data.get("project_id")
    print("project_id", project_id)
    try:
        projectobj = ProjectDetails.objects.get(project=project_id, is_active=True)
    except:
        return error_response(message=projectNotFound)
    tasksobjs = ProjectTasks.objects.filter(project=project_id, is_active=True)
    tasks_list = []
    for item in tasksobjs:
        task_dict = {}
        task_dict[task] = item.task
        task_dict[task_name] = item.task_name
        task_dict[description] = item.description
        task_dict[start_date] = item.start_date
        task_dict[end_date] = item.end_date
        tasks_list.append(task_dict)
    data = {"tasks_list": tasks_list}
    return ok_response(data=data)
