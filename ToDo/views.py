from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from ToDo.models import ToDo
from django.http import HttpResponseRedirect


def tasks(request):
    todo_items = ToDo.objects.all().order_by("-added_time")
    return render(request, 'index.html', {"todo_items":todo_items})

@csrf_exempt
def todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    ToDo.objects.create(added_time=current_date, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
