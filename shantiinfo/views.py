from django.http import HttpResponse
from django.shortcuts import render
from service.models import task
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# def task_list(request):
#     return HttpResponse("test")


def task_list(request):
    if request.method=="GET":
        ts = request.GET.get('serch_d')
        task_data = task.objects.all()
        if ts :
            task_data = task_data.objects.filter(task_reason__icontains = ts)
    data = {
        'title':task_data
    }
    return render(request,"task.html",data)
    

def add_task(request):
    if request.method == "GET":
        # breakpoint()
        task_reason = request.GET.get('task_reason')
        task_step = "Step 1"
        data = task(task_reason = task_reason,task_step = "step_1")
        data.save()
    return JsonResponse({"message":"Success"})
    # return render(request,"add_task.html")



def delete_record(request, pk):
    record = get_object_or_404(task, pk=pk)    
    record.delete()
    return redirect('/')  # Redirect to a success page
    
    # return render(request, 'task.html', {'record': record})


# def update_task(request,task_id):
#     data = task.Objects.get(tt=task_id)
#     from task(request.POST or None)