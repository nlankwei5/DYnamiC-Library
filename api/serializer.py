from rest_framework import serializers 
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =  ['user_id', 'email', 'username', 'first_name', 'last_name','is_admin' ]
        read_only_fields = ['is_admin']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']

class MusicSheetSerializer(serializers.ModelSerializer):
    uploaded_by_username = serializers.CharField(source='uploaded_by.username', read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    
    class Meta:
        model = MusicSheet
        fields = ['title', 'file', 'date_uploaded','uploaded_by', 'uploaded_by_username', 'category', 'category_name']
        read_only_fields = ['uploaded_by_username', 'date_uploaded', 'uploaded_by']

    def validate_file(self, value):
        if not value.name.endswith('.pdf'):
            raise  serializers.ValidationError("Only PDF files are allowed.")

        return value
