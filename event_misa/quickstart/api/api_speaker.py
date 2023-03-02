from quickstart.models import speaker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import uuid
import json
class getSpeakerList(APIView):
    def get(self, request, one=False):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetSpeaker]')
            r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
            return Response({
                "data": json.dumps(r[0] if r else None) if one else r
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response({
                "message": "Lỗi"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            cursor.close()

class getSpeakerByID(APIView):
    def get(self, request, id, one=False):
        cursor = connection.cursor()
        try:
            cursor.execute("EXEC [dbo].[Proc_GetSpeakerByID] @SpeakerID=" + "'"+ str(id)+"'")
            r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
            return Response({
                "data": json.dumps(r[0] if r else None) if one else r
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response({
                "message": "Lỗi"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            cursor.close()

class deleteSpeakerByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute("EXEC [dbo].[Proc_DeleteSpeakerByID] @SpeakerID=" + "'"+ str(id)+"'")
            return Response({
                "message": "Xóa thành công",
                "id":id
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response({
                "message": "Lỗi"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            cursor.close()

class InsertSpeaker(APIView):
    def post(self, request):
        cursor = connection.cursor()
        SpeakerName = request.data['SpeakerName']
        Avatar = request.data['Avatar']
        Position = request.data['Position']
        Description = request.data['Description']
        Inactive = request.data['Inactive']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_InsertSpeaker] @SpeakerID=" + "'"+ str(uuid.uuid4())+"'" + ", @SpeakerName=" + "'"+ str(SpeakerName)+"'" + ", @Avatar=" + "'"+ str(Avatar)+"'" + ", @Position=" + "'"+ str(Position)+"'" + ", @Description=" + "'"+ str(Description)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
            return Response({
                "message": "Thêm thành công",
                "data": request.data
                },
                status=status.HTTP_201_CREATED
            )
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)

class UpdateSpeaker(APIView):
    def put(self, request, id):
        cursor = connection.cursor()
        SpeakerName = request.data['SpeakerName']
        Avatar = request.data['Avatar']
        Position = request.data['Position']
        Description = request.data['Description']
        Inactive = request.data['Inactive']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_UpdateSpeaker] @SpeakerID=" + "'"+ str(id)+"'" + ", @SpeakerName=" + "'"+ str(SpeakerName)+"'" + ", @Avatar=" + "'"+ str(Avatar)+"'" + ", @Position=" + "'"+ str(Position)+"'" + ", @Description=" + "'"+ str(Description)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
            return Response({
                "message": "Cập nhật thành công",
                "data": request.data
                },
                status=status.HTTP_200_OK
            )
        finally:
            cursor.close()
