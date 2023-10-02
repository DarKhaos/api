from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_all_product_tags

urlpatterns = [
    re_path(r'^products/(?P<product_id>[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12})/tags/$', get_all_product_tags),
]

urlpatterns = format_suffix_patterns(urlpatterns)