"""
URL configuration for roverproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="measureHome"),
    path("about",views.about,name="about"),
    path("measurementHistory",views.measurementHistory,name="measurementHistory"),
    path("fieldInput",views.fieldInput,name="fieldInput"),
    path("liveMeasurementAutonomous",views.liveMeasurementAutonomous,name="liveMeasurement"),
    path("liveMeasurementManual", views.liveMeasurementManual, name="liveMeasurementManual"),
    path("manualOperations",views.manualOperations,name="manualOperations"),
    path('liveReadingManual_endpoint/', views.takeReading_ajax, name='liveReadingManual_endpoint'),
    path('moveRover_endpoint/',views.moveRover,name="moveRoverManual"),
    path('stopMotors_endpoint/',views.stopMotors,name="stopMotorsManual"),
    path('drill_endpoint/',views.drill_endpoint,name="drillManual")
]
