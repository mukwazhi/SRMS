from datetime import date

from django.core.mail import send_mail
from django.db.models import Count, Sum, Case, When, Value, CharField, Q
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import RiskDetail, Officials, Documents, Station, Location
from django.contrib.auth.models import User, Group
from .forms import RiskDetailForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.http import HttpResponse

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name__in=["staff",'officer'] ).exists():
        # user is an admin
        return redirect("quickView")
    else:
        return HttpResponseRedirect('/dashboard/')

@login_required(login_url='/accounts/login/')
def report_list(request, report_no):
    risk_list = RiskDetail.objects.filter(report_no=report_no)
    print(risk_list)

    context = {
        'risk_list': risk_list,
    }
    return render(request, "riskList.html", context)

@login_required(login_url='/accounts/login/')
def riskform(request):
    riskForm = RiskDetailForm()
    if request.method == 'POST':
        form = RiskDetailForm(request.POST)
        if form.is_valid():
            riskForm = form.save(commit=False)
            riskForm.save()
            sendmail()
            return HttpResponseRedirect('/operations/assessmentList/')

    else:
        context = {'riskForm': riskForm}
        return render(request, "riskForm.html", context)

@login_required(login_url='/accounts/login/')
def assessmentList(request):
    assessmentList = RiskDetail.objects.filter(status='Pending', action_required='').exclude(archive=1)
    openHazards = RiskDetail.objects.filter(status='Open').exclude(archive=1).count()
    unevaluated = RiskDetail.objects.filter(status='Pending').exclude(archive=1).count()
    closedHazards = RiskDetail.objects.filter(status='Closed').exclude(archive=1).count()

    context = {
        'assessmentList': assessmentList,
        'openHazards': openHazards,
        'unevaluated': unevaluated,
        'closedHazards': closedHazards,
    }
    return render(request, "assessmentList.html", context)

# def group_check(user):
#     return user.groups.filter(name__in=['Officer']).exists()

@login_required(login_url='/accounts/login/')
def evaluation(request, report_no):
    if request.user.groups.filter(name__in=['Officer']).exists():
        riskdetail = RiskDetail.objects.get(report_no=report_no)
        evaluationForm = RiskDetailForm(instance=riskdetail)
        if request.method == 'POST':
            form = RiskDetailForm(request.POST, instance=riskdetail)
            if form.is_valid():
                evaluation = form.save(commit=False)
                evaluation.save()
                return HttpResponseRedirect('/operations/assessmentList/')
        else:
            context = {
                'riskdetail': riskdetail,
                'evaluationForm': evaluationForm
            }
            return render(request, "evaluation.html", context)
    else:
        return HttpResponse("You can not evaluate")

@login_required(login_url='/accounts/login/')
def quickView(request):
    openHazards = RiskDetail.objects.filter(status='Open').exclude(archive=1).count()
    unevaluated = RiskDetail.objects.filter(status='Pending').exclude(archive=1).count()
    closedHazards = RiskDetail.objects.filter(status='Closed').exclude(archive=1).count()

    docCount = Documents.objects.filter(document_type='Manual').count()
    checklistCount = Documents.objects.filter(document_type='Checklist').count()
    formCount = Documents.objects.filter(document_type='Form').count()
    bulletinCount = Documents.objects.filter(document_type='Bulletin').count()

    context = {
        'openHazards': openHazards,
        'unevaluated': unevaluated,
        'closedHazards': closedHazards,
        'docCount':docCount,
        'checklistCount': checklistCount,
        'formCount': formCount,
        'bulletinCount': bulletinCount
    }

    return render(request, "quickView.html", context)

@login_required(login_url='/accounts/login/')
def openhazards(request):
    openClosedHazards = RiskDetail.objects.filter(status='Open').annotate(due=Case(When(due_date__lte=date.today(), then=Value('OD')),
                                                     When(due_date__gt=date.today(), then=Value('OK')),
                                                     output_field=CharField())).exclude(archive=1)
    for o in openClosedHazards:
        print(o.due)
    openHazards = RiskDetail.objects.filter(status='Open').exclude(archive=1).count()
    unevaluated = RiskDetail.objects.filter(action_required='').exclude(archive=1).count()
    closedHazards = RiskDetail.objects.filter(status='Closed').exclude(archive=1).count()
    context = {
        # 'dueStatus':dueStatus,
        'openClosedHazards': openClosedHazards,
        'openHazards': openHazards,
        'unevaluated': unevaluated,
        'closedHazards': closedHazards,
    }
    return render(request, "openclosedhazards.html", context)

