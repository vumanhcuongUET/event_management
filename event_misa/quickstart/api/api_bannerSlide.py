from quickstart.models import bannerSlide
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import datetime
import json
class bannerSlideList(APIView):
    """
    List all bannerSlides, or create a new bannerSlide.
    """

    def get(self, request, format=None, one=False):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetListBannerSLide]')
            r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
            return Response({
                "data": json.dumps(r[0] if r else None) if one else r
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()
class deleteBannerSlideByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_DeleteBannerSlideByID] @BannerID=' + str(id))
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
class updateBannerSlide(APIView):
    def put(self,request, id):
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
            cursor.execute("EXEC [dbo].[Proc_UpdateBannerSlide] @BannerID=" + "'"+ str(id)+"'" + ", @BannerTitle=" + "'"+ str(bannerTitle)+"'" + ", @BannerUrl=" + "'"+ str(bannerUrl)+"'" + ", @LinkTo=" + "'"+ str(linkTo)+"'" + ", @SortOrder=" + "'"+ str(sortOrder)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
            return Response({
                "message": "Cập nhật thành công",
                "data": request.data
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