from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSeriazlier
from .models import Todo
 
# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
           'status' : 200,
           'message' : 'Yes! Django rest framework is working!!',
           'method_called' : 'Uou called GET method'
        })

    elif request.method == 'POST':
        return Response({
           'status' : 200,
           'message' : 'Yes! Django rest framework is working!!',
           'method_called' : 'Uou called POST method'
        })

    elif request.method == 'PATCH':
        return Response({
           'status' : 400,
           'message' : 'Yes! Django rest framework is working!!',
           'method_called' : 'Uou called PATCH method'
        })    

    else:
        return Response({
           'status' : 200,
           'message' : 'Yes! Django rest framework is working!!',
           'method_called' : 'Uou called invalid method'
        })


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSeriazlier(todo_objs, many = True)

    return Response({
        'status' : True,
        'message' : 'Todo fetched',
        'data' : serializer.data
    })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSeriazlier(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
               'status' : True,
               'message' : 'success!!',
               'data' : serializer.data
    })
        return Response({
          'status' : False,
          'message' : 'invalid data',
        'data' : serializer.errors
    })
   


            
    except Exception as e:
        print(e) 
    
    return Response({
        'status' : False,
        'message' : 'Something went wrong!!'
    })

    #TodoSeriazlier

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status' : False,
                'message': 'uid is required',
                'data' : {}
            })

        obj = Todo.objects.get(uid = data.get('uid'))

        serialize = TodoSeriazlier(obj, data = data, partial = True)
        if serialize.is_valid():
            serialize.save()     
            return Response({
                'status' : True,
                'message': 'success data',
                'data' : serialize.data
        })
        return Response({
            'status' : False,
            'message' : 'invalid data',
            'data' : serialize.errors
      })

    except Exception as e:
            print(e)
    return Response({
            'status' : False,
            'message' : 'invalid uid',
            'data' : {}
      })        



@api_view(['DELETE'])
def delete_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSeriazlier(todo_objs, many = True)

    return Response({
        'status' : True,
        'message' : 'Todo fetched',
        'data' : serializer.data
    })      