from django.db.models import Count, QuerySet
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, Page
from django.contrib.auth.decorators import login_required

from openpyxl.styles import Alignment

from .xlsx_utils import expired_xlsx, trainingList_xlsx, untrainedlist_xlsx
from .emailAlert import autoEmail
# from .utils import generate, generateTrainedPdf, searchPdf
from .models import TrainingRecord,Trainer,Employee,Course,Department,JobTitle,Section, CourseResources
from datetime import date
from .forms import RecordForm

from django.http import JsonResponse, response, HttpResponse, HttpResponseRedirect
cm = 2.54

@login_required(login_url='/accounts/login/')
def expired(request):
    # get date values less than the current date
    department = Department.objects.all()
    course = Course.objects.all()
    job_title = JobTitle.objects.all()
    section = Section.objects.all()
    expired_info = TrainingRecord.objects.filter(training_expiry__lt = date.today()).exclude(archive=1)

    # filter by expired course
    selected_course = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('r')
    selected_title = request.GET.get('s')


    if selected_title or selected_department or selected_title or selected_section:
        # filter by course and department
        if selected_course !='0' and selected_department!= '0' and selected_section=='0' and selected_title=='0':
            expired_course = expired_info.filter(course_id=selected_course)
            expired_list = expired_course.filter(department_id=selected_department)
            paginator = Paginator(expired_list, 25)
            page = request.GET.get('page')
            expired = paginator.get_page(page)
            context = {
                     'expired_course': expired_course,
                    'expired': expired,
                    'course': course,
                    'department': department,
                    'job_title': job_title,
                    "section": section,
                 }

            return render(request, 'expired.html', context) #filtered_course_department.html

        # filter by department, section and title
        elif selected_department != '0' and selected_section != '0' and selected_title != '0' and selected_course == '0':
            expired_department = expired_info.filter(department_id=selected_department)
            expired_section = expired_department.filter(section_id=selected_section)
            expired_list = expired_section.filter(job_title_id=selected_title)
            paginator = Paginator(expired_list, 25)
            page = request.GET.get('page')
            expired = paginator.get_page(page)
            context = {
                    'expired': expired,
                    'course':course,
                    'department': department,
                    'job_title':job_title,
                    "section":section,
                }
            return render(request, 'expired.html', context) # template  department_section_title.html

            # filter by department, section , title & course
        elif selected_department != '0' and selected_section != '0' and selected_title != '0' and selected_course != '0':
            expired_department = expired_info.filter(department_id=selected_department)
            expired_section = expired_department.filter(section_id=selected_section)
            expired_list = expired_section.filter(job_title_id=selected_title)
            paginator = Paginator(expired_list, 25)
            page = request.GET.get('page')
            expired = paginator.get_page(page)
            context = {
                'expired': expired,
                'course': course,
                'department': department,
                'job_title': job_title,
                "section": section,
            }
            return render(request, 'expired.html', context)
        # filter by course
        elif selected_department == '0' and selected_section == '0' and selected_title == '0' and selected_course != '0':
            print("reached 1")
            expired_list = expired_info.filter(course_id=selected_course)
            paginator = Paginator(expired_list, 25)
            page = request.GET.get('page')
            expired = paginator.get_page(page)
            context = {
                    'expired': expired,
                    'course':course,
                    'department': department,
                    'job_title':job_title,
                    "section":section,
                }
            return render(request, 'expired.html', context) #filtered_training.html

        #filter by title
        elif selected_department == '0' and selected_section == '0' and selected_title != '0' and selected_course == '0':
            expired_list = expired_info.filter(job_title_id=selected_title)
            paginator = Paginator(expired_list, 25)
            page = request.GET.get('page')
            expired = paginator.get_page(page)
            context = {
                    'expired': expired,
                    'course':course,
                    'department': department,
                    'job_title':job_title,
                    "section":section,
                }
            return render(request, 'expired.html', context) #filtered_training.html

    else:
        #paging results
        paginator = Paginator(expired_info, 25)
        page = request.GET.get('page')
        print(page)
        expired_info = paginator.get_page(page)
        context= {
                "expired_info": expired_info,
                'course':course,
                'department': department,
                'job_title':job_title,
                "section":section,
            }
        return render(request, 'expired.html',context)

