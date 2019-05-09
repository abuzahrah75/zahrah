from django.shortcuts import render


def index(request):

    context = {
        'messages': ""
    }
    return render(request, 'akaun/index.html', context)
