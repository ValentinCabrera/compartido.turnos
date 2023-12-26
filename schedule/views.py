from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer
from accounts.models import User

class SheduleView(APIView):
    def post(self, request):
        profesional_id = request.data.get("profesional")

        try:
            profesional = User.objects.get(id=profesional_id)

        except:
            return Response({"error": "No se encontro el profesional."}, status=404)

        try:
            shedules = profesional.get_schedules()
            serializer = ScheduleSerializer(shedules, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=500)



