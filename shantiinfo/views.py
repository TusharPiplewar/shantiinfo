from django.http import HttpResponse
from django.shortcuts import render
from service.models import task

# def task_list(request):
#     return HttpResponse("test")


def task_list(request):
    task_data = task.objects.all()
    if request.method == "POST":
        task_reason = request.POST.get('task_reason')
        data = task(task_reason = task_reason,task_step = "step_1")
        data.save()
        return render(request,"add_task.html")
    if request.method=="GET":
        ts = request.GET.get('serch_d')
        if ts != None:
            task_data = task.objects.filter(task_reason__icontains = ts)
    data = {
        'title':task_data
    }
    return render(request,"task.html",data)
    

def add_task(request):
    if request.method == "POST":
        task_reason = request.POST.get('task_reason')
        task_step = "Step 1"
        data = task(task_reason = task_reason,task_step = "step_1")
        data.save()
    return render(request,"add_task.html")

# def update_task(request,task_id):
#     data = task.Objects.get(tt=task_id)
#     from task(request.POST or None)