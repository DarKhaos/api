from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Pack
from .serializers import PackSerializer


@api_view(['GET'])
def get_all_product_tags(request, product_id=None):
    response = None
    try:
        packs = Pack.objects.filter(id=product_id, product__tags__name='tag1')
        if len(packs) > 0:
            response = Response(PackSerializer(packs, many=True).data)
        response = Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    except Pack.DoesNotExist:
        response = Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    return response