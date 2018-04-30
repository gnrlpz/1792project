from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseClass(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Room(BaseClass):
#     room_name = models.CharField(max_length=255, unique=True)
#     building_name = models.CharField(max_length=255)

#     def __str__(self):
#         return '[%s] %s' % (self.building_name, self.room_name)

# class Timeslot(BaseClass):
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     room = models.ForeignKey(Room, related_name='available_timeslots', on_delete=models.CASCADE)

#     def __str__(self):
#         return '%s to %s' % (self.start_time, self.end_time)

class Appointment(BaseClass):
    date = models.DateField()
    # room = models.ForeignKey(Room, related_name='appointment', on_delete=models.CASCADE)
    # timeslot = models.ForeignKey(Timeslot, related_name='appointment', on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '%s - %s on %s at %s' % (self.start_time, self.end_time, self.date, self.room_name)