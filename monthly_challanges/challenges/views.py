from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

months = {
    "january": "Julia",
    "february": "C#",
    "march": "Node",
    "april": "Python",
    "may": "PHP",
    "june": "Ruby",
    "july": "C++",
    "august": "Golang",
    "september": "C",
    "october": "Rust",
    "november": "Java",
    "december": None,
}

# Create your views here.


def index(request):
    month_list = list(months.keys())
    return render(request, "challenges/index.html", {
        "months": month_list
    })


def show_challenge(request, month):
    challenge = None
    try:
        challenge = months[month]
        return render(request, "challenges/challenge.html", {
            "challenge": challenge,
            "month": month
        })
    except:
        raise Http404()


def show_challenge_by_number(request, month):
    challenge = None
    list_of_keys = list(months.keys())
    if len(months) < month:
        raise Http404()
    challenge = list_of_keys[month - 1]
    redirect_path = reverse("challengeURL", args=[challenge])
    return HttpResponseRedirect(redirect_path)
