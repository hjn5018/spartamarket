from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        'member':member
    }
    return render(request, "users/profile.html", context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if request.user != member:
            if request.user in member.follower.all():
                member.follower.remove(request.user)
            else:
                member.follower.add(request.user)
        return redirect('users:profile', member.username)
    return redirect('accounts:login')