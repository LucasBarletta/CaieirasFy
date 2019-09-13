from rest_framework import serializers
from artista.models import Artista
from musica.serializers import MusicaSerializer
from musica.models import Musica

class ArtistaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    musicas = MusicaSerializer(
        many=True,
        read_only=True
    )

    def create(self, validated_data):
        artista = Artista.objects.create(**validated_data)
        return artista
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.save()
        return instance
