from urllib import request
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, UserRegisterSerializer,JobSerializer,WorkHistorySerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from .models import Job,WorkHistory

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()        
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#JobOverview API
@api_view(['GET'])
def jobApiOverview(request):
	api_urls = {
		'List':'/jobs/',
		'Detail View':'/jobs-detail/<str:pk>/',
		'Create':'/jobs-create/',
		'Update':'/jobs-update/<str:pk>/',
		'Delete':'/jobs=delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def jobList(request):
	jobs = Job.objects.all().order_by('-id')
	serializer = JobSerializer(jobs, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def jobDetail(request, pk):
	jobs = Job.objects.get(id=pk)
	serializer = JobSerializer(jobs, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def jobCreate(request):
	serializer = JobSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def jobUpdate(request, pk):
	job = Job.objects.get(id=pk)
	serializer = JobSerializer(instance=job, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def jobDelete(request, pk):
	job = Job.objects.get(id=pk)
	job.delete()
	return Response('Item succsesfully delete!')

@api_view(['GET'])
def workHistoryList(request,job,user):
	workHistory = WorkHistory.objects.get(job=job,user=user)
	serializer = WorkHistorySerializer(workHistory, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def workHistoryCreate(request):
	serializer = WorkHistorySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)