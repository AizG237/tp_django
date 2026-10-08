"""Tache 3 : brancher les ViewSets sur un DefaultRouter.

Les routes attendues sont (prefixe /api/ deja fourni par config/urls.py) :
  /api/salles/            /api/salles/{id}/
  /api/reservations/      /api/reservations/{id}/
  /api/salles/{id}/occupation/
"""
from rest_framework.routers import DefaultRouter
from . import views
# TODO : votre code ici
router = DefaultRouter()
router.register('salles', views.SalleViewSet)
router.register('reservations', views.ReservationViewSet)
urlpatterns = router.urls