from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Student

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_marks(request):
    if request.method == 'POST':
        name = request.POST['name']
        class_name = request.POST['class_name']
        subject = request.POST['subject']
        marks = request.POST['marks']
        Student.objects.create(name=name, class_name=class_name, subject=subject, marks=marks)
        return redirect('view')
    return render(request, 'add_marks.html')

@login_required
def view_marks(request):
    students = Student.objects.all()
    return render(request, 'view_marks.html', {'students': students})

@login_required
def edit_marks(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.class_name = request.POST['class_name']
        student.subject = request.POST['subject']
        student.marks = request.POST['marks']
        student.save()
        return redirect('view')
    return render(request, 'edit_marks.html', {'student': student})

@login_required
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def delete_marks(request, student_id):
    Student.objects.filter(id=student_id).delete()

    # Reassign IDs
    students = Student.objects.all().order_by('id')
    for index, student in enumerate(students, start=1):
        student.id = index
        student.save()

    return redirect('view')

@login_required
def export_csv(request):
    # Set up the HTTP response for a CSV file
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Class', 'Subject', 'Marks'])  # Column headers

    # Fetch data from the database and write rows
    students = Student.objects.all()
    for student in students:
        writer.writerow([student.id, student.name, student.class_name, student.subject, student.marks])

    return response

@login_required
def update_marks(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.name = request.POST['name']
        student.class_name = request.POST['class_name']
        student.subject = request.POST['subject']
        student.marks = request.POST['marks']
        student.save()
        return redirect('view')
    
def user_logout(request):
    logout(request)
    return redirect('login')    