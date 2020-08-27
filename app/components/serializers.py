from rest_framework import serializers

class ComponentSerializer(serializers.Serializer):
    name = models.CharField(required=True,max_length=200)
    description = models.CharField(max_length=500)
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
