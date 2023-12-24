from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .models import Client, CaseType, AddCase,Rules, RespondentAdvocate,NextListening, InterimOrder, CaseFile, AdvocateProfile
from .serializers import ClientSerializer, CaseSerializer, AddCaseSerializer, NextListingSerializer, \
    InterimOrderSerializer,RespondentSerializer, RuleSerializer,CaseFileSerializer, AdvocateProfileSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def client_list_create(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        if user_id is not None:
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def advocate_list_create(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            clients = AdvocateProfile.objects.all()
            serializer = AdvocateProfileSerializer(clients, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        if user_id is not None:
            serializer = AdvocateProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def case_type_create(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            case = CaseType.objects.all()
            serializer = CaseSerializer(case, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        if user_id is not None:
            serialized_obj = CaseSerializer(data=request.data)
            if serialized_obj.is_valid():
                serialized_obj.save()
                return Response(serialized_obj.data, status=201)
            return Response(serialized_obj.errors, status=400)
@csrf_exempt
@api_view(['GET', 'POST'])
def rules(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            clients = Rules.objects.all()
            serializer = RuleSerializer(clients, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        if user_id is not None:
            serializer = RuleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def respondent(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            clients = RespondentAdvocate.objects.all()
            serializer = RespondentSerializer(clients, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        if user_id is not None:
            serializer = RespondentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
@csrf_exempt
@api_view(['GET', 'POST'])
def add_case(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            add_obj = AddCase.objects.all()
            serializer = []
            for i in add_obj:
                serializer.append({
                    'id': i.id,
                    'client_details': i.client_details.name,
                    'case_type': i.case_type.name,
                    'filling_number': i.filling_number,
                    'filling_date': i.filling_date,
                    'registration_number': i.registration_number,
                    # 'registration_date': registration_date,
                    'cnr_number': i.cnr_number,
                    'first_hearing': i.first_hearing,
                    'case_stage': i.case_stage,
                    'court_no': i.court_no,
                    'petitioner': i.petitioner,
                    'advocate_name': i.advocate_name,
                    'police_station': i.police_station,
                    'fir_number': i.fir_number,
                    'fir_year': i.fir_year,
                    'fir_date': i.fir_date,
                })
            return Response(serializer, status=200)
    elif request.method == "POST":
        if user_id is not None:
            serializer = AddCaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def next_listing(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            add_obj = NextListening.objects.all()
            serializer = NextListingSerializer(add_obj, many=True)
            return Response(serializer.data, status=200)
    elif request.method == "POST":
        if user_id is not None:
            serializer = NextListingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def homepage_today_case(request, date):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            add = NextListening.objects.filter(next_hearing_date=date)
            serializer = []
            for i in add:
                date = i.case_detail.first_hearing
                serializer.append({
                    "id": i.id,
                    "Client": {
                        "id": i.case_detail.id,
                        "CNR_no": i.case_detail.cnr_number,
                        "case_type": i.case_detail.case_type.name,
                        "first_hearing": date,
                        "client_name": i.case_detail.client_details.name,
                        "client_ph_no": i.case_detail.client_details.phone_number,

                    },
                    "case_stage": i.case_stage,
                    "court_no_judge": i.court_no_judge
                })
            return Response(serializer)


class InterimOrderList(APIView):

    def post(self, request, key):
        user_id = getattr(request, 'user_id', None)
        next_hearing_details_id = key
        print(next_hearing_details_id)
        try:
            opd1_patient_document = NextListening.objects.get(id=next_hearing_details_id)
            print(opd1_patient_document)
        except NextListening.DoesNotExist:
            return Response({'message': 'Invalid next_hearing_details ID'}, status=status.HTTP_404_NOT_FOUND)
        print(opd1_patient_document.id)
        existing_order = InterimOrder.objects.filter(next_hearing_details=opd1_patient_document.id).first()

        if existing_order:
            # An InterimOrder for this next_hearing_details already exists, handle it as needed
            return Response({'message': 'InterimOrder already exists', "exist": False}, status=status.HTTP_200_OK)
        data = request.data.copy()
        data['next_hearing_details'] = opd1_patient_document.id

        order_details = request.data.get('order_details')
        data['order_details'] = order_details
        print(data)
        serializer = InterimOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uploaded'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseFiles(APIView):
    def post(self, request, key):
        user_id = getattr(request, 'user_id', None)
        try:
            case_obj = AddCase.objects.get(id=key)
        except AddCase.DoesNotExist:
            return Response({'message': 'Invalid sarvhit ID',"is_valid":False}, status=status.HTTP_404_NOT_FOUND)
        print(case_obj.id)
        data = request.data.copy()
        data['case'] = case_obj.id

        file = request.data.get('file')
        data['file'] = file
        print(data)
        serializer = CaseFileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uploaded'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'DELETE'])
def CaseFileGet(request, pk):
    user_id = getattr(request, 'user_id', None)
    documents = CaseFile.objects.filter(case_id=pk)
    if request.method == 'GET':
        if user_id is not None:
            serializer = CaseFileSerializer(documents, many=True)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        if user_id is not None:
            documents.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AdvocateLoginView(APIView):
    def post(self, request, format=None):
        serializer = AdvocateProfileSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        # name=serializer.validated_data['first_name']
        Password = serializer.validated_data['password']

        try:
            user = AdvocateProfile.objects.get(phone_number=phone_number)

            if Password == user.password:
                request.session['id'] = user.id

                expiration_time = datetime.utcnow() + timedelta(hours=24)
                payload = {
                    'user_id': user.id,
                    'exp': expiration_time.timestamp()
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

                response = Response({'token': token, 'message': 'Operator logged in successfully.', 'is_log': True,
                                     'username': phone_number}, status=status.HTTP_200_OK)
                response.set_cookie('my_jwt_cookie', token, httponly=True, secure=True, samesite="None")
                return response
            else:
                return Response({'detail': 'Invalid number or password.', 'is_loged': False},
                                status=status.HTTP_201_CREATED)

        except AdvocateProfile.DoesNotExist:
            return Response({'detail': 'does  not exist .', 'is_loged': False}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def super_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(username=username, password=password)

    if user is not None and user.is_active:
        if user.is_superuser:
            # Superuser login
            expiration_time = datetime.utcnow() + timedelta(hours=24)
            payload = {
                'user_id': user.id,
                'exp': expiration_time.timestamp()
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            login(request, user)
            response = Response({'token': token, 'message': 'Superuser logged in successfully.'},
                                status=status.HTTP_200_OK)
            response.set_cookie('my_jwt_cookie', token, max_age=3600, httponly=True, secure=True, samesite="None")
            return response


# @api_view(['POST'])
# def next_hearing_by_sid(request):
#     if request.method == "POST":
#         sid = request.data.get('sid')  # Get 'sid' from POST data
#         if sid is not None:
#             add_case = AddCase.objects.get(sarvhit_number=sid)
#             sid_obj = InterimOrder.objects.filter(next_hearing_details__case_detail=add_case)
#             serializer = []
#
#             for i in sid_obj:
#                 file_url = i.order_details.url
#                 serializer.append({
#                     "id":i.id,
#                     "order_details": file_url,
#                     # "client_name": i.next_hearing_details.case_detail.client_details.name,
#                     # "client_fh_name": i.next_hearing_details.case_detail.client_details.fh_name,
#                     "hearing_date":i.next_hearing_details.next_hearing_date,
#                     "case_stage":i.next_hearing_details.case_stage,
#                     "court_no_judge":i.next_hearing_details.court_no_judge,
#                     # "case_type":i.next_hearing_details.case_detail.case_type.name,
#                     # "filling_number": i.next_hearing_details.case_detail.filling_number,
#                     # "registration_number": i.next_hearing_details.case_detail.registration_number,
#                     # "filling_date": i.next_hearing_details.case_detail.filling_date,
#                     # "first_hearing": i.next_hearing_details.case_detail.first_hearing,
#                     # "cnr_number": i.next_hearing_details.case_detail.cnr_number,
#                     # "petitioner": i.next_hearing_details.case_detail.petitioner,
#                     # "advocate_name": i.next_hearing_details.case_detail.advocate_name,
#                     # "police_station": i.next_hearing_details.case_detail.police_station,
#                     # "fir_number": i.next_hearing_details.case_detail.fir_number,
#                     # "fir_year": i.next_hearing_details.case_detail.fir_year,
#
#                 })
#                 print(serializer)
#             return Response(serializer)
#         else:
#             return Response({"error": "Missing 'sid' in POST data"})
#

@api_view(['POST'])
def next_hearing_by_sid(request):
    if request.method == "POST":
        sid = request.data.get('sid')  # Get 'sid' from POST data

        if sid is not None:
            try:
                add_case = AddCase.objects.get(sarvhit_number=sid)
                sid_obj = InterimOrder.objects.filter(next_hearing_details__case_detail=add_case)
                serializer = []

                for i in sid_obj:
                    file_url = i.order_details.url
                    serializer.append({
                        "id": i.id,
                        "order_details": file_url,
                        "hearing_date": i.next_hearing_details.next_hearing_date,
                        "case_stage": i.next_hearing_details.case_stage,
                        "court_no_judge": i.next_hearing_details.court_no_judge,
                    })

                return Response({"data_value": serializer, "is_valid": True}, status=status.HTTP_200_OK)
            except AddCase.DoesNotExist: 
                return Response({"error": "The provided 'sid' does not exist.","is_valid":False}, status=status.HTTP_200_OK)
        else:
            # Handle the case when 'sid' is not provided in the POST data
            return Response({"error": "Please provide a valid 'sid' in the POST data.","is_valid":False})




@api_view(['POST'])
def rules_by_sid(request):
    if request.method == "POST":
        sid = request.data.get('sid')  # Get 'sid' from POST data

        if sid is not None:
            try:
                add_case = AddCase.objects.get(sarvhit_number=sid)
                sid_obj = Rules.objects.filter(case=add_case)
                serializer = []

                for i in sid_obj:
                    serializer.append({
                        "id": i.id,
                        "under_act":i.under_act,
                        "under_section":i.under_section
                    })

                return Response(serializer)
            except AddCase.DoesNotExist:
                # Handle the case when 'sid' doesn't exist
                return Response({"error": "The provided 'sid' does not exist.","is_valid":False}, status=status.HTTP_200_OK)
        else:
            # Handle the case when 'sid' is not provided in the POST data
            return Response({"error": "Please provide a valid 'sid' in the POST data.","is_valid":False})



@api_view(['POST'])
def respondent_by_sid(request):
    if request.method == "POST":
        sid = request.data.get('sid')  # Get 'sid' from POST data

        if sid is not None:
            try:
                add_case = AddCase.objects.get(sarvhit_number=sid)
                sid_obj = RespondentAdvocate.objects.filter(case_resp=add_case)
                serializer = []

                for i in sid_obj:
                    serializer.append({
                        "id": i.id,
                        "name":i.name,
                        "phone_number":i.phone_number,
                        "resp_advocate":i.resp_advocate,
                        "adv_no":i.adv_no
                    })

                return Response(serializer)
            except AddCase.DoesNotExist:
                # Handle the case when 'sid' doesn't exist
                return Response({"error": "The provided 'sid' does not exist.","is_valid":False}, status=status.HTTP_200_OK)
        else:
            # Handle the case when 'sid' is not provided in the POST data
            return Response({"error": "Please provide a valid 'sid' in the POST data.","is_valid":False})

@api_view(['POST'])
def case_details_by_sid(request):
    if request.method == "POST":
        sid = request.data.get('sid')  # Get 'sid' from POST data

        if sid is not None:
            try:
                add_case = AddCase.objects.filter(sarvhit_number=sid)
                serializer = []
                for i in add_case:
                    serializer.append({
                        "client_details": {"client_id":i.client_details.id, "client_name":i.client_details.name, "client_fh_name":i.client_details.fh_name},
                        "case_type": {"case_id":i.case_type.id,"case_name":i.case_type.name},
                        "filling_number": i.filling_number,
                        "sarvhit_number": i.sarvhit_number,
                        "filling_date": i.filling_date,
                        "registration_number": i.registration_number,
                        # "registration_date": i.registration_date,
                        "cnr_number": i.cnr_number,
                        "first_hearing": i.first_hearing,
                        "case_stage": i.case_stage,
                        "court_no": i.court_no,
                        "petitioner": i.petitioner,
                        "advocate_name": i.advocate_name,
                        "police_station": i.police_station,
                        "fir_number": i.fir_number,
                        "fir_year": i.fir_year,
                        "fir_date": i.fir_date
                    })

                return Response(serializer)
            except AddCase.DoesNotExist:
                # Handle the case when 'sid' doesn't exist
                return Response({"error": "The provided 'sid' does not exist.","is_valid":False}, status=status.HTTP_200_OK)
        else:
            # Handle the case when 'sid' is not provided in the POST data
            return Response({"error": "Please provide a valid 'sid' in the POST data.","is_valid":False})
