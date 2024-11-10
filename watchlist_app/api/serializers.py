from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"  # ["id", "name", "description"]
        # exclude = ["active"]

    # Type 1: Field Leval Validator
    def validate_name(self, value):
        if len(value) < 2 or len(value) > 50:
            raise serializers.ValidationError(
                "Name must be between 5 and 50 characters long."
            )
        return value

    # Type 2: Object Leval Validation
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description cannot be the same."
            )
        return data


# # Type 3: Validator
# def description_length(data):
#     if len(data) < 5 or len(data) > 200:
#         raise serializers.ValidationError(
#             "Description must be between 5 and 200 characters long."
#         )
#     return data


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     # Type 1: Field Leval Validator
#     def validate_name(self, value):
#         if len(value) < 2 or len(value) > 50:
#             raise serializers.ValidationError(
#                 "Name must be between 5 and 50 characters long."
#             )
#         return value

#     # Type 2: Object Leval Validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError(
#                 "Title and Description cannot be the same."
#             )
#         return data

#     # Type 3: Validator defined on the top
