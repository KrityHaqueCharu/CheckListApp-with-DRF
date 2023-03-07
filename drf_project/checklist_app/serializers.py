from rest_framework import serializers
from checklist_app.models import CheckList


#THIS IS ONE WAY
# class CheckListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()

#THIS IS ANOTHER WAY
class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'