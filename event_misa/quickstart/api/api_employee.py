from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
import uuid
class getPagingEmployee(APIView):
    def get(self, request, one=False):
        cursor = connection.cursor()
        pageIndex = request.data['PageIndex']
        pageSize = request.data['PageSize']
        where = request.data['Where']
        sort = request.data['Sort']
        print('EXEC [dbo].[Proc_GetPagingEmployee] @PageIndex=' + str(pageIndex) + ', @PageSize=' + str(pageSize) + ', @Where=' + str(where) + ', @Sort=' + str(sort))
        cursor.execute('EXEC [dbo].[Proc_GetPagingEmployee] @PageIndex=' + str(pageIndex) + ', @PageSize=' + str(pageSize) + ', @Where=' + str(where) + ', @Sort=' + str(sort))
        r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        return Response({
            "data": json.dumps(r[0] if r else None) if one else r
            },
            status=status.HTTP_200_OK
        )