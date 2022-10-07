from django.shortcuts import render

# Create your views here.
def home_view(req, *args, **kwargs):
    data = {
        'name': 'Rafael',
        'age' : 24,
        'list' : []
    }
    
    return render(req, 'home.html', data)
