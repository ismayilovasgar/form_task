from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import RegisterForm
from django.http import HttpResponseRedirect


# Create your views here.
def register__page(request):
    return render(request, "register.html")


def signup__page(request):

    # if request.method == "POST":
    #     firstname = request.POST.get("firstname")
    #     lastname = request.POST.get("lastname")
    #     job_position = request.POST.get("job_position")
    #     bussines_area = request.POST.get("bussines_area")
    #     self_description = request.POST.get("self_description")
    #     job_expectation = request.POST.get("job_expectation")
    #     programming_lang = request.POST.get("prog_lang")
    #     lang_framework = request.POST.get("framework")
    #     last_post_experience = request.POST.get("post_expe")
    #     last_company_name = request.POST.get("last_comp_name")
    #     country = request.POST.get("country")
    #     phone_code = request.POST.get("phone_code")
    #     phone_number = request.POST.get("phone")
    #     email = request.POST.get("emai;")

    #     newRegister=Register()

    # return redirect(reverse("register", kwargs={}))

    context = dict()
    url = request.META.get("HTTP_REFERER")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)

    else:
        context["form"] = RegisterForm()

    return render(request, "admin", context)
