from rest_framework import serializers
from ..models import Subject, Course, Module
from ..models import Content
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
# ModuleSerializer параметр many=True, обозначает, что для
#  одного курса может быть множество модулей. 
# Параметр read_only сообщает фреймворку, что
#  данные вложенного сериализатора 
# не являются доступными для редактирования
class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview',
                  'created', 'owner', 'modules']        
# создали собственное поле, являющееся наследником 
# класса RelatedField фреймворка Django REST, и переопределили метод to_rep-
# resentation()
class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()
# создали сериализатор ContentSerializer для модели Con-
# tent, в котором определили поле item типа ItemRelatedField.        
class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ['order', 'item']

class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']
class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules']