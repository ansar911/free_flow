from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Parent
from .forms import ParentForm


@login_required
def parent_list(request):

    search = request.GET.get("search", "")

    parents = Parent.objects.all()

    if search:
        parents = parents.filter(
            Q(name__icontains=search) |
            Q(phone__icontains=search)
        )

    parents = parents.order_by("name")

    return render(
        request,
        "parents/parent_list.html",
        {
            "parents": parents,
            "search": search,
        }
    )


@login_required
def add_parent(request):

    if request.method == "POST":

        form = ParentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("parent_list")

    else:
        form = ParentForm()

    return render(
        request,
        "parents/add_parent.html",
        {
            "form": form,
        }
    )


@login_required
def edit_parent(request, pk):

    parent = get_object_or_404(Parent, pk=pk)

    if request.method == "POST":

        form = ParentForm(request.POST, instance=parent)

        if form.is_valid():
            form.save()
            return redirect("parent_list")

    else:
        form = ParentForm(instance=parent)

    return render(
        request,
        "parents/add_parent.html",
        {
            "form": form,
        }
    )