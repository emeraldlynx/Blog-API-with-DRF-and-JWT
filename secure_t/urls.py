from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('openapi/', TemplateView.as_view(
        template_name='openapi.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='openapi'),
]
