from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.PositiveSmallIntegerField()
    course_name = models.CharField(max_length=30)
    course_department = models.CharField(max_length = 30)
    course_prerequisites = models.CharField(max_length = 50)
    teacher_id = models.PositiveSmallIntegerField()
    teacher_first_name = models.CharField(max_length=20)
    teacher_last_name = models.CharField(max_length=20)
    contact_details = models.CharField(max_length = 20)
    course_requirements = models.CharField(max_length = 30)
    course_capacity = models.PositiveSmallIntegerField()
    

    def __str__(self):
        return f"{self.course_id} {self.course_name}"
