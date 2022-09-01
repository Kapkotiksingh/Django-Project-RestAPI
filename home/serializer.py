from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify


class TodoSeriazlier(serializers.ModelSerializer):


    slug = serializers.SerializerMethodField()


    class Meta:
        model = Todo
        fields = ['todo_title', 'slug', 'todo_description', 'is_done', 'uid']
        # `exclude = ['created_at']

    def get_slug(self, obj):
        # return  slugify(obj.todo_title) 
        return "kamal"


    def validated_todo_title(self, data):
        if data:
            todo_title = data
            regex = re.compile('[@!#$%^&*()|}{?><:~]')

            if len(todo_title)<3:
                raise serializers.ValidationError("todo title must be more then 3 chars")

            if not regex.search(todo_title)== None:
                raise serializers.ValidationError('todo_title cannot contains special characters')
        

        return data
    # def validate(self, validated_data):
    #     print(validated_data)

    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@!#$%^&*()|}{?><:~]')

    #         if len(todo_title)<3:
    #             raise serializers.ValidationError("todo title must be more then 3 chars")
    #         if not regex.search(todo_title)== None:
    #             raise serializers.ValidationError('todo_title cannot contains special characters')
                  
    #     return validated_data      