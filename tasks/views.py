
from django.shortcuts import render
from django.utils import timezone  # Import the timezone module
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    current_datetime = timezone.now()
    tasks = Task.objects.filter(completed=False, user=request.user, due_date__gt=current_datetime)

    return render(request, 'tasks/home.html', {'tasks': tasks})

def upcoming(request):
    current_datetime = timezone.now()
    upcoming_tasks = Task.objects.filter(completed=False,  user=request.user, due_date__gt=current_datetime)
    return render(request, 'tasks/upcoming.html', {'upcoming_tasks': upcoming_tasks})

def past_due(request):
    current_datetime = timezone.now()
    past_due_tasks = Task.objects.filter(completed=False, user=request.user, due_date__lte=current_datetime)
    return render(request, 'tasks/past_due.html', {'past_due_tasks': past_due_tasks})

def completed(request):
    completed = Task.objects.filter(completed=True, user=request.user)
    return render(request, 'tasks/completed.html', {'completed' : completed})

def logout(request):
    logout = Task.objects.filter(completed=True)
    return render(request, 'tasks/logout.html', {'logout': logout})



# user log in
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})

# user log in
# Sa iyong views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')
        # Authenticate the user
        user = authenticate(request, username=username_email, password=password)

        if user is not None:
            # Login the user
            auth_login(request, user)
            return redirect('home')  # I-redirect ang user sa home page o sa kahit saan mo gusto
        else:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'tasks/login.html')

# add tasks
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages module

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('dueDate')

        due_date = timezone.datetime.strptime(due_date, '%Y-%m-%dT%H:%M')

        new_task = Task(title=title, description=description, due_date=due_date, user=request.user)
        new_task.save()

        return redirect('home')

    return render(request, 'tasks/add_task.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Import ang TaskForm kung meron ka nang ito

def edit_task(request, task_id):
    # Kunin ang task mula sa database
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        # Kunin ang data mula sa form
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            # Save ang updates sa task
            form.save()
            return redirect('home')  # Redirect pagkatapos ng pag-edit
    else:
        # I-create ang form na may data ng existing task
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'tasks/delete_task.html', {'task': task})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.utils import timezone
from .forms import TaskStatusForm  # Gumawa ka ng bagong form kung kinakailangan

def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            task.completed_date = timezone.now()
            task.save()
            return redirect('home')  # Palitan ito ng tamang pangalan ng iyong redirect view
    else:
        form = TaskStatusForm(instance=task)
    return render(request, 'home.html', {'form': form})
