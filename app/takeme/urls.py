from rest_framework import routers
from takeme.views import TakeMe
from django.conf.urls import url

router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    url("objetivo", TakeMe.as_view()),
]
