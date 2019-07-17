from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.family_datastructure import Family
import json

# initialize a 'Doe' family
family = Family(last_name='Rojas')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""


class MembersView(APIView):
    def get(self, request, member_id=None):
        # fill this method and update the return
        if member_id is not None:
            result = family.get_member(member_id)
            if result is None:
                return Response("No existe este integrante", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(result, status=status.HTTP_200_OK)
        else:
            result = family.get_all_members()
            return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        # fill this method and update the return
        member = request.data
        if "first_name" in member and member["first_name"] != "":
            result = family.add_member(member)
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, member_id=None):
        # fill this method and update the return
        result = None
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, member_id=None):
        if member_id is not None:
            result = family.delete_member(member_id)
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response("No enviaste el id a eliminar", status=status.HTTP_400_BAD_REQUEST)
