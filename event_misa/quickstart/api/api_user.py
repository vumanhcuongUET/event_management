from quickstart.models import user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
class getUserByEventID(APIView):
    def get(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetUser] @EventID=' + str(id))
            print(id)
            result_set = cursor.fetchall()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)