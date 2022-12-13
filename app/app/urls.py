from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login
from rest_framework import permissions
from channel.views import ChannelList,ChannelSend
from chat.views import ChatGet
from users.views import MyDetails,Hospital,UserAddDonate
from request.views import GetDetails
from donation.views import DoctorDonation
from assestment.views import AssessmentVerification,AssessmentByHospital
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    # path('api/v1/admin/', admin.site.urls),
    path('api/v1/channellist/', ChannelList.as_view(), name='Sign up'),
    # path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/', Login.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/donation/', include('donation.urls')),
    path('api/v1/channel/', include('channel.urls')),
    path('api/v1/assessment/', include('assestment.urls')),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/location/', include('hospital.urls')),
    path('api/v1/request/', include('request.urls')),
    path('api/v1/sendMessage/', ChannelSend.as_view(), name='get_user'),
    path('api/v1/user-donate/', UserAddDonate.as_view(), name='get_user'),
    path('api/v1/blood-request/<int:hospital_id>/', GetDetails.as_view(), name='get_user'),
    path('api/v1/hospital/', Hospital.as_view(), name='get_user'),
    path('api/v1/user-details/', MyDetails.as_view(), name='get_user'),
    path('api/v1/donation-doctor/', DoctorDonation.as_view(), name='get_user'),
    path('api/v1/assessment-hospital/<int:hospital_id>/<str:status>/', AssessmentByHospital.as_view(), name='get_user'),
    path('api/v1/assessment-user/<int:user_id>/', AssessmentVerification.as_view(), name='get_user'),
    path('api/v1/chatgetall/', ChatGet.as_view(), name='get_user'),
    # path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
]