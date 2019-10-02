from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required

@login_required
@permission_required('akaun.level1', raise_exception=True)
def index(request):

    context = {
        'messages': ""
    }
    return render(request, 'akaun/index.html', context)
