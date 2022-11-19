# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, CreateMeasurementSerializer


# @api_view(['GET', 'POST'])
# def sensors(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         serial = SensorSerializer(sensors, many=True)
#         return Response(serial.data)
#     if request.method == 'POST':
#         return Response('Hello world')


# class SensorsView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         serial = SensorSerializer(sensors, many=True)
#         return Response(serial.data)
#     def post(self, request):
#         return Response('Hello world')


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = CreateMeasurementSerializer