@login_required(login_url='/accounts/login/')
def employeeList(request):
    employees = Employee.objects.all()
    employeez = Employee.objects.all()
    job_title = JobTitle.objects.all()
    section = Section.objects.all()
    department = Department.objects.all()


    # filter by expired course
    selected_staff_number = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('r')
    selected_title = request.GET.get('s')

    if selected_title  or selected_department or selected_staff_number or selected_section:

        #filter by department
        if int(selected_department)>0 and int(selected_title)==0 and int(selected_section)==0:
            filtered_employees_list = employees.filter(department_id=selected_department)
            paginator = Paginator(filtered_employees_list, 25)
            page = request.GET.get('page')
            filtered_employees = paginator.get_page(page)
            context = {
                 'filtered_employees': filtered_employees,
                'section':section,
                'job_title':job_title,
                 'department': department,
             }
            return render(request, 'filtered_employee_list.html', context) #filtered_course_department.html

        #filter by Section
        elif int(selected_section)>0 and int(selected_title) == 0 and int(selected_department)==0:
            filtered_employees_list = employees.filter(section_id=selected_section)
            paginator = Paginator(filtered_employees_list, 25)
            page = request.GET.get('page')
            filtered_employees = paginator.get_page(page)
            context = {
                 'filtered_employees': filtered_employees,
                'section':section,
                'job_title':job_title,
                 'department': department,
             }
            return render(request, 'filtered_employee_list.html', context)

        #filter by job title
        elif int(selected_title) > 0 and int(selected_department)==0 and int(selected_section)==0:
            filtered_employees_list = employees.filter(job_title_id=selected_title)
            paginator = Paginator(filtered_employees_list, 25)
            page = request.GET.get('page')
            filtered_employees = paginator.get_page(page)
            print(filtered_employees)
            context = {
                'filtered_employees': filtered_employees,
                'section': section,
                'job_title': job_title,
                'department': department,
            }
            return render(request, 'filtered_employee_list.html', context)


            # filter by department and section
        elif int(selected_title) == 0 and int(selected_department) > 0 and int(selected_section) > 0:
            filtered_department = employees.filter(department_id=selected_department)
            filtered_employees_list = filtered_department.filter(section_id=selected_section)
            paginator = Paginator(filtered_employees_list, 25)
            page = request.GET.get('page')
            filtered_employees = paginator.get_page(page)
            context = {
                    'filtered_employees': filtered_employees,
                    'department': department,
                    'section': section,
                    'job_title': job_title,
                }
            return render(request, 'filtered_employee_list.html', context)  # filtered_course_department.html

        # #filter  Department, Section and Title
        elif int(selected_department)>0 and int(selected_section)>0 and int(selected_title)>0:
            department = employees.filter(department_id=selected_department)
            sectionf = department.filter(section_id=selected_section)
            filtered_employees_list = sectionf.filter(job_title_id=selected_title)
            paginator = Paginator(filtered_employees_list, 25)
            page = request.GET.get('page')
            filtered_employees = paginator.get_page(page)
            context = {
                'filtered_employees': filtered_employees,
                'department': department,
                'section': section,
                'job_title': job_title,
            }
            return render(request, 'filtered_employee_list.html', context) #filtered_course

        else:
            paginator = Paginator(employeez, 25)
            page = request.GET.get('page')
            employees = paginator.get_page(page)
            context = {
                'employees':employees,
                'job_title':job_title,
                'section':section,
                'department':department
            }
            return render(request,"filtered_employee_list.html", context)

    else:
        print("here")
        employees = Employee.objects.all()
        print(employees)
        context = {
            'employees': employees,
            'job_title': job_title,
            'section': section,
            'department': department
        }
        return render(request, "filtered_employee_list.html", context)

