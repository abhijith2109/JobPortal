from django.urls import path
from candidate import  views


urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profile/add",views.CandidateProfileCreateView.as_view(),name="cand-addprofile"),
    path("profile/detail",views.CandidateProfileDetailView.as_view(),name="cand-viewprofile"),
    path("profile/detail/edit/<int:id>",views.CandidateProfileEditView.as_view(),name="cand-editprofile"),
    path("jobs/details/<int:id>",views.CandidateJobDetailView.as_view(),name="cand-detailjob"),
    path("applications/add/<int:id>",views.applay_now,name="apply_now"),
    path("myapplications",views.MyApplications.as_view(),name="cand-myappl"),
    path("myapplicaions/acceptedapplication",views.AcceptedApplicationListView.as_view(),name="cand-acceptedapplicaions")

]