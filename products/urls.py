from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Articon API",
      default_version='v1',
      description="Description goes here",
      terms_of_service="http://localhost:8000/api/categories/doc/",
      contact=openapi.Contact(email="contact@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('categories/', views.CategoryList.as_view(), name='categories'),
   path('categories/<int:pk>/', views.CategoryDetail.as_view()),
   path('', views.ProductList.as_view(), name='categories'),
   path('<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)