@login_required(login_url='/accounts/login/')
def trainingList(request):
    trainingRecords_list = TrainingRecord.objects.all()
    course = Course.objects.all()
    job_title = JobTitle.objects.all()
    section = Section.objects.all()
    department = Department.objects.all()

    selected_course = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('r')
    selected_title = request.GET.get('s')


    if selected_course or selected_department or selected_section or selected_title:
        #filter by department
        if selected_course=='0' and selected_department!= '0' and selected_section=='0' and int(selected_title)=='0':
            filtered_training_list = trainingRecords_list.filter(department_id=selected_department)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                     'filtered_training': filtered_training,
                     'department': department
                }
            return render(request, 'filtered_training.html', context) #filtered_course_department.html

                # filter by department, course
        elif selected_course !='0' and selected_department != '0' and selected_section != '0' and selected_title == '0':
            filtered_deoartment = trainingRecords_list.filter(department_id=selected_department)
            filtered_training_list = filtered_deoartment.filter(course_id=selected_course)
            filtered_training_lists = filtered_training_list.filter(section_id=selected_course)
            paginator = Paginator(filtered_training_lists, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                        'filtered_training': filtered_training,
                        'department': department,
                    }
            return render(request, 'filtered_training.html', context)  # filtered_course_department.html

            # filter by department, course
        elif selected_course != '0' and selected_department != '0' and selected_section == '0' and selected_title == '0':
            filtered_deoartment = trainingRecords_list.filter(department_id=selected_department)
            filtered_training_list = filtered_deoartment.filter(course_id=selected_course)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                'filtered_training': filtered_training,
                'department': department,
            }
            return render(request, 'filtered_training.html', context)  # filtered_course_department.html

            #filter Course, Department, Section and Title
        elif selected_department !='0' and selected_section !='0' and selected_title!='0' and selected_course !='0':
                department = trainingRecords_list.filter(department_id=selected_department)
                section = department.filter(section_id=selected_section)
                title = section.filter(job_title_id=selected_title)
                filtered_training_list = title.filter(course_id=selected_course)
                paginator = Paginator(filtered_training_list, 25)
                page = request.GET.get('page')
                filtered_training = paginator.get_page(page)
                context = {
                    'filtered_training': filtered_training,
                }
                return render(request, 'filtered_training.html', context) #filtered_course
        # filter by department the section and job title
        elif selected_department != '0' and selected_section != '0' and selected_title != '0' and selected_course == '0':
            department = trainingRecords_list.filter(department_id=selected_department)
            section = department.filter(section_id=selected_section)
            filtered_training_list = section.filter(job_title_id=selected_title)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                    'filtered_training': filtered_training,
                }
            return render(request, 'filtered_training.html', context) # template  department_section_title.html

            #filter course
        elif selected_department == '0' and selected_section == '0' and selected_title == '0' and selected_course != '0':
            filtered_training_list = trainingRecords_list.filter(course_id=selected_course)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                    'filtered_training': filtered_training,
                    'department': department,
                }
            return render(request, 'filtered_training.html', context) #filtered_training.html

            # filter job title
        elif selected_department == '0' and selected_section == '0' and selected_title != '0' and selected_course == '0':
            filtered_training_list = trainingRecords_list.filter(job_title_id=selected_title)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                'filtered_training': filtered_training,
                'department': department,
            }
            return render(request, 'filtered_training.html', context)  # filtered_training.html

            # filter by section
        elif selected_department == '0' and selected_section != '0' and selected_title == '0' and selected_course == '0':
            filtered_training_list = trainingRecords_list.filter(section_id=selected_section)
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                'filtered_training': filtered_training,
                'department': department,
            }
            return render(request, 'filtered_training.html', context)  # filtered_training.html

        elif selected_department == '0' and selected_section == '0' and selected_title == '0' and selected_course == '0':
            filtered_training_list = trainingRecords_list.filter()
            paginator = Paginator(filtered_training_list, 25)
            page = request.GET.get('page')
            filtered_training = paginator.get_page(page)
            context = {
                'filtered_training': filtered_training,
                'department': department,
            }
            return render(request, 'filtered_training.html', context)  # filtered_training.html

    else:

        paginator = Paginator(trainingRecords_list, 25)
        page = request.GET.get('page')
        trainingRecords = paginator.get_page(page)

        context = {
            'trainingRecords': trainingRecords,
            'course':course,
            'job_title':job_title,
            'section':section,
            'department':department,
            }
        return render(request, "trainingList.html", context)

