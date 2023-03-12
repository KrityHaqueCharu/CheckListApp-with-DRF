from rest_framework import serializers
from checklist_app.models import CheckList,CheckListItem


#THIS IS ONE WAY
# class CheckListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()

#THIS IS ANOTHER WAY

class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'

class CheckListSerializer(serializers.ModelSerializer):
    items = CheckListItemSerializer(source='checklistitem_set', many=True,read_only=True)
    class Meta:
        model = CheckList
        fields = '__all__'

