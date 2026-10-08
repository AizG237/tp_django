"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets

from salles.serializers import ReservationSerializer, SalleSerializer

from .models import Reservation, Salle

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response


from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework import status
# TODO : votre code ici



class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

    @action(detail=True, methods=["get"])
    def get_occupation(self,request):
        resp= None
        try:
            debut = parse_datetime(request.query_params.get("debut", ""))
            fin = parse_datetime(request.query_params.get("fin", ""))
        except ValueError:
            pass 
        if debut is None or fin is None:
            return Response(
                {"detail": "Les parametres debut et fin sont obligatoires, au format ISO 8601."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"message": resp})


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)

  
        

