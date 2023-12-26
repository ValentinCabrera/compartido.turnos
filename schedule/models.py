from django.db import models
from accounts.models import User

class Schedule(models.Model):
    STATES = [
        [1, 'enabled'],
        [2, 'disabled']
    ]

    date = models.DateField(unique=True)
    state = models.SmallIntegerField(choices=STATES, default=1)
    appointment_duration = models.SmallIntegerField()

    profesional = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='schedules')

    def __str__(self):
        return f'{self.profesional} - {self.date}'

class Appointment(models.Model):
    STATES = [
        [1, 'free'],
        [2, 'busy']
    ]

    time = models.TimeField()
    duration = models.PositiveSmallIntegerField()
    state = models.SmallIntegerField(choices=STATES, default=1)

    schedule = models.ForeignKey(Schedule, on_delete=models.RESTRICT, related_name='appointments')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='appointments')

    def __str__(self):
        return f'{self.user} - {self.schedule.date} - {self.time}'
