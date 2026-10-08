"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets

from salles.serializers import ReservationSerializer, SalleSerializer

from .models import Reservation, Salle


# TODO : votre code ici

class SalleViewSet(viewsets.ModelViewSet):
    serializer_class = SalleSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

  
        

