from django.shortcuts import render,redirect
from .models import Login
from django.contrib import messages # new

# Create your views here.
# 
def index(request):
    if request.method == 'POST': # new
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        if username and mail: # new
            try: # new
                data = Login(username=username, mail=mail)
                data.save()
                messages.success(request, f'Your data has been saved!') # new
                return redirect('some_other_page') # new
            except Exception as e: # new
                messages.error(request, f'Something went wrong: {e}') # new
        else: # new
            messages.error(request, f'Please enter a valid username and mail.') # new
    return render(request, 'pages/index.html')