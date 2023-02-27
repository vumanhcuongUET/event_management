from quickstart.models import bannerSlide
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import datetime
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
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)

class InsertBannerSlide(APIView):
    def post(self, request, format=None):
        cursor = connection.cursor()
        bannerTitle = request.data['BannerTitle']
        bannerUrl = request.data['BannerUrl']
        linkTo = request.data['LinkTo']
        sortOrder = request.data['SortOrder']
        Inactive = request.data['Inactive']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_InsertBannerSlide] @BannerTitle=" + "'"+ str(bannerTitle)+"'" + ", @BannerUrl=" + "'"+ str(bannerUrl)+"'" + ", @LinkTo=" + "'"+ str(linkTo)+"'" + ", @SortOrder=" + "'"+ str(sortOrder)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)