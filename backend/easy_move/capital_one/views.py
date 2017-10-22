# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import send_email
# Create your views here.

class CapitalOneLogin(APIView):
    def get(self, request):
        # Validate the incoming input (provided through query parameters)
        serializer = CityStateSearchSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # Get the model input
        data = serializer.validated_data
        city_state = data["city_state"]
        city_state = serach_city_state(city_state)
        city = [i[0] for i in city_state]
        state = [i[1] for i in city_state]
        city_and_state = [i[2] for i in city_state]

        return Response({
            "city_state": city_and_state,
            "city": city,
            "state": state
        })

class SendEmail(APIView):
    def get(self, request):
        result = send_email.email()
        if result == True:
            return Response({
                "success": result
                }, 200)
        else:
            return Response({
                "error": result
                }, 404)