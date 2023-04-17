from django.shortcuts import render
from django.http import FileResponse
from fpdf import FPDF
from api.models import *


def report_generator():

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font('courier', 'B', 18)

    pdf.cell(40, 10, 'ntwaalako Organisation Report ', 0, 1)
    pdf.cell(40, 10, '', 0, 1)

    pdf.set_font('courier', 'B', 14)

    pdf.cell(40, 10, 'These are all the Approved trips of this month ', 0, 1)
    pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Destination'.ljust(10)} {'Pick_up_location'.rjust(10)} {'Passenger'.ljust(10)}{'Date'.rjust(10)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)

    queryset = PassengerTrip.objects.all()

    for line in queryset:
        if(line.trip.status == 'Approved'):
            st = str(line.trip.date)
            pdf.cell(200, 8, f"{line.trip.destination.ljust(10)} {line.trip.pick_up_location.rjust(7)}{line.passenger.user.username.rjust(18)}{st.split(' ', 1)[0].rjust(18)}", 0, 1)

    pdf.cell(40, 10, '', 0, 1)

    pdf.set_font('courier', 'B', 14)
    pdf.cell(40, 10, 'These are all the Pending trips of this month ', 0, 1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Destination'.ljust(10)} {'Pick_up_location'.rjust(10)} {'Passenger'.ljust(10)}{'Date'.rjust(10)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)

    for line in queryset:
        if(line.trip.status == 'Pending'):
            st = str(line.trip.date)
            pdf.cell(200, 8, f"{line.trip.destination.ljust(10)} {line.trip.pick_up_location.rjust(7)}{line.passenger.user.username.rjust(18)}{st.split(' ', 1)[0].rjust(18)}", 0, 1)

    report = pdf.output('report.pdf', 'F')
    return report
