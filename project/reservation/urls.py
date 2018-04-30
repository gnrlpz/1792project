from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    # path('', views.index, name='index')
    url(r'^users/$', views.UserList.as_view()),
    url(r'^user/(?P<username>[0-9a-zA-Z_-]+)/$', views.UserDetail.as_view()),
    # url(r'^rooms/$', views.RoomList.as_view()),
    # url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view()),
    url(r'^appointments/$', views.AppointmentList.as_view()),
    url(r'^appointment/(?P<pk>[0-9]+)/$', views.AppointmentDetail.as_view()),

    # url(r'^api/$', get_schema_view()),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]