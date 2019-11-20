from datetime import date

from django.db import models

def report_number():
    last_report = RiskDetail.objects.all().order_by("id").last()
    if not last_report:
        return 'FRN0001'
    report_no = last_report.report_no
    report_int = int(report_no.split('FRN')[-1])
    width = 4
    new_report_int = report_int + 1
    formatted = (width - len(str(new_report_int))) * '0' + str(new_report_int)
    new_report_no = 'FRN' + str(formatted)
    return new_report_no

class RiskDetail(models.Model):
    report_no = models.CharField(max_length=500, default=report_number, null=True, blank=True)
    station = models.ForeignKey('Station', max_length=100, null=True,blank=True, on_delete=models.DO_NOTHING)
    location_of_incident = models.ForeignKey('Location', on_delete=models.DO_NOTHING, null=True, blank=True)
    date_of_incident = models.DateField(null=True, blank=True, verbose_name="Date")
    time_of_incident = models.TimeField(null=True, blank=True)
    HAZARDTYPE = (
        ('Aircraft Related','Aircraft Related'),
        ('Non Aircraft', 'Non Aircraft')
    )
    hazard_type = models.CharField(max_length=100, choices=HAZARDTYPE,null=True,blank=True)
    HAZARDCAT = (
        ('Aircraft hazard','Aircraft hazard'),
        ('Personal Injury', 'Personal Injury'),
        ('Equipment hazard', 'Equipment hazard'),
        ('Environmental hazard', 'Environmental hazard'),
        ('personal & equipment hazard', 'Personal & equipment hazard')
    )
    hazard_category = models.CharField(max_length=100, choices=HAZARDCAT, null=True,blank=True)
    incident_detail = models.TextField(max_length=3000, null=True,blank=True, verbose_name="Hazard Details")
    Rating_CHOICES = (
        (1, 'Extremely Improbable'),
        (2, 'Improbable'),
        (3, 'Remote'),
        (4, 'Occasional'),
        (5, 'Frequent')
    )
    likelyhood = models.IntegerField(choices=Rating_CHOICES, default=1, null=True,blank=True)
    Rating_Severity = (
        (1, 'No effect'),
        (2, 'Slight'),
        (3, 'Moderate'),
        (4, 'Major'),
        (5, 'Serious')
    )
    severity = models.IntegerField(choices=Rating_Severity, default=1, null=True,blank=True)
    rating = models.IntegerField(null=True, blank=True)
    proposed_mitigation = models.TextField(max_length=3000, null=True,blank=True)
    original_report = models.FileField(null=True, blank=True, upload_to="scans/")
    reporter_name = models.CharField(max_length=100, null=True,blank=True)
    #Evaluation
    action_required = models.TextField(max_length=1000, null=True, blank=True)
    resources_required = models.TextField(max_length=1000, null=True, blank=True)
    responsible_official = models.ForeignKey('Officials', on_delete=models.DO_NOTHING, related_name='responsible_official', null=True, blank=True)
    assignment = models.ForeignKey('Officials',null=True,blank=True, on_delete=models.DO_NOTHING, related_name='assignment')
    due_date = models.DateField(null=True, blank=True)
    Action_Taken = models.TextField(max_length=3000,null=True,blank=True)
    evidence_of_closure = models.FileField(null=True, blank=True, upload_to="evidence/")
    residual_likelyhood = models.IntegerField(choices=Rating_CHOICES, default=1, null=True, blank=True)
    residual_severity = models.IntegerField(choices=Rating_Severity, default=1, null=True, blank=True)
    residual_rating = models.IntegerField(null=True, blank=True)
    Status = (
        ('Pending', 'Pending'),
        ('Open', 'Open'),
        ('Closed', 'Closed')
    )
    status = models.CharField(choices=Status, default='Pending', max_length=10,null=True,blank=True)
    archive = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.rating = self.likelyhood*self.severity
        self.residual_rating = self.residual_likelyhood * self.residual_severity
        super(RiskDetail, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.report_no)

class Location(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.location)

class Station(models.Model):
    station = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.station)


class Officials(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Documents(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(null=True, blank=True, upload_to='resources/')
    valid_to = models.DateField(null=True, blank=True)
    archive = models.BooleanField(default=False)
    docType = (
        ('Manual', 'Manual'),
        ('Form', 'Form'),
        ('Checklist', 'Checklist'),
        ('Bulletin', 'Bulletin'),

    )
    document_type = models.CharField(choices=docType, max_length=50)

    def __str__(self):
        return self.title

# class Budget(models.Model):
#         MONTHS = (
#             (1, "January"),
#             (2, "February"),
#             (3, "March"),
#             (4, "April"),
#             (5, "May"),
#             (6, "June"),
#             (7, "July"),
#             (8, "August"),
#             (9, "September"),
#             (10, "October"),
#             (11, "November"),
#             (12, "December")
#         )
#         budget_year = models.IntegerField()
#         budget_month = models.IntegerField(choices=MONTHS)
#         target_incidents = models.IntegerField()


