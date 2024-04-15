from django.shortcuts import render

# Create your views here.
def profile(request, username):
    context = {'username':username}
    return render(request, "profile.html", context)