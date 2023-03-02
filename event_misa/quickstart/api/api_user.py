from quickstart.models import user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import uuid
import json
class getUserByEventID(APIView):
    def get(self, request, id, one=False):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetUser] @EventID=' + str(id))
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

class insertUser(APIView):
    def post(self, request):
        cursor = connection.cursor()
        # UserID = request.data['UserID']
        EventID = request.data['EventID']
        FullName = request.data['FullName']
        Position = request.data['Position']
        Email = request.data['Email']
        Phone = request.data['Phone']
        Organizational = request.data['Organizational']
        TaxCode = request.data['TaxCode']
        CreatedDate = request.data['CreatedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_InsertUser] @UserID=" + "'"+ str(uuid.uuid4())+"'" + ", @EventID=" + "'"+ str(EventID)+"'" + ", @FullName=" + "'"+ str(FullName)+"'" + ", @Position=" + "'"+ str(Position)+"'" + ", @Email=" + "'"+ str(Email)+"'" + ", @Phone=" + "'"+ str(Phone)+"'" + ", @Organizational=" + "'"+ str(Organizational)+"'" + ", @TaxCode=" + "'"+ str(TaxCode)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'")
            return Response({
                "message": "Thêm thành công",
                "data": request.data
                },
                status=status.HTTP_201_CREATED
            )
        except:
            return Response({
                "message": "Lỗi"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        finally:
            cursor.close()