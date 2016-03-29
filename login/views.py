from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    hello = "hello"
    goodbye = "goodbye"
    context = {
        "donuts" : hello,
        "brownies" : goodbye,
        # "key" : "value"
    }

    return render(request, 'login/login.html', context)

    # return HttpResponse("we made it home_page")


# def login(request):
#     print request.POST["username"]
#     return render(request, '')