@login_required(login_url='/accounts/login/')
def dashboard(request):
    expired_employees = TrainingRecord.objects.filter(training_expiry__lt=date.today()).count()
    number_expired_courses = TrainingRecord.objects.values('course__course_name').annotate(no_courses=Count('course'))

    course = Course.objects.all()

    for corse in course:
        trained = TrainingRecord.objects.filter(course= corse)
        print(corse)
        notTrained = Employee.objects.exclude(id__in=trained)
        nTrained=(str(notTrained))
        # nCount = Employee.objects.all().count()
        print(nTrained)

    context={
        "expired_employees":expired_employees,
        'number_expired_courses':number_expired_courses,
        'nTrained':nTrained,
        'course': course,
    }
    return render(request, "home.html", context)

@login_required(login_url='/accounts/login/')
def untrained(request):
    courseList = Course.objects.all()
    departmentList = Department.objects.all()
    sectionList = Section.objects.all()
    job_titleList = JobTitle.objects.all()

    course = request.GET.get('p')
    department = request.GET.get('q')
    section = request.GET.get('s')



    if course != "0" and department == "0" and section=="0":
        trained = TrainingRecord.objects.filter(course_id=course)
        notTrained_list = Employee.objects.exclude(trainingrecord__in=trained)
        notTrainedCount = Employee.objects.exclude(trainingrecord__in=trained).count()
        paginator = Paginator(notTrained_list, 25)
        page = request.GET.get('page')
        notTrained = paginator.get_page(page)
        context = {
            'courseList': courseList,
            "notTrained":notTrained,
            "notTrainedCount":notTrainedCount,
            'departmentList': departmentList,
            'sectionList':sectionList,
            'job_titleList': job_titleList,
        }
        return render(request, 'untrained.html', context)

    elif department !="0" and course != "0" and section=="0":
        trained = TrainingRecord.objects.filter(course_id=course)
        notTrainedl = Employee.objects.exclude(trainingrecord__in=trained)
        notTrained_list = notTrainedl.filter(department_id=department)
        notTrainedCount = notTrainedl.filter(department_id=department).count()
        paginator = Paginator(notTrained_list, 25)
        page = request.GET.get('page')
        notTrained = paginator.get_page(page)
        context = {
            'courseList': courseList,
            "notTrained": notTrained,
            "notTrainedCount": notTrainedCount,
            'departmentList': departmentList,
            'sectionList': sectionList,
            'job_titleList': job_titleList,
        }
        return render(request, 'untrained.html', context)

    elif department != "0" and course != "0" and section!="0":
        trained = TrainingRecord.objects.filter(course_id=course)
        notTrainedl = Employee.objects.exclude(trainingrecord__in=trained)
        notTrainedd = notTrainedl.filter(department_id=department)
        notTrained_list = notTrainedd.filter(section_id=section)
        notTrainedCount = notTrainedd.filter(section_id=section).count()
        paginator = Paginator(notTrained_list, 25)
        page = request.GET.get('page')
        notTrained = paginator.get_page(page)

        context = {
            'courseList': courseList,
            "notTrained": notTrained,
            "notTrainedCount": notTrainedCount,
            'departmentList': departmentList,
            'sectionList': sectionList,
            'job_titleList': job_titleList,
        }
        return render(request, 'untrained.html', context)

    else:
        
        context = {
            'courseList': courseList,
            'departmentList':departmentList,
            'sectionList': sectionList,
            'job_titleList': job_titleList,
        }
        return render(request, 'untrained.html', context)

@login_required(login_url='/accounts/login/')
def training_history(request, staff_number):
    history = TrainingRecord.objects.filter(staff_number=staff_number)
    course = Course.objects.all()
    selected_course = request.GET.get('p')
    if selected_course != None:
        filtered_result = TrainingRecord.objects.filter(course_id=selected_course)
        context = {
            'filtered_result':filtered_result,
            'history': history,
        }
        return render(request, "filtered_result.html", context)
    else:
        context = {
            'course': course,
            'history': history,
        }
        return render(request, "training_history.html", context)

@login_required(login_url='/accounts/login/')
def certificate(request, id):
    cert = TrainingRecord.objects.get(id=id)
    context = {
        "cert": cert,
    }
    return render(request,'certificate.html', context)

