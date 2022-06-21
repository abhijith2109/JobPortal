from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.models import EmployerProfile,Jobs,Applications
from employer.forms import EmployerProfileForm,JobForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"



class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class EmployeeProfileEditView(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-editprofile.html"
    success_url = reverse_lazy("emp-home")
    pk_url_kwarg = "id"

class EmployerProfileDetailView(TemplateView):
    template_name = "emp-viewprofile.html"


class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,"Job has been posted successfully")
        return super().form_valid(form)


class EmployerJobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"
    def form_valid(self, form):
        messages.success(self.request,"Job has been Updated")
        return super().form_valid(form)




class EmployerJobListView(ListView):
    model = Jobs
    context_object_name ="jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")

class EmployerJobDetailView(DetailView):
    model = Jobs
    template_name ="emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

    # def get_queryset(self):
    #     return Jobs.objects.filter(posted_by=self.request.user)


class ViewApplications(ListView):
    model = Applications
    template_name = "emp-allapplications.html"
    context_object_name = "all_appl"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"),status="applied")

class EmployerAcceptedApplicationsView(ListView):
    model = Applications
    template_name = "emp-acceptedapplications.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"))

class ApplicantProfileDetailView(DetailView):
    model = Applications
    template_name = "emp-applicantprofile.html"
    pk_url_kwarg = "id"
    context_object_name = "appl"


def update_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    qs=Applications.objects.get(id=app_id)
    qs.status="rejected"
    qs.save()
    return redirect("emp-home")

def accept_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    qs=Applications.objects.get(id=app_id)
    qs.status="accepted"
    qs.save()
    send_mail(
        'Job Notification',
        'Your Resume accepted..',
        'abhijitb2109@gmail.com',
        ['pegasuscrtz@gmail.com'],
        fail_silently=False,
    )
    return redirect("emp-home")

