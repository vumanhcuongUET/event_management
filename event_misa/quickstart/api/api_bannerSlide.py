from quickstart.models import bannerSlide
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
class bannerSlideList(APIView):
    """
    List all bannerSlides, or create a new bannerSlide.
    """

    def get(self, request, format=None):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetListBannerSLide]')
            result_set = cursor.fetchall()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)
class deleteBannerSlideByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_DeleteBannerSlideByID] @BannerID=' + str(id))
            result_set = cursor.fetchone()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)