@login_required(login_url='/accounts/login/')
def viewRecord(request):
    vRecord = Employee.objects.filter(staff_number=600520)
    department = Department.objects.all()
    context = {
        'vRecord':vRecord,
        'department' : department
    }
    return render(request,'viewRecord.html', context)

@login_required(login_url='/accounts/login/')
def search(request):
    queryDate = request.GET.get('td')
    queryEmployee = request.GET.get('eey')
    print(queryDate,queryEmployee)

    if queryDate != None:
        filtered_training = TrainingRecord.objects.filter(training_date=queryDate)
        context = {
            'filtered_training': filtered_training,
        }
        return render(request,'filtered_training.html',context)

    elif queryEmployee != None:
        filtered_training = TrainingRecord.objects.filter(staff_number=queryEmployee)
        context = {
            'filtered_training': filtered_training,
        }
        return render(request, 'filtered_training.html', context)
    context = {

    }
    return render(request, 'searchHazard.html', context)

#to be deleted
def validate_username(request):
    staff_number = request.GET.get('staff_number', None)
    data = {
        'is_taken': TrainingRecord.objects.filter(staff_number=staff_number).exists()
    }
    print('validating')
    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def expiredxlsx(request):
    # get date values less than the current date
    department = Department.objects.all()
    course = Course.objects.all()
    job_title = JobTitle.objects.all()
    section = Section.objects.all()
    expired_info = TrainingRecord.objects.filter(training_expiry__lt = date.today()).exclude(archive=1)


    selected_course = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('r')
    selected_title = request.GET.get('s')

    # generate pdf by course and  department
    if selected_course !='0' and selected_department!= '0' and selected_section=='0' and selected_title=='0':
        expired_course = expired_info.filter(course_id=selected_course)
        expired = expired_course.filter(department_id=selected_department)
        if expired:
           return expired_xlsx(expired)

    # generate pdf by course, section and  department
    elif selected_department != '0' and selected_section != '0' and selected_title != '0' and selected_course == '0':
        print("here")
        expired_department = expired_info.filter(department_id=selected_department)
        expired_section = expired_department.filter(section_id=selected_section)
        expired = expired_section.filter(job_title_id=selected_title)

        if expired:
            return  expired_xlsx(expired)
    # generate pdf by course
    elif selected_department == '0' and selected_section == '0' and selected_title == '0' and selected_course != '0':
        expired = expired_info.filter(course_id=selected_course)
        if expired:
            return  expired_xlsx(expired)

    #generate by department
    elif selected_department != '0' and selected_section == '0' and selected_title == '0' and selected_course == '0':
        expired = expired_info.filter(course_id=selected_course)
        if expired:
            return  expired_xlsx(expired)

    #generate pdf by job title
    elif selected_department == '0' and selected_section == '0' and selected_title != '0' and selected_course == '0':
        expired = expired_info.filter(job_title_id=selected_title)
        if expired:
            return  expired_xlsx(expired)

    context= {
            "expired_info": expired_info,
            'course':course,
            'department': department,
            'job_title':job_title,
            "section":section,
        }
    return render(request, 'expiredxlsx.html',context)

@login_required(login_url='/accounts/login/')
def trainingListxlsx(request):
    trainingRecords = TrainingRecord.objects.all()
    course = Course.objects.all()
    job_title = JobTitle.objects.all()
    section = Section.objects.all()
    department = Department.objects.all()

    selected_course = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('r')
    selected_title = request.GET.get('s')


    if selected_course or selected_department or selected_section or selected_title:
        #filter by department
        if selected_course=='0' and selected_department!= '0' and int(selected_section)=='0' and int(selected_title)=='0':
            filtered_training = trainingRecords.filter(department_id=selected_department)
            return trainingList_xlsx(filtered_training)

                # filter by department, course
        elif selected_course !='0' and selected_department != '0' and selected_section == '0' and selected_title == '0':
            filtered_deoartment = trainingRecords.filter(department_id=selected_department)
            filtered_training = filtered_deoartment.filter(course_id=selected_course)
            return trainingList_xlsx(filtered_training)

        #department, Course, section
        elif selected_course != '0' and selected_department != '0' and selected_section != '0' and selected_title == '0':
            filtered_deoartment = trainingRecords.filter(department_id=selected_department)
            filtered_course = filtered_deoartment.filter(course_id=selected_course)
            filtered_training = filtered_course.filter(course_id=selected_course)
            return trainingList_xlsx(filtered_training)

            #filter Course, Department, Section and Title
        elif selected_department !='0' and selected_section !='0' and selected_title!='0' and selected_course !='0':
            department = trainingRecords.filter(department_id=selected_department)
            section = department.filter(section_id=selected_section)
            title = section.filter(job_title_id=selected_title)
            filtered_training = title.filter(course_id=selected_course)
            return trainingList_xlsx(filtered_training)

        # filter by department the section and job title
        elif selected_department != '0' and selected_section != '0' and selected_title != '0' and selected_course == '0':
            department = trainingRecords.filter(department_id=selected_department)
            section = department.filter(section_id=selected_section)
            filtered_training = section.filter(job_title_id=selected_title)
            return trainingList_xlsx(filtered_training)

            #filter course
        elif selected_department == '0' and selected_section == '0' and selected_title == '0' and selected_course != '0':
            filtered_training = trainingRecords.filter(course_id=selected_course)
            return trainingList_xlsx(filtered_training)

            # filter job title
        elif selected_department == '0' and selected_section == '0' and selected_title != '0' and selected_course == '0':
            filtered_training = trainingRecords.filter(job_title_id=selected_title)
            return trainingList_xlsx(filtered_training)

    else:
        context = {
            'trainingRecords': trainingRecords,
            'course':course,
            'job_title':job_title,
            'section':section,
            'department':department,
            }
        return render(request, "traininglistxlsx.html", context)


@login_required(login_url='/accounts/login/')
def untrainedxlsx(request):
    trainingRecords = TrainingRecord.objects.all()
    course = Course.objects.all()
    department = Department.objects.all()
    section = Section.objects.all()
    # job_title = JobTitle.objects.all()

    selected_course = request.GET.get('p')
    selected_department = request.GET.get('q')
    selected_section = request.GET.get('s')

    if selected_course or selected_department or selected_section:

        if selected_course != "0" and selected_department == "0" and selected_section == "0":
            print('reached 1')
            trained = trainingRecords.filter(course_id=selected_course)
            notTrained_list = Employee.objects.exclude(trainingrecord__in=trained)
            return untrainedlist_xlsx(notTrained_list)


        elif selected_department != "0" and selected_department != "0" and selected_section == "0":
            trained = TrainingRecord.objects.filter(course_id=selected_course)
            notTrainedl = Employee.objects.exclude(trainingrecord__in=trained)
            notTrained_list = notTrainedl.filter(department_id=selected_department)
            return untrainedlist_xlsx(notTrained_list)


        elif selected_department != "0" and selected_department != "0" and selected_section != "0":
            trained = TrainingRecord.objects.filter(course_id=selected_course)
            notTrainedl = Employee.objects.exclude(trainingrecord__in=trained)
            notTrainedd = notTrainedl.filter(department_id=selected_department)
            notTrained_list = notTrainedd.filter(section_id=selected_section)
            return untrainedlist_xlsx(notTrained_list)

    else:

        context = {
            'course': course,
            'department': department,
            'section': section,
            # 'job_title': job_title,

        }
        return render(request, 'untrainedxlsx.html', context)




# @login_required(login_url='/accounts/login/')
# def searchpdf(request):
#     queryDate = request.GET.get('td')
#     queryEmployee = request.GET.get('eey')
#     print("hit")
#     if queryDate != None:
#         filtered_training = TrainingRecord.objects.filter(training_date=queryDate)
#         return searchPdf(filtered_training)
#
#     elif queryEmployee != None:
#         filtered_training = TrainingRecord.objects.filter(staff_number=queryEmployee)
#         return searchPdf(filtered_training)
#
#     context = {
#
#     }
#     return render(request, 'traininglistxlsx.html', context)

#to be deleted
@login_required(login_url='/accounts/login/')
def getPdf(request):

    context = {

    }
    return autoEmail()

import csv
from django.http import HttpResponse

def resources(request):
    resources = CourseResources.objects.all()
    context= {
        'resources':resources
    }
    return render(request,'resources.html',context)


