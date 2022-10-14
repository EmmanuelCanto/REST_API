from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    '''Serealizar un campo para probar nuestro APIView'''
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializa objeto de perfil de usuario'''
        
    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
        
    def create(self, validate_data):
        '''Crear y retornar nuevo usuario'''
        user=models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        '''Crear y retornar nuevo usuario'''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            
        return super().update(instance, validated_data)