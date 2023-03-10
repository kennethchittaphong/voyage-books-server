from voyagebooksapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has associated User
    Method arguments:
      request -- The full HTTP request object
    '''

    uid = request.data['uid']

    try:
        user = User.objects.get(uid=uid)

        data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_image_url': user.profile_image_url,
            'email': user.email,
            'about': user.about
        }
        return Response(data)
    except:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        profile_image_url=request.data['profile_image_url'],
        about=request.data['about'],
        email=request.data['email'],
        uid=request.data['uid']
    )

    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'profile_image_url': user.profile_image_url,
        'email': user.email,
        'about': user.about,
        'uid': user.uid,
    }
    return Response(data)
