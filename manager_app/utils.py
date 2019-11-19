# from django.http import HttpResponse, request
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
# from reportlab.platypus.tables import Table, TableStyle
# from django.contrib.auth.models import User
#
#
# cm = 2.54
#
# def generate(expired):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=somefile.pdf'
#     # PAGE_HEIGHT = int(defaultPageSize[1]); PAGE_WIDTH = int(defaultPageSize[0])
#     # print(type(PAGE_WIDTH),"--",type(PAGE_HEIGHT))
#     # styles = getSampleStyleSheet()
#     print('expired pdf 1')
#
#     # header information
#
#     def myFirstPage(canvas, doc):
#         canvas.saveState()
#         canvas.setFont('Times-Bold', 8)
#         # logo image
#         # I = Image('{% static "image/nhs-logo.png" %}')
#         # I.drawHeight = 1.25 * inch * I.drawHeight / I.drawWidth
#         # I.drawWidth = 1.25 * inch
#         # canvas.drawImage(I,100, 800)
#         canvas.drawString(200, 800, "Expired Course Report")
#         canvas.drawString(400, 800, 'User : bmukwazhi')
#         # canvas.drawString(500, 800, "23.11.2018 21:40")
#         canvas.setFont('Times-Roman', 9)
#         # canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
#         canvas.restoreState()
#
#     elements = []
#
#     doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=20 * cm, bottomMargin=0)
#
#     data=[["Employee Name",'Staff Number', "Course", "Training Date", "Training Expiry "],]
#
#     for exp in expired:
#         r =[]
#         r.append(str(exp.employee_name))
#         r.append(str(exp.staff_number))
#         r.append(str(exp.course))
#         r.append(str(exp.training_date))
#         r.append(str(exp.training_expiry))
#         data.append(r)
#
#     table = Table(data)
#     table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
#                         ('TEXTCOLOR', (3, 1), (3, -1), colors.red),
#                         ('BACKGROUND', (0, 0), (4, 0), colors.pink),
#                         ('VALIGN', (0, 0), (0, -1), 'TOP'),
#                         ('TEXTCOLOR', (0, 0), (0, -2), colors.black),
#                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),]))
#
#     elements.append(table)
#     doc.build(elements, onFirstPage=myFirstPage)
#     return response
#
# def generateTrainedPdf(filtered_training):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=somefile.pdf'
#     # PAGE_HEIGHT = int(defaultPageSize[1]); PAGE_WIDTH = int(defaultPageSize[0])
#     # print(type(PAGE_WIDTH),"--",type(PAGE_HEIGHT))
#     styles = getSampleStyleSheet()
#     print('trained pdf 1')
#     # header information
#
#     def myFirstPage(canvas, doc):
#         canvas.saveState()
#         canvas.setFont('Times-Bold', 8)
#         # logo image
#         # I = Image('{% static "image/nhs-logo.png" %}')
#         # I.drawHeight = 1.25 * inch * I.drawHeight / I.drawWidth
#         # I.drawWidth = 1.25 * inch
#         # canvas.drawImage(I,100, 800)
#         canvas.drawString(200, 800, "Trained Query Report")
#         canvas.drawString(400, 800, 'User : bmukwazhi')
#         # canvas.drawString(500, 800, "23.11.2018 21:40")
#         canvas.setFont('Times-Roman', 9)
#         # canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
#         canvas.restoreState()
#
#     elements = []
#
#     doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=20 * cm, bottomMargin=0)
#
#     data=[["Employee Name",'Staff Number', "Course", "Training Date", "Training Expiry "],]
#
#     for exp in filtered_training:
#         r =[]
#         r.append(str(exp.employee_name))
#         r.append(str(exp.staff_number))
#         r.append(str(exp.course))
#         r.append(str(exp.training_date))
#         r.append(str(exp.training_expiry))
#         data.append(r)
#
#     table = Table(data)
#     table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
#                         ('TEXTCOLOR', (3, 1), (3, -1), colors.red),
#                         ('BACKGROUND', (0, 0), (4, 0), colors.pink),
#                         ('VALIGN', (0, 0), (0, -1), 'TOP'),
#                         ('TEXTCOLOR', (0, 0), (0, -2), colors.black),
#                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),]))
#
#     elements.append(table)
#     doc.build(elements, onFirstPage=myFirstPage)
#     print('trainedpdf')
#     return response
#
# def searchPdf(filtered_training):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=somefile.pdf'
#     # PAGE_HEIGHT = int(defaultPageSize[1]); PAGE_WIDTH = int(defaultPageSize[0])
#     # print(type(PAGE_WIDTH),"--",type(PAGE_HEIGHT))
#     styles = getSampleStyleSheet()
#
#     # header information
#
#     def myFirstPage(canvas, doc):
#         canvas.saveState()
#         canvas.setFont('Times-Bold', 8)
#         # logo image
#         # I = Image('{% static "image/nhs-logo.png" %}')
#         # I.drawHeight = 1.25 * inch * I.drawHeight / I.drawWidth
#         # I.drawWidth = 1.25 * inch
#         # canvas.drawImage(I,100, 800)
#         canvas.drawString(200, 800, "Training Report")
#         canvas.drawString(400, 800, 'User : bmukwazhi')
#         # canvas.drawString(500, 800, "23.11.2018 21:40")
#         canvas.setFont('Times-Roman', 9)
#         # canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
#         canvas.restoreState()
#
#     elements = []
#
#     doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=20 * cm, bottomMargin=0)
#
#     data=[["Employee Name",'Staff Number', "Course", "Training Date", "Training Expiry "],]
#
#     for exp in filtered_training:
#         r =[]
#         r.append(str(exp.employee_name))
#         r.append(str(exp.staff_number))
#         r.append(str(exp.course))
#         r.append(str(exp.training_date))
#         r.append(str(exp.training_expiry))
#         data.append(r)
#
#     table = Table(data)
#     table.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
#                         ('TEXTCOLOR', (3, 1), (3, -1), colors.red),
#                         ('BACKGROUND', (0, 0), (4, 0), colors.pink),
#                         ('VALIGN', (0, 0), (0, -1), 'TOP'),
#                         ('TEXTCOLOR', (0, 0), (0, -2), colors.black),
#                         ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),]))
#
#     elements.append(table)
#     doc.build(elements, onFirstPage=myFirstPage)
#     return response
