from quickstart.models import speaker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
class getSpeakerList(APIView):
    def get(self, request):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetSpeaker]')
            result_set = cursor.fetchall()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)

class getSpeakerByID(APIView):
    def get(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute("EXEC [dbo].[Proc_GetSpeakerByID] @SpeakerID=" + "'"+ str(id)+"'")
            result_set = cursor.fetchall()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)

class deleteSpeakerByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute("EXEC [dbo].[Proc_DeleteSpeakerByID] @SpeakerID=" + "'"+ str(id)+"'")
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)