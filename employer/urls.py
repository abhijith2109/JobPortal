from django.urls import path
from employer import views

urlpatterns=[
    path("ehome",views.EmployerHomeView.as_view(),name="emp-home"),
    path("profile/add",views.EmployerProfileCreateView.as_view(),name="emp-profile"),
    path("profile/detail",views.EmployerProfileDetailView.as_view(),name="emp-detail"),
    path("jobs/add",views.JobCreateView.as_view(),name="emp-addjob"),
    path("jobs/all",views.EmployerJobListView.as_view(),name="emp-listjob"),
    path("job/detail/<int:id>",views.EmployerJobDetailView.as_view(),name="emp-jobdetail"),
    path("job/detail/edit/<int:id>",views.EmployerJobEditView.as_view(),name="emp-jobedit"),
    path("job/viewapplications/<int:id>",views.ViewApplications.as_view(),name="emp-viewappl"),
    path("job/viewapplications/profile/<int:id>",views.ApplicantProfileDetailView.as_view(),name="emp-applicantprofile"),
    path("job/viewapplications/status/reject/<int:id>",views.update_application,name="emp-rejectapplication"),
    path("job/viewapplications/status/accept/<int:id>", views.accept_application,name="emp-acceptapplication"),
    path("job/viewapplications/status/<int:id>",views.EmployerAcceptedApplicationsView.as_view(),name="emp-applicationstatus"),

]