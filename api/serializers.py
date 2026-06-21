from rest_framework import serializers
from .models import CarBrand,Car,Comment


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        request = self.context.get('request')
        car_id = request.data.get('car')
        author = request.user

        car = Car.objects.get(id=car_id)

        comment = Comment.objects.create(
            car=car,
            author=author,
            text=validated_data.get('text')
        )
        return comment

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        request = self.context.get('request')
        car_id = request.data.get('car')
        if car_id:
            instance.car = Car.objects.get(id=car_id)

        instance.save()
        return instance