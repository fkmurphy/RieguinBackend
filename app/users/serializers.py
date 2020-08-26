from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    website = serializers.CharField(max_length=140)
    #name = serializers.CharField(required=True,max_length=255)
    """
    name = serializers.CharField(required=True,max_length=255,
                validators=[
                    UniqueValidator(queryset=Profile.objects.all())
                ]
            )
    """

    """sobrescribir create update para cambiar comportamiento"""
    """
    def create(self,data):
        # en el cliente usar serializer.save()
        return Profile.objects.create(**data) 

    """
