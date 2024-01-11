from rest_framework import serializers
from .models import CustomUser, HostelAdmin, Warden, Parent, Hostel, Rooms, Student, Attendance
from .models import AttendanceReport, OutPassStudent, OutPassWarden, MaintenanceRequestStudent
from .models import MaintenanceRequestWarden, NotificationsStudent, NotificationsWarden

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class HostelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelAdmin
        fields = '__all__'

class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = '__all__'

class OutPassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPassStudent
        fields = '__all__'

class OutPassWardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPassWarden
        fields = '__all__'

class MaintenanceRequestStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequestStudent
        fields = '__all__'

class MaintenanceRequestWardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequestWarden
        fields = '__all__'

class NotificationsStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationsStudent
        fields = '__all__'

class NotificationsWardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationsWarden
        fields = '__all__'
