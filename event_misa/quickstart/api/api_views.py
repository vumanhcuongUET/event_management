from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .api_bannerSlide import bannerSlideList, deleteBannerSlideByID, InsertBannerSlide
from .api_event import getEventByID, deleteEventByID,InsertEvent, getAllEvent
from .api_speaker import getSpeakerList, getSpeakerByID, deleteSpeakerByID
from .api_user import getUserByEventID