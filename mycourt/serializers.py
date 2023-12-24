from rest_framework import serializers
from .models import *


class AdvocateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateProfile
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseType
        fields = '__all__'


class AddCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCase
        fields = '__all__'


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'


class NextListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextListening
        fields = '__all__'


class InterimOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterimOrder
        fields = '__all__'


class CaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFile
        fields = '__all__'


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespondentAdvocate
        fields = '__all__'