@login_required(login_url='/accounts/login/')
def closedhazards(request):
    openHazards = RiskDetail.objects.filter(status='Open').exclude(archive=1).count()
    unevaluated = RiskDetail.objects.filter(action_required='').exclude(archive=1).count()
    closedHazards = RiskDetail.objects.filter(status='Closed').exclude(archive=1).count()
    openClosedHazards = RiskDetail.objects.filter(status='Closed').exclude(archive=1)
    context = {
        'openClosedHazards': openClosedHazards,
        'openHazards': openHazards,
        'unevaluated': unevaluated,
        'closedHazards': closedHazards,
    }
    return render(request, "openclosedhazards.html", context)

@login_required(login_url='/accounts/login/')
def detailedView(request, report_no):
    detailed_report = RiskDetail.objects.filter(report_no=report_no)
    print(detailed_report)
    context = {
        "detailed_report": detailed_report
    }
    return render(request, "detailed_report.html", context)

@login_required(login_url='/accounts/login/')
def dashboard(request):
    # hazard distribution by hazard type
    hazardType = RiskDetail.objects.values('hazard_type').annotate(hazards=Count('hazard_type')).order_by('hazard_type')\
        .exclude(archive=1)
    #  Hazard distributio by category
    hazardCategory = RiskDetail.objects.values('hazard_category').annotate(hazards=Count('hazard_category')).order_by(
        'hazard_category').exclude(archive=1)
    # hazard distribution by station
    stationHazard = RiskDetail.objects.values('station').annotate(stationCount=Count('station')).order_by(
        'station').exclude(archive=1)
    # periodic hazard distribution
    monthly = RiskDetail.objects.filter(date_of_incident__year=2019).annotate(
        month=ExtractMonth('date_of_incident')).values('month').annotate(monthCount=Count('station')).exclude(archive=1)
    # hazard closure reports
    statusProgress = RiskDetail.objects.values('status').annotate(statusCheck=Count('status'))\
        .exclude(archive=1).order_by('status').exclude(archive=1)

    stationDash = Station.objects.filter()
    for s in monthly:
        print(s['month'],s['monthCount'])

    context = {
        'stationDash':stationDash,
        'monthly': monthly,
        'statusProgress':statusProgress,
        "hazardType": hazardType,
        "hazardCategory": hazardCategory,
        "stationHazard":stationHazard,
    }
    return render(request, "dashboard.html", context)

@login_required(login_url='/accounts/login/')
def stationReport(request, station_id):
    # hazard distribution by hazard type
    hazardType = RiskDetail.objects.filter(station_id=station_id).values('hazard_type')\
        .annotate(hazards=Count('hazard_type')).order_by('hazard_type').exclude(archive=1)
    #  Hazard distributio by category
    hazardCategory = RiskDetail.objects.filter(station_id=station_id).values('hazard_category').annotate(hazards=Count('hazard_category')).order_by(
        'hazard_category').exclude(archive=1)
    # # hazard distribution by station
    # stationHazard = RiskDetail.objects.values('station').annotate(stationCount=Count('station')).order_by(
    #     'station')
    # periodic hazard distribution
    monthly = RiskDetail.objects.filter(station_id=station_id).filter(date_of_incident__year=2019).annotate(
        month=ExtractMonth('date_of_incident')).values('month').annotate(monthCount=Count('station')).exclude(archive=1)
    # hazard closure reports
    statusProgress = RiskDetail.objects.filter(station_id=station_id).values('status').annotate(statusCheck=Count('status')).order_by('status').exclude(archive=1)
    stationDash = Station.objects.filter(id=station_id)
    stationOther = Station.objects.filter().exclude(id=station_id)


    context = {
        'stationOther':stationOther,
        'stationDash': stationDash,
        'monthly': monthly,
        'statusProgress': statusProgress,
        "hazardType": hazardType,
        "hazardCategory": hazardCategory,
        # "stationHazard": stationHazard,
    }
    return render(request, "stationDashboard.html", context)

