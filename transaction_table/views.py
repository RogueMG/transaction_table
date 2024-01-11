from rest_framework import generics
from .models import CustomUser, HostelAdmin, Warden, Parent, Hostel, Rooms, Student
from .models import Attendance, AttendanceReport, OutPassStudent, OutPassWarden, MaintenanceRequestStudent
from .models import MaintenanceRequestWarden, NotificationsStudent, NotificationsWarden
from .serializers import CustomUserSerializer, HostelAdminSerializer, WardenSerializer
from .serializers import ParentSerializer, HostelSerializer, RoomsSerializer, StudentSerializer
from .serializers import AttendanceSerializer, AttendanceReportSerializer, OutPassStudentSerializer
from .serializers import OutPassWardenSerializer, MaintenanceRequestStudentSerializer
from .serializers import MaintenanceRequestWardenSerializer, NotificationsStudentSerializer, NotificationsWardenSerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class HostelAdminList(generics.ListCreateAPIView):
    queryset = HostelAdmin.objects.all()
    serializer_class = HostelAdminSerializer

class HostelAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostelAdmin.objects.all()
    serializer_class = HostelAdminSerializer

class WardenList(generics.ListCreateAPIView):
    queryset = Warden.objects.all()
    serializer_class = WardenSerializer

class WardenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warden.objects.all()
    serializer_class = WardenSerializer

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class HostelList(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class HostelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class RoomsList(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class RoomsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceReportList(generics.ListCreateAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer

class AttendanceReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer

class OutPassStudentList(generics.ListCreateAPIView):
    queryset = OutPassStudent.objects.all()
    serializer_class = OutPassStudentSerializer

class OutPassStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutPassStudent.objects.all()
    serializer_class = OutPassStudentSerializer

class OutPassWardenList(generics.ListCreateAPIView):
    queryset = OutPassWarden.objects.all()
    serializer_class = OutPassWardenSerializer

class OutPassWardenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutPassWarden.objects.all()
    serializer_class = OutPassWardenSerializer

class MaintenanceRequestStudentList(generics.ListCreateAPIView):
    queryset = MaintenanceRequestStudent.objects.all()
    serializer_class = MaintenanceRequestStudentSerializer

class MaintenanceRequestStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequestStudent.objects.all()
    serializer_class = MaintenanceRequestStudentSerializer

class MaintenanceRequestWardenList(generics.ListCreateAPIView):
    queryset = MaintenanceRequestWarden.objects.all()
    serializer_class = MaintenanceRequestWardenSerializer

class MaintenanceRequestWardenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequestWarden.objects.all()
    serializer_class = MaintenanceRequestWardenSerializer

class NotificationsStudentList(generics.ListCreateAPIView):
    queryset = NotificationsStudent.objects.all()
    serializer_class = NotificationsStudentSerializer

class NotificationsStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotificationsStudent.objects.all()
    serializer_class = NotificationsStudentSerializer

class NotificationsWardenList(generics.ListCreateAPIView):
    queryset = NotificationsWarden.objects.all()
    serializer_class = NotificationsWardenSerializer

class NotificationsWardenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotificationsWarden.objects.all()
    serializer_class = NotificationsWardenSerializer

