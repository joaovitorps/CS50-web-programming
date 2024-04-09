from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Piority", min_value=1, max_value=1)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    context = {"tasks": request.session["tasks"]}
    return render(request, "tasks/index.html", context)


def create(request):
    # body_unicode = request.body.decode("utf-8")
    # print(body_unicode)
    # # body = json.loads(body_unicode)
    # tasks.append(body_unicode["task"])
    # url = reverse("index")
    # return redirect(url)

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # request.session["tasks"].append(task)
            request.session["tasks"] += [task]
            url = reverse("tasks:index")

            return HttpResponseRedirect(url)
        else:
            return render(request, "tasks/create.html", {"form": form})

    return render(request, "tasks/create.html", {"form": NewTaskForm()})
