from rest_framework import serializers
from musica.models import Musica
from artista.serializers import ArtistaSerializer
from artista.models import Artista


class MusicaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    genero = serializers.CharField(read_only=True)
    artista = ArtistaSerializer(
        many=True,
        read_only=True
    )
    
    def create(self, validated_data):
        musica = Musica.objects.create(**validated_data)
        return musica

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.genero = validated_data.get('genero')
        instance.save()
        return instance