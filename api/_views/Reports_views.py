
from rest_framework.response import Response
from rest_framework import status, generics
from api._serializers.reports_serializers import ReportSerializer
from django.http import HttpResponse
from core.utilities.rest_exceptions import (ValidationError)
from django.shortcuts import render
from django.http import FileResponse
from business_logic.utilities.pdf_generator import report_generator


class ReportsView(generics.GenericAPIView):
    serializer_class = ReportSerializer

    def post(self, request, format=None):
        # print(request.data)
        report = report_generator()
        # return Response('res', status=status.HTTP_201_CREATED)
        return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
