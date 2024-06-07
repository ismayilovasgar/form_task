from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
import pdfkit


# Create your views here.
def register__page(request):
    return render(request, "register.html")


def signup__page(request):
    # * Muellim izah etdiyi yol
    # if request.method == "POST":
    #     firstname = request.POST.get("firstname")
    #     lastname = request.POST.get("lastname")
    #     job_position = request.POST.get("job_position")
    #     bussines_area = request.POST.get("bussines_area")
    #     self_description = request.POST.get("self_description")
    #     job_expectation = request.POST.get("job_expectation")
    #     programming_lang = request.POST.get("programming_lang")
    #     last_framework = request.POST.get("last_framework")
    #     last_post_experience = request.POST.get("last_post_experience")
    #     last_comp_name = request.POST.get("last_comp_name")
    #     country = request.POST.get("country")
    #     phone_code = request.POST.get("phone_code")
    #     phone_number = request.POST.get("phone_number")
    #     email = request.POST.get("email")

    #     newRegister = Register(
    #         firstname=firstname,
    #         lastname=lastname,
    #         job_position=job_position,
    #         bussines_area=bussines_area,
    #         self_description=self_description,
    #         job_expectation=job_expectation,
    #         programming_lang=programming_lang,
    #         last_framework=last_framework,
    #         last_post_experience=last_post_experience,
    #         last_comp_name=last_comp_name,
    #         country=country,
    #         phone_code=phone_code,
    #         phone_number=phone_number,
    #         email=email,
    #     )
    #     newRegister.save()
    #     messages.success(request, "Successfully Add Your Information")
    # return redirect(reverse("register", kwargs={}))

    # * Internetden Baxdim
    context = dict()
    url = request.META.get("HTTP_REFERER")
    print(url)

    if request.method == "POST":
        form = ProfilesForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)

    else:
        context["form"] = ProfilesForm()

    return render(request, "admin", context)


config = pdfkit.configuration(
    wkhtmltopdf=r"C:/Program Files/wkhtmltox/bin/wkhtmltopdf.exe"
)


def home(request):
    return render(request, "resume.html")


def generatePDF(request, id):
    pdf = pdfkit.from_url(
        request.build_absolute_uri(reverse("home")),
        False,
        configuration=config,
    )
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="file_name.pdf"'
    return response


def download__page(request):
    registers = Register.objects.all()
    context = {"users": registers}
    return render(request, "download.html", context)
