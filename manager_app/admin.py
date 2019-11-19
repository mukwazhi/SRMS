from django.contrib import admin
from .models import Course,JobTitle,Trainer,TrainingRecord, Department,Section, Employee, CourseResources

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name', 'course_description','trainer']

class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','department_name']

class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','section_name', 'department']

class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ['id','staff_number', 'course','trainer','training_date','training_expiry']

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id','trainer_name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'employee_surname', 'staff_number','job_title','department', 'section']

class CourseResourcesAdmin(admin.ModelAdmin):
    list_display = ['id','title','trainer', 'course','file']


admin.site.register(Course, CourseAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(TrainingRecord, TrainingRecordAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CourseResources, CourseResourcesAdmin)
