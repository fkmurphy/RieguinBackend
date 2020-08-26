from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Profile
from users.serializers import ProfileSerializer
# Create your views here.
@api_view(['GET'])
def ver(requests):
    profiles = Profile.objects.all()
    data = []
    """
    for profile in profiles:
        serializer = ProfileSerializer(profile).data
        data.append(serializer)
    """
    serializer = ProfileSerializer(profiles,many=True)
    data = serializer.data
    return Response(data)

""" para validar
    serializer.is_valid(raise_exception=True)
"""
""""para un create masivo desde un json
    create = Profile.objects.create(**data)

"""
