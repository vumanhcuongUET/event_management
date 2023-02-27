from quickstart.models import event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
def listToString(s):
     
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += json.dumps(ele)
 
    # return string
    return str1
class getEventByID(APIView):
    def get(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_GetEventByID] @EventID=' + str(id))
            print(id)
            result_set = cursor.fetchall()
        finally:
            cursor.close()
        return Response(result_set, status=status.HTTP_200_OK)

class deleteEventByID(APIView):
    def delete(self, request, id):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[Proc_DeleteEventByID] @EventID=' + str(id))
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)

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
        finally:
            cursor.close()
        return Response(status=status.HTTP_200_OK)