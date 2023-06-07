from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import serial.tools.list_ports
from .models import *
import time
from django.utils import timezone

# Create your views here.
def index(request):
    all_readings = SoilMeasurement.objects.all()
    number_of_readings = len(all_readings)
    return render(request,'measure/index.html',{'number_of_readings':number_of_readings})

def about(request):
    return render(request,'measure/about.html')

def measurementHistory(request):
    all_readings = SoilMeasurement.objects.all()
    print(all_readings)
    n = len(all_readings)
    params = {'number_of_readings':n, 'range':range(n),'reading':all_readings}
    return render(request,'measure/measurementHistory.html',params)

def takeReading_ajax(request):
    # myReading = {'nitrogen':10, 'potassium':20, 'phosphorous':10, 'ph':7}
    myReading = sensor_reading_from_arduino()
    time.sleep(2)
    print(myReading)
    newManualReading = SoilMeasurement(location_x = 0, location_y = 0, drilled_status = False, ph_current = myReading['current'], ph_value = myReading['ph'], nitrogen_sensor = 0, nitrogen_reading = myReading['nitrogen'], phosphorous_sensor = 0, phosphorous_reading = myReading['phosphorous'], potassium_sensor = 0, potassium_reading = myReading['potassium'], measurement_date = timezone.now())
    newManualReading.save()
    return JsonResponse(myReading)

def liveMeasurementManual(request):
    return render(request, 'measure/liveMeasurementManual.html')

def sensor_reading_from_arduino():
    ports = serial.tools.list_ports.comports() #list of all ports in use
    serialInst = serial.Serial() #Blank instance of serial object
    portList = [] #Empty list of ports
    for port in ports:
        portList.append(str(port))
        # print(str(port))
    print(portList)
    serialInst.baudrate = 9600  #Setting the baudrate
    serialInst.port = "COM5" #portList[0][:4]
    # print(serialInst.port)
    serialInst.open()
    time.sleep(5)
    command = 'reading'
    print("Sending reading command")
    serialInst.write(command.encode('utf-8'))
    time.sleep(2)
    responseList = []
    while True:#serialInst.in_waiting:  #If serial instance has data in the buffer
        response = serialInst.readline()
        response = response.decode('utf').rstrip('\t')
        responseList.append(response)
        print(responseList)
        time.sleep(3)
        if response=='Done\r\n' or response=='Moving rover\r\n' or response=='Stopping motors\r\n':
            break
    readingDict = {}
    readingDict['current'] = float(responseList[2][10:19])
    readingDict['ph'] = float(responseList[2][24:28])
    readingDict['nitrogen'] = float(responseList[3][10:13])
    readingDict['phosphorous'] = float(responseList[4][13:16])
    readingDict['potassium'] = float(responseList[5][11:14])
    print(readingDict)
    return readingDict

def read_data_from_arduino():
    ports = serial.tools.list_ports.comports() #list of all ports in use
    serialInst = serial.Serial() #Blank instance of serial object
    portList = [] #Empty list of ports
    for port in ports:
        portList.append(str(port))
        # print(str(port))
    print(portList)
    serialInst.baudrate = 9600  #Setting the baudrate
    serialInst.port = portList[0][:4]
    # print(serialInst.port)
    serialInst.open()
    while True:  #Read data continuously
        if serialInst.in_waiting:  #If serial instance has data in the buffer
            packet = serialInst.readline()  #Read bytes, in unicode, needs to be converted to string
            print(packet.decode('utf').rstrip('\n'))  #Converting to string
            command = input('Enter command for rover')
            serialInst.write(command.encode('utf-8'))
            while serialInst.in_waiting:
                response = serialInst.readline()
                response = response.decode('utf').rstrip('\n')
                print(response)

def fieldInput(request):
    return render(request,'measure/fieldInput.html')

def liveMeasurementAutonomous(request):
    if request.method=='POST':
        print(request)
        fieldLength = request.POST.get('fieldLength')
        fieldWidth = request.POST.get('fieldWidth')
        numberOfReadings = request.POST.get('numberOfReadings')
        print("Field Length: {} Field Width: {} Number Of Readings: {}".format(fieldLength, fieldWidth, numberOfReadings))
        fieldData = FieldData(fieldLength=fieldLength, fieldWidth = fieldWidth, numberOfReadings = numberOfReadings)
        fieldData.save()
    return render(request, 'measure/liveMeasurementAutonomous.html')

def manualOperations(request):
    return render(request,'measure/manualOperations.html')