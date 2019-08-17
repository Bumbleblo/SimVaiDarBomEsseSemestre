from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    url(r"token/", obtain_jwt_token),
]

