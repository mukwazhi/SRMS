from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=45, unique=True)
    course_description = models.TextField(max_length=200, null=True, blank=True)
    trainer = models.ForeignKey('Trainer', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.course_name

class JobTitle(models.Model):
    title = models.CharField(max_length=45, unique=True)


    def __str__(self):
        return self.title


class Department(models.Model):
    department_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.department_name

class Section(models.Model):
    section_name = models.CharField(max_length=45, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_name

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.trainer_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=45)
    employee_surname = models.CharField(max_length=45)
    staff_number = models.IntegerField(unique=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    mandatory_courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.employee_name +" "+ self.employee_surname



class TrainingRecord(models.Model):
    staff_number = models.IntegerField()
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    training_date = models.DateField()
    training_expiry = models.DateField()
    archive = models.BooleanField()
    certificate = models.ImageField(null=True, blank=True, upload_to='image/')


class CourseResources(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=None)
    trainer = models.ForeignKey(Trainer, on_delete=None)
    file = models.FileField(null=True,blank=True, upload_to='resources/')

