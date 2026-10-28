from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Student

from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from logs.services.logger import Logger
from django.contrib import messages

@login_required
def student_list(request):

    search = request.GET.get("search", "")

    students = Student.objects.select_related("parent")

    if search:

        students = students.filter(

            Q(student_id__icontains=search) |
            Q(name__icontains=search) |
            Q(parent__name__icontains=search) |
            Q(parent__phone__icontains=search)

        )

    students = students.order_by("student_id")

    paginator = Paginator(students, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(

        request,

        "students/student_list.html",

        {

            "page_obj": page_obj,

            "search": search,

        }

    )

    students = students.order_by("student_id")

    return render(

        request,

        "students/student_list.html",

        {

            "students": students,

            "search": search,

        },

    )


@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save()

            Logger.log(
                    request.user,
                    "ADD_STUDENT",
                    f"Added student {student.student_id} - {student.name}",
                )

            messages.success(
                    request,
                    "Student added successfully."
                )

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
        },
    )
@login_required
def edit_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()

            Logger.log(
                request.user,
                "EDIT_STUDENT",
                f"Edited student {student.student_id} - {student.name}",
            )

            messages.success(
                request,
                "Student updated successfully."
            )
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
        },
    )