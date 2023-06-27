from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignUpForm

@api_view(['GET'])
def me(request):
    user = request.user
    email = user.email
    return JsonResponse({
            'email': email
        })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([]) 
def signup(request):
    data = request.data
    message = 'success'

    form = SignUpForm({
        'profile': data.get('profile'),
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()

        #send verification email later
    else:
        print(form.errors)
        message = 'error'

    return JsonResponse({'message':message})