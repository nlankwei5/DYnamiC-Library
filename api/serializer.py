from rest_framework import serializers 
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =  ['user_id', 'email', 'username', 'first_name', 'last_name']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']

class MusicSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicSheet
        fields = ['title', 'file', 'date_uploaded','uploaded_by', 'category']
        read_only_fields = ['uploaded_by', 'date_uploaded']

    def validate_file(self, value):
        if not value.name.endswith('.pdf'):
            raise  serializers.ValidationError("Only PDF files are allowed.")
        
        if value.content_type != 'application/pdf':
            raise serializers.ValidationError("File must be a PDF.")
        
        return value
