"""django_mongodb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from tutorials import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'snippet', views.SnippetList)
# router.register(r'snippetdetail', views.SnippetDetail)
# router.register(r'snippet1', views.SnippetList1)
# router.register(r'snippetdetail1', views.SnippetDetail1)
# router.register(r'userlist', views.UserList)
# router.register(r'userdetail', views.UserDetail)
router.register(r'snippetview', views.SnippetViewSet)
router.register(r'userview', views.UserViewSet1)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# swagger 接口文档
schema_view = get_schema_view(
    openapi.Info(
        title="HelloDjango REST framework tutorial API",
        default_version="v1",
        description="HelloDjango REST framework tutorial AP",
        terms_of_service="",
        contact=openapi.Contact(email="zmrenwu@163.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('snippet/', include("tutorials.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 接口文档配置
    re_path(r"swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json", ),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
