from .models import Schedule, Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ["time", "duration", "state"]

    def get_state(self, obj):
        return obj.get_state_display()
class ScheduleSerializer(serializers.ModelSerializer):
    appointments = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ["date", "state", "appointments"]

    def get_appointments(self, obj):
        appointments = obj.appointments.all()
        serializer = AppointmentSerializer(appointments, many=True)

        return serializer.data

    def get_state(self, obj):
        return obj.get_state_display()