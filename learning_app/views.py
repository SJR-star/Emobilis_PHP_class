from django.shortcuts import render

# Create your views here.
def Welcome_home(request):
    """ Function to display the home/landing page"""
    context = {}
    return render(request, "index.html", context)

def about_us(request):

    context ={}
    return render(request, "about.html", context)

def Our_story(request):

    context ={}
    return render(request, "story.html", context)

def Our_team_members(request):

    context={}
    return render(request, "team.html", context)


def Contact_Us(request):
    context={}
    return render(request, "contact.html", context)