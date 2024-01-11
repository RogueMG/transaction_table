
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_choices= ((1,"ADMIN"),(2,"WARDEN"),(3,"STUDENT"),(4,"PARENT"))
    user_type = models.CharField(default = 1, choices=user_type_choices, max_length=10)

class HostelAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class Warden(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=12)
    objects = models.Manager()

class Hostel(models.Model):
    id = models.AutoField(primary_key=True)
    hostel_name = models.CharField(max_length = 255)
    no_of_rooms = models.IntegerField(default = 1)
    warden_id = models.ForeignKey(Warden, on_delete=models.CASCADE)
    objects = models.Manager()

class Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    room_no = models.IntegerField(default = 1)
    hostel_id = models.ForeignKey(Hostel, on_delete = models.CASCADE)
    objects = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 255)
    hostel_id = models.ForeignKey(Hostel, on_delete=models.DO_NOTHING)
    room_id = models.ForeignKey(Rooms, on_delete = models.DO_NOTHING)
    objects = models.Manager()


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    hostel_id = models.ForeignKey(Warden, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()

class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    objects = models.Manager()

class OutPassStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    from_date = models.DateField(default = datetime.today)
    to_date = models.DateField(default = datetime.today)
    reason = models.TextField()
    status = models.BooleanField(default = False)
    objects = models.Manager()

class OutPassWarden(models.Model):
    id = models.AutoField(primary_key=True)
    warden_id = models.ForeignKey(Warden, on_delete=models.CASCADE)
    from_date = models.DateField(default = datetime.today)
    to_date = models.DateField(default = datetime.today)
    reason = models.TextField()
    status = models.BooleanField(default = False)
    objects = models.Manager()

class MaintenanceRequestStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student , on_delete = models.CASCADE)
    request = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class MaintenanceRequestWarden(models.Model):
    id = models.AutoField(primary_key=True)
    warden_id = models.ForeignKey(Warden, on_delete = models.CASCADE)
    request = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class NotificationsStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class NotificationsWarden(models.Model):
    id = models.AutoField(primary_key=True)
    warden_id = models.ForeignKey(Warden, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

@receiver(post_save, sender=CustomUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            HostelAdmin.objects.create(admin=instance)
        if instance.user_type==2:
            Warden.objects.create(admin=instance)
        if instance.user_type==3:
            Student.objects.create(admin=instance)
        if instance.user_type==4:
            Parent.objects.create(admin=instance)
        
@receiver(post_save, sender=CustomUser)
def save_user(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.hosteladmin.save()
    if instance.user_type==2:
        instance.warden.save()
    if instance.user_type==3:
        instance.student.save()
    if instance.user_type==4:
        instance.parent.save