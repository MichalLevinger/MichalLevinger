from django.shortcuts import render, redirect

from .models import Permission, Person

from .forms import RegisterPersonForm

def index(request):
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
    if request.method == 'GET':
        register_person_form = RegisterPersonForm()
    else:
        register_person_form = RegisterPersonForm(request.POST)
        if register_person_form.is_valid():
            person_name = register_person_form.cleaned_data['name']
            address_name = register_person_form.cleaned_data['address']
            person, _ = Person.objects.get_or_create(name=person_name, address=address_name)
            selected_permission.persons.add(person)
            return redirect('success-page')
        else:
            print('not valid')

    return render(request, 'polls/action-page.html', {
        'permission': selected_permission,
        'register_person_form': register_person_form
    })


def success_page(request):
    return render(request, 'polls/success.html')