@login_required(login_url='/accounts/login/')
def searchHazard(request):
   station = Station.objects.filter()
   location = Location.objects.filter()
   search = RiskDetail.objects.filter()
   results =  RiskDetail.objects.filter().annotate(due=Case(When(due_date__lte=date.today(), then=Value('OD')),
                                                     When(due_date__gt=date.today(), then=Value('OK')),
                                                     output_field=CharField())).exclude(archive=1)
   # filter by expired course
   selected_type = request.GET.get('p')
   selected_category = request.GET.get('q')
   selected_station = request.GET.get('r')
   selected_location = request.GET.get('s')

   if selected_type or selected_category or selected_station or selected_location:
        # filter by Statation and location
        if selected_station != '0' and selected_location != '0' and selected_type == ' ' and selected_category == ' ':
           filter_results = results.filter(Q(station_id=selected_station) & Q(location_of_incident=selected_location))
           context = {
               'filter_results': filter_results,
               # 'results': results,
               'search': search,
               'station': station,
               'location': location,
           }
           return render(request, 'searchHazard.html', context)

        # filter by type of hazard
        elif selected_station == '0' and selected_location == '0' and selected_type != ' ' and selected_category == ' ':
           filter_results = results.filter(hazard_type=selected_type)
           context = {
               'filter_results': filter_results,
               # 'results': results,
               'search': search,
               'station': station,
               'location': location,
           }
           return render(request, 'searchHazard.html', context)

        # Filter by hazard type and hazard category
        elif selected_station == '0' and selected_location == '0' and selected_type != ' ' and selected_category != ' ':
            filter_results = results.filter(Q(hazard_type=selected_type) & Q(hazard_category=selected_category))
            context = {
                'filter_results': filter_results,
                # 'results': results,
                'search': search,
                'station': station,
                'location': location,
            }
            return render(request, 'searchHazard.html', context)

        #filter by hazard location, type and category
        elif selected_station == '0' and selected_location != '0' and selected_type != ' ' and selected_category != ' ':
            filter_results = results.filter(Q(hazard_type=selected_type) & Q(hazard_category=selected_category)
                               & Q(location=selected_location))
            context = {
                'filter_results': filter_results,
                # 'results': results,
                'search': search,
                'station': station,
                'location': location,
            }
            return render(request, 'searchHazard.html', context)

        #filter by station location type and category
        elif selected_station != '0' and selected_location != '0' and selected_type != ' ' and selected_category != ' ':
            filter_results = results.filter(Q(station=selected_station) & Q(location_of_incident_id=selected_location) &
                               Q(hazard_type=selected_type) & Q(hazard_category=selected_category))
            context = {
                'filter_results': filter_results,
                # 'results': results,
                'search': search,
                'station': station,
                'location': location,
            }
            return render(request, 'searchHazard.html', context)
            # filter by type of Station
        elif selected_station != '0' and selected_location == '0' and selected_type == ' ' and selected_category == ' ':
            filter_results = results.filter(station=selected_station)
            context = {
                'filter_results': filter_results,
                # 'results': results,
                'search': search,
                'station': station,
                'location': location,
            }
            return render(request, 'searchHazard.html', context)
        else:
            context = {
                'search': search,
                'station': station,
                'location': location,
            }
            return render(request, 'searchHazard.html', context)

   else:
       context = {
            'search': search,
           'station':station,
           'location': location,
        }
       return render(request, "searchHazard.html", context)

@login_required(login_url='/accounts/login/')
def downloads(request):
    manual_uploads = Documents.objects.filter(document_type='Manual')
    form_uploads = Documents.objects.filter(document_type='Form')
    checklist_uploads = Documents.objects.filter(document_type='Checklist')
    bulletin_uploads = Documents.objects.filter(document_type='Bulletin')
    context = {
       'manual_uploads' : manual_uploads,
        'form_uploads': form_uploads,
        'checklist_uploads': checklist_uploads,
        'bulletin_uploads': bulletin_uploads,

    }
    return render(request, "documents.html", context)

def sendmail():
    print(" sender email processing ")
    send_mail('Hazard Report ',
              'A Hazard has been registered in the in the system. '
              'Please logon http://127.0.0.1:8000/operations/quickView to view this Report',
              'tipsoff@nhszim.com', ['mukwazhi@gmail.com', 'bmukwazhi@nhszim.com'])
    print(" email send ")


