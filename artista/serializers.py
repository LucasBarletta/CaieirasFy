from rest_framework import serializers
from artista.models import Artista
from musica.models import Musica


class MusicaData(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)

class ArtistaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    estilo = serializers.CharField()
    musica = MusicaData(read_only=True)

    def create(self, validated_data):
        musica_data = validated_data.pop('musica_data')
        musica = Musica.objects.get(id=musica_data['id'])
        artista = Artista.objects.create(musica_data = musica, **validated_data)
        return artista

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.estilo = validated_data.get('estilo')
        musica_data = validated_data.pop('musica_data')
        musica = Musica.objects.get(id=musica_data['id'])
        instance.musica_data = musica
        instance.save()
        return instance

class ArtistaLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()