from django.shortcuts import render

from .models import Permission

def index(request):
    # permissions = [
    #     {'type': 'manager',
    #      'action': 'reset'
    #      },
    #     {
    #         'type': 'junior',
    #         'action': 'save'
    #     },
    #     {
    #         'type': 'senior',
    #         'action': 'cancel'
    #     }
    # ]
    permissions = Permission.objects.all()
    location_files = ['page 1', 'page 2']
    return render(request, 'polls/index.html', {
        'show': True,
        'disable': False,
        'permissions': permissions,
        'location_files': location_files
    })


def action_page(request, action):
    selected_permission = Permission.objects.get(action=action)
    return render(request, 'polls/action-page.html', {'action': selected_permission.action})

