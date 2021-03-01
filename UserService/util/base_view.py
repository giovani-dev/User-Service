# Utilidade: Podemos utilizar em funcionalidades genericas o suficiente para que possam corresponder com praticamente todo codigo
# Onde Utilizar: Basicamnete em todas as views que tenham o mesmo comportamento citado anteriormente 

from typing import Any

from django.core.cache import cache

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from util.pagination import CustomPagination

# Funcionalidade: Registro utilizando serializer
class CreateView(generics.CreateAPIView):

    def perform_create(self, serializer):
        serializer.save()

# Funcionalidade: Listagem com paginacao, utilizando querysets e serializers
class ListAllView(generics.ListAPIView):
    QUERY = None
    pagination_class = CustomPagination

    def get_queryset(self):
        return self.QUERY

class GetUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    MODEL = object()
    SLUG_TAG = str()
    ERROR_MSG_QUERY_DOES_NOT_EXIST = str()

    def retrieve(self, request, *args, **kwargs):
        response_cached = cache.get(self.kwargs[self.SLUG_TAG])
        if response_cached:
            return Response(response_cached)
        else:
            instance = self.get_object()
            data = self.serializer_class(instance).data
            self.set_cache(data=data)
            return Response(data)

    def put(self, request, *args, **kwargs):
        updated = super(GetUpdateDestroyView, self).put(request, *args, **kwargs)
        self.set_cache(data=updated.data)
        return updated

    def get_object(self):
        try:
            if self.request.method == "DELETE":
                cache.delete(self.kwargs[self.SLUG_TAG])
            return self.MODEL.objects.get(identifier=self.kwargs[self.SLUG_TAG])
        except self.MODEL.DoesNotExist:
            raise NotFound(detail=self.ERROR_MSG_QUERY_DOES_NOT_EXIST)
    
    def set_cache(self, data: Any):
        cache.set(self.kwargs[self.SLUG_TAG], data)