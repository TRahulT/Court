from django.urls import path
from .views import (client_list_create,rules_by_sid,rules,respondent,respondent_by_sid,case_details_by_sid,super_login,next_hearing_by_sid,advocate_list_create,AdvocateLoginView,case_type_create,add_case,next_listing,homepage_today_case,InterimOrderList,CaseFiles,CaseFileGet)

urlpatterns = [
    path('client_add/', client_list_create, name="client_get_post"),
    path('advocate_add/', advocate_list_create, name="advocate_get_post"),
    path('rules_add/', rules, name="rules"),
    path('respondent_add/', respondent, name="respondent"),
    path('case-type/',case_type_create,name="add new case type"),
    path('new-case/',add_case,name="new case"),
    path('next-listing/',next_listing,name="next-listing"),
    path('home/<str:date>/',homepage_today_case,name="home-page"),
    path('copy-of-order/<int:key>/', InterimOrderList.as_view(), name='COO'),
    path('post-casefiles/<int:key>/',CaseFiles.as_view(),name="case-File-post"),
    path('get-casefile/<int:pk>/', CaseFileGet, name='case-file'),
    path('advocate-login/', AdvocateLoginView.as_view(), name='advocate-login'),
    path('superuser/login/', super_login, name="superuser"),
    path("next_hearing_by_sid/",next_hearing_by_sid,name='next-by'),
    path("respondent_by_sid/",respondent_by_sid,name='res-by'),
    path("rules_by_sid/", rules_by_sid, name='rules-by'),
    path("case_details_by_sid/", case_details_by_sid, name='next')

]
