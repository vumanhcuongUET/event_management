from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .api_bannerSlide import bannerSlideList, deleteBannerSlideByID, InsertBannerSlide, updateBannerSlide
from .api_event import getEventByID, deleteEventByID,InsertEvent, getAllEvent,UpdateEvent,getPagingEvent
from .api_speaker import getSpeakerList, getSpeakerByID, deleteSpeakerByID, InsertSpeaker,UpdateSpeaker
from .api_user import getUserByEventID,insertUser
from .api_leadScoring import deleteLeadScoringByEmail,updateLeadScoringByEmail,synchronizedLeadScoring
from .api_employee import getPagingEmployee