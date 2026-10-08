"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ["nom", "capacite", "batiment"]

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["salle","debut","fin","motif","statut","cree_le"]
        read_only_fields = ["utilisateur"]

    def validate(self, data):
        debut = data["debut"]
        fin = data["fin"]
        salle = data["salle"]
        statut = data["statut"]

      # Logques de validation

        if debut > fin :
            raise serializers.ValidationError("Date de debut doit etre anterieure a la date de fin")
        same_room = Reservation.objects.filter(salle=salle, statut="CONFIRMEE",debut__lt=fin, fin__gt=debut)
  
        if same_room.exists():
            raise serializers.ValidationError("Il y a deja une reservation confirmee pour cette salle a cette periode")

        if same_room.exists() and same_room.filter(id=self.instance.id).exists():
            raise serializers.ValidationError("Il y a deja une reservation confirmee pour cette salle a cette periode")

        
        return data


