from quickstart.models import event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
from enum import Enum
def listToString(s):
     
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += json.dumps(ele)
 
    # return string
    return str1
# class filter(Enum):
#     Like:1
#     EqualString:2
#     EqualNumber:3
#     Less:4
#     LessEqual:5
#     Greater:6
#     GreaterEqual:7
#     StartWith:8
#     EndWith:9
#     NotLike:10
class getAllEvent(APIView):
    def get(self, request, one=False):
        try:
            cursor = connection.cursor()
            cursor.execute('EXEC [dbo].[Proc_GetAllEvent]')
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
class getEventByID(APIView):
    def get(self, request, eventID, one=False):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetEventByID] @EventID=' + str(eventID))
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

class deleteEventByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_DeleteEventByID] @EventID=' + str(id))
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

class InsertEvent(APIView):
    def post(self, request, format=None):
        cursor = connection.cursor()
        EventName = request.data['EventName']
        Banner = request.data['Banner']
        BannerMobile = request.data['BannerMobile']
        Avatar = request.data['Avatar']
        Topic = request.data['Topic']
        EventType = request.data['EventType']
        StartDate = request.data['StartDate']
        EndDate = request.data['EndDate']
        Cost = request.data['Cost']
        Summary = request.data['Summary']
        Content = request.data['Content']
        BenefitContent = request.data['BenefitContent']
        OrganizationalUnit = request.data['OrganizationalUnit']
        Address = request.data['Address']
        Slot = request.data['Slot']
        TargetCustomer = request.data['TargetCustomer']
        Schedule = request.data['Schedule']
        aiMarketingCode = request.data['aiMarketingCode']
        ZaloLink = request.data['ZaloLink'] 
        FanpageLink = request.data['FanpageLink']
        VideoLink = request.data['VideoLink']
        DocumentLink = request.data['DocumentLink']
        Speaker = request.data['Speaker']
        IsHideBanner = request.data['IsHideBanner']
        IsHideContent = request.data['IsHideContent']
        IsHideSchedule = request.data['IsHideSchedule']
        Inactive = request.data['Inactive']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_InsertEvent] @EventName=" + "'"+ str(EventName)+"'" + ", @Banner=" + "'"+ str(Banner)+"'" + ", @BannerMobile=" + "'"+ str(BannerMobile)+"'" + ", @Avatar=" + "'"+ str(Avatar)+"'" + ", @Topic=" + "'"+ str(Topic)+"'" + ", @EventType=" + "'"+ str(EventType)+"'" + ", @StartDate=" + "'"+ str(StartDate)+"'" + ", @EndDate=" + "'"+ str(EndDate)+"'" + ", @Cost=" + "'"+ str(Cost)+"'" + ", @Summary=" + "'"+ str(Summary)+"'" + ", @Content=" + "'"+ str(Content)+"'" + ", @BenefitContent=" + "'"+ listToString(BenefitContent)+ "'" + ", @OrganizationalUnit=" + "'"+ str(OrganizationalUnit)+"'" + ", @Address=" + "'"+ str(Address)+"'" + ", @Slot=" + "'"+ str(Slot)+"'" + ", @TargetCustomer=" + "'"+ str(TargetCustomer)+"'" + ", @Schedule=" + "'"+ str(Schedule)+"'" + ", @aiMarketingCode=" + "'"+ str(aiMarketingCode)+"'" + ", @ZaloLink=" + "'"+ str(ZaloLink)+"'" + ", @FanpageLink=" + "'"+ str(FanpageLink)+"'" + ", @VideoLink=" + "'"+ str(VideoLink)+"'" + ", @DocumentLink=" + "'"+ str(DocumentLink)+"'" + ", @Speaker=" + "'"+ listToString(Speaker)+"'" + ", @IsHideBanner=" + "'"+ str(IsHideBanner)+"'" + ", @IsHideContent=" + "'"+ str(IsHideContent)+"'" + ", @IsHideSchedule=" + "'"+ str(IsHideSchedule)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
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

