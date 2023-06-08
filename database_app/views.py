from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

def index(request):
  if request.user.is_authenticated:
    lists = request.user.todolist.all()
    return render(request,'index.html', {"lists": lists})
  else:
    return redirect("login")
def list(request,id):
  ls = ToDoList.objects.get(id=id)
  if request.user == ls.user:
    if request.method == "POST":
      if request.POST.get("save"):
        for item in ls.item_set.all():
          if request.POST.get("c"+ str(item.id)) == "clicked":
            item.complete = True
          else:
            item.complete = False
          item.save()

      elif request.POST.get("newItem"):
        txt = request.POST.get("new")
        ls.item_set.create(text = txt, complete = False)
    return render(request,'list.html', {"list": ls})
  else:
    return redirect("/")
def create(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      form = CreateNewList(request.POST)
      if form.is_valid():
        n = form.cleaned_data["name"]
        ls = ToDoList(name = n)
        ls.save()
        request.user.todolist.add(ls)
        return HttpResponseRedirect("/%i" %ls.id)
    else:
      form = CreateNewList()
      return render(request,'create.html', {"form":form})
  else:
    return redirect("login")
