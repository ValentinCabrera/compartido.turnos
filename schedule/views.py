from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer

class SheduleView(APIView):
    def post(self, request):
        shedules = Schedule.objects.all()
        serializer = ScheduleSerializer(shedules, many=True)

        return Response(serializer.data)


