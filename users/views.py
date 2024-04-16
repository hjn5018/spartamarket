from django.shortcuts import render

# Create your views here.
def profile(request, username):
    context = {'username':username}
    return render(request, "users/profile.html", context)