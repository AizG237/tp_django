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
        fields = ["salle","debut","fin","motif","statut","cree_le","utilisateur"]
        read_only_fields = ["utilisateur"]

    def validate(self, data):
    #     debut = data["debut"]
    #     fin = data["fin"]    Echech en cas de POST
    #     salle = data["salle"]
    #     statut = data["statut"]
        if self.instance is None:
            debut = data["debut"]
            fin = data["fin"]
            salle = data["salle"]
            statut = data.get("statut", Reservation.Statut.CONFIRMEE)
        else:
            debut = data.get("debut", self.instance.debut)
            fin = data.get("fin", self.instance.fin)
            salle = data.get("salle", self.instance.salle)
            statut = data.get("statut", self.instance.statut)

      # Logques de validation

        if fin <= debut:
            raise serializers.ValidationError("Date de debut doit etre anterieure a la date de fin")

        same_room = Reservation.objects.filter(salle=salle, statut=Reservation.Statut.CONFIRMEE, debut__lt=fin, fin__gt=debut)

        if self.instance is None and same_room.exists():
            raise serializers.ValidationError("Il y a deja une reservation confirmee pour cette salle a cette periode")

        if self.instance is not None and same_room.exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Il y a deja une reservation confirmee pour cette salle a cette periode")


        return data


