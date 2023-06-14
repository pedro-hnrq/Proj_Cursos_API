from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API de Cursos com DRF
    """
    def get(self, request):
        print(dir(request))
        cursos = Curso.objects.all()
        serilizer = CursoSerializer(cursos, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        # Verificar se valido
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"curso": serializer.data['titulo'],"criação": serializer.data['criacao']}, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    """
    API de Cursos da Geek
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
