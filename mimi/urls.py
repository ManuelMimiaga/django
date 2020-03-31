from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
schema_view = get_swagger_view(title='Mimiaga')


urlpatterns = [
	path('admin/', admin.site.urls),
	re_path(r'^',include(router.urls)),
	re_path(r'^api/v1/',include('Login.urls')),
	re_path(r'^api/v1/',include('Profile.urls')),
	url(r'^swagger/',schema_view),
	path(r'accounts/',include('rest_framework.urls'))
]