class UpdateEvent(APIView):
    def put(self,request):
        cursor = connection.cursor()
        EventID = request.data['EventID']
        EventName = request.data['EventName']
        Banner = request.data['Banner']
        BannerMobile = request.data['BannerMobile']
        Avatar = request.data['Avatar']
        Topic = request.data['Topic']
        EventType = request.data['EventType']
        StartDate = request.data['StartDate']
        EndDate = request.data['EndDate']
        Cost = request.data['Cost']
        Summary = request.data['Summary']
        Content = request.data['Content']
        BenefitContent = request.data['BenefitContent']
        OrganizationalUnit = request.data['OrganizationalUnit']
        Address = request.data['Address']
        Slot = request.data['Slot']
        TargetCustomer = request.data['TargetCustomer']
        Schedule = request.data['Schedule']
        aiMarketingCode = request.data['aiMarketingCode']
        ZaloLink = request.data['ZaloLink']
        FanpageLink = request.data['FanpageLink']
        VideoLink = request.data['VideoLink']
        DocumentLink = request.data['DocumentLink']
        Speaker = request.data['Speaker']
        IsHideBanner = request.data['IsHideBanner']
        IsHideContent = request.data['IsHideContent']
        IsHideSchedule = request.data['IsHideSchedule']
        Inactive = request.data['Inactive']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        try:
            cursor.execute("EXEC [dbo].[Proc_UpdateEvent] @EventID=" + str(EventID) + ", @EventName=" + "'"+ str(EventName)+"'" + ", @Banner=" + "'"+ str(Banner)+"'" + ", @BannerMobile=" + "'"+ str(BannerMobile)+"'" + ", @Avatar=" + "'"+ str(Avatar)+"'" + ", @Topic=" + "'"+ str(Topic)+"'" + ", @EventType=" + "'"+ str(EventType)+"'" + ", @StartDate=" + "'"+ str(StartDate)+"'" + ", @EndDate=" + "'"+ str(EndDate)+"'" + ", @Cost=" + "'"+ str(Cost)+"'" + ", @Summary=" + "'"+ str(Summary)+"'" + ", @Content=" + "'"+ str(Content)+"'" + ", @BenefitContent=" + "'"+ listToString(BenefitContent)+ "'" + ", @OrganizationalUnit=" + "'"+ str(OrganizationalUnit)+"'" + ", @Address=" + "'"+ str(Address)+"'" + ", @Slot=" + "'"+ str(Slot)+"'" + ", @TargetCustomer=" + "'"+ str(TargetCustomer)+"'" + ", @Schedule=" + "'"+ str(Schedule)+"'" + ", @aiMarketingCode=" + "'"+ str(aiMarketingCode)+"'" + ", @ZaloLink=" + "'"+ str(ZaloLink)+"'" + ", @FanpageLink=" + "'"+ str(FanpageLink)+"'" + ", @VideoLink=" + "'"+ str(VideoLink)+"'" + ", @DocumentLink=" + "'"+ str(DocumentLink)+"'" + ", @Speaker=" + "'"+ listToString(Speaker)+"'" + ", @IsHideBanner=" + "'"+ str(IsHideBanner)+"'" + ", @IsHideContent=" + "'"+ str(IsHideContent)+"'" + ", @IsHideSchedule=" + "'"+ str(IsHideSchedule)+"'" + ", @Inactive=" + "'"+ str(Inactive)+"'" + ", @CreatedBy=" + "'"+ str(CreatedBy)+"'" + ", @CreatedDate=" + "'"+ str(CreatedDate)+"'" + ", @ModifiedBy=" + "'"+ str(ModifiedBy)+"'" + ", @ModifiedDate=" + "'"+ str(ModifiedDate)+"'")
            return Response({
                "message": "Sửa thành công",
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
class getPagingEvent(APIView):
    def get(self, request, one=False):
        cursor = connection.cursor()
        pageIndex = request.data['PageIndex']
        pageSize = request.data['PageSize']
        where = request.data['Where']
        sort = request.data['Sort']
        totalRecord = request.data['TotalRecord']
        cursor.execute("EXEC [dbo].[Proc_GetPagingEvent] @PageIndex=" + str(pageIndex) + ", @PageSize=" + str(pageSize) + ", @Where=" + "'"+ str(where)+"'" + ", @Sort=" + "'"+ str(sort)+"'" + ", @TotalRecord=" + str(totalRecord))
        print(cursor.fetchall())
        # r = [dict((cursor.description[i][0], value) \
        #     for i, value in enumerate(row)) for row in cursor.fetchall()]
        return Response({
            "data": {}
            },
            status=status.HTTP_200_OK
        )