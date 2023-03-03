from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
import uuid

class deleteLeadScoringByEmail(APIView):
    def delete(self, request, email):
        cursor = connection.cursor()
        try:
            cursor.execute("EXEC [dbo].[Proc_DeleteLeadScoringByEmail] @Email=" + "'"+ str(email)+"'")
            return Response({
                "message": "Xóa thành công",
                "email":email
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
class updateLeadScoringByEmail(APIView):
    def put(self, request, email):
        cursor = connection.cursor()
        try:
            fullName = request.data['FullName']
            phone = request.data['Phone']
            position = request.data['Position']
            career = request.data['Career']
            scale = request.data['Scale']
            doSurvey = request.data['DoSurvey']
            openEmailNumber = request.data['OpenEmailNumber']
            visitNumber = request.data['VisitNumber']
            downloadNumber = request.data['DownloadNumber']
            seminarRegisterNumber = request.data['SeminarRegisterNumber']
            seminarVisitNumber = request.data['SeminarVisitNumber']
            trialNumber = request.data['TrialNumber']
            advisoryNumber = request.data['AdvisoryNumber']
            newsletterRegister = request.data['NewsletterRegister']
            messengerInteration = request.data['MessengerInteration']
            ACT_Topic = request.data['ACT_Topic']
            CRM_Topic = request.data['CRM_Topic']
            HRM_Topic = request.data['HRM_Topic']
            BIL_Topic = request.data['BIL_Topic']
            RTL_Topic = request.data['RTL_Topic']
            MGM_Topic = request.data['MGM_Topic'],
            Lead_Scoring = request.data['Lead_Scoring']
            CreatedDate = request.data['CreatedDate']
            ModifiedDate = request.data['ModifiedDate']
            CreatedBy = request.data['CreatedBy']
            ModifiedBy = request.data['ModifiedBy']
            cursor.execute('EXEC [dbo].[Proc_UpdateLeadScoringByEmail] @Email=' + "'"+ str(email)+"'" + ', @FullName=' + "'"+ str(fullName)+"'" + ', @Phone=' + "'"+ str(phone)+"'" + ', @Position=' + "'"+ str(position)+"'" + ', @Career=' + "'"+ str(career)+"'" + ', @Scale=' + "'"+ str(scale)+"'" + ', @DoSurvey=' + "'"+ str(doSurvey)+"'" + ', @OpenEmailNumber=' + "'"+ str(openEmailNumber)+"'" + ', @VisitNumber=' + "'"+ str(visitNumber)+"'" + ', @DownloadNumber=' + "'"+ str(downloadNumber)+"'" + ', @SeminarRegisterNumber=' + "'"+ str(seminarRegisterNumber)+"'" + ', @SeminarVisitNumber=' + "'"+ str(seminarVisitNumber)+"'" + ', @TrialNumber=' + "'"+ str(trialNumber)+"'" + ', @AdvisoryNumber=' + "'"+ str(advisoryNumber)+"'" + ', @NewsletterRegister=' + "'"+ str(newsletterRegister)+"'" + ', @MessengerInteration=' + "'"+ str(messengerInteration)+"'" + ', @ACT_Topic=' + "'"+ str(ACT_Topic)+"'" + ', @CRM_Topic=' + "'"+ str(CRM_Topic)+"'" + ', @HRM_Topic=' + "'"+ str(HRM_Topic)+"'" + ', @BIL_Topic=' + "'"+ str(BIL_Topic)+"'" + ', @RTL_Topic=' + "'"+ str(RTL_Topic)+"'" + ', @MGM_Topic=' + "'"+ str(MGM_Topic)+"'" + ', @Lead_Scoring=' + "'"+ str(Lead_Scoring)+"'" + ', @CreatedDate=' + "'"+ str(CreatedDate)+"'" + ', @ModifiedDate=' + "'"+ str(ModifiedDate)+"'" + ', @CreatedBy=' + "'"+ str(CreatedBy)+"'" + ', @ModifiedBy=' + "'"+ str(ModifiedBy)+"'")
            return Response({
                "message": "Cập nhật thành công",
                "email":email
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
class synchronizedLeadScoring(APIView):
    def put(self,request,email):
        cursor = connection.cursor()
        fullName = request.data['FullName']
        phone = request.data['Phone']
        position = request.data['Position']
        career = request.data['Career']
        scale = request.data['Scale']
        doSurvey = request.data['DoSurvey']
        openEmailNumber = request.data['OpenEmailNumber']
        visitNumber = request.data['VisitNumber']
        downloadNumber = request.data['DownloadNumber']
        seminarRegisterNumber = request.data['SeminarRegisterNumber']
        seminarVisitNumber = request.data['SeminarVisitNumber']
        trialNumber = request.data['TrialNumber']
        advisoryNumber = request.data['AdvisoryNumber']
        newsletterRegister = request.data['NewsletterRegister']
        messengerInteration = request.data['MessengerInteration']
        ACT_Topic = request.data['ACT_Topic']
        CRM_Topic = request.data['CRM_Topic']
        HRM_Topic = request.data['HRM_Topic']
        BIL_Topic = request.data['BIL_Topic']
        RTL_Topic = request.data['RTL_Topic']
        MGM_Topic = request.data['MGM_Topic']
        # Lead_Scoring = request.data['Lead_Scoring']
        CreatedDate = request.data['CreatedDate']
        ModifiedDate = request.data['ModifiedDate']
        CreatedBy = request.data['CreatedBy']
        ModifiedBy = request.data['ModifiedBy']
        cursor.execute('EXEC [dbo].[Proc_SynchronizedLeadScoring] @Email=' + "'"+ str(email)+"'" + ', @FullName=' + "'"+ str(fullName)+"'" + ', @Phone=' + "'"+ str(phone)+"'" + ', @Position=' + "'"+ str(position)+"'" + ', @Career=' + "'"+ str(career)+"'" + ', @Scale=' + "'"+ str(scale)+"'" + ', @DoSurvey=' + "'"+ str(doSurvey)+"'" + ', @OpenEmailNumber=' + "'"+ str(openEmailNumber)+"'" + ', @VisitNumber=' + "'"+ str(visitNumber)+"'" + ', @DownloadNumber=' + "'"+ str(downloadNumber)+"'" + ', @SeminarRegisterNumber=' + "'"+ str(seminarRegisterNumber)+"'" + ', @SeminarVisitNumber=' + "'"+ str(seminarVisitNumber)+"'" + ', @TrialNumber=' + "'"+ str(trialNumber)+"'" + ', @AdvisoryNumber=' + "'"+ str(advisoryNumber)+"'" + ', @NewsletterRegister=' + "'"+ str(newsletterRegister)+"'" + ', @MessengerInteration=' + "'"+ str(messengerInteration)+"'" + ', @ACT_Topic=' + "'"+ str(ACT_Topic)+"'" + ', @CRM_Topic=' + "'"+ str(CRM_Topic)+"'" + ', @HRM_Topic=' + "'"+ str(HRM_Topic)+"'" + ', @BIL_Topic=' + "'"+ str(BIL_Topic)+"'" + ', @RTL_Topic=' + "'"+ str(RTL_Topic)+"'" + ', @MGM_Topic=' + "'"+ str(MGM_Topic)+"'" + ', @CreatedDate=' + "'"+ str(CreatedDate)+"'" + ', @ModifiedDate=' + "'"+ str(ModifiedDate)+"'" + ', @CreatedBy=' + "'"+ str(CreatedBy)+"'" + ', @ModifiedBy=' + "'"+ str(ModifiedBy)+"'")
        return Response({
            "message": "Cập nhật thành công",
            "email":email
            },
            status=status.HTTP_200_OK
        )
