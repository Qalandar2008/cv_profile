from django.shortcuts import render

from .models import Certificate, Interest, ResumeProfile


def cv_home(request):
    profile = ResumeProfile.load()
    certificates = Certificate.objects.all()
    interests = Interest.objects.all()
    return render(
        request,
        "resume/home.html",
        {
            "profile": profile,
            "certificates": certificates,
            "interests": interests,
        },
    )
