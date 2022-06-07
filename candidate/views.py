from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView
from candidate.models import CandidateProfile
from candidate.forms import CandidateProfileForm
from employer.models import Jobs,Applications
from candidate.filters import JobFilter
# Create your views here.

class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"

    def get(self,request,*args,**kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,"cand-home.html",{"filter":filter})

    def get_context_data(self, **kwargs):  #for send an extra context
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context["jobs"]=qs
        return context



class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateProfileEditView(UpdateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-editprofile.html"
    success_url = reverse_lazy("cand-home")
    pk_url_kwarg = "id"

class CandidateProfileDetailView(TemplateView):
    template_name = "cand-viewprofile.html"


class CandidateJobDetailView(DetailView):
    template_name = "cand-detailjob.html"
    model = Jobs
    context_object_name = "job"
    pk_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context["status"]=qs
        return context


def applay_now(request,*args,**kwargs):
    job_id=kwargs.get("id")
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")

class MyApplications(ListView):
    model = Applications
    template_name = "cand-appliedjobs.html"
    context_object_name = "applied"
    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)

class AcceptedApplicationListView(ListView):
    model = Applications
    template_name = "accepted_application.html"
    context_object_name = "application"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status="accepted")

