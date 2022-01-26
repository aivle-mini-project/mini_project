from rest_framework import serializers
from diary.models import Diary, Expression


class DiarySerializer(serializers.ModelSerializer):
  writer = serializers.StringRelatedField()
  # expression = Expression.objects.filter(user=str(writer))  

  class Meta:
    model = Diary
    fields = ['id','writer', 'write','emotion','neutral','positive','negative','register_date', 'expressions']
    depth = 3