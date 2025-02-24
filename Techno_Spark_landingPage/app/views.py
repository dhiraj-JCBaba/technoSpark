from django.conf import settings
from django.contrib import messages
from django.contrib.sites import requests
from django.shortcuts import render, redirect
from .forms import leadForm
import requests

base_url = settings.API_PARENT_URL


def getLeadsData():
    leads = []
    api_url_for_leads = f"{base_url}/showLeads/"
    leads_response = requests.get(api_url_for_leads)
    if leads_response.status_code == 200:
        leads = leads_response.json()
    return leads


def HOME(request):
    return render(request, 'index.html')


def lead_registration(request):
    leads = getLeadsData()
    print("leads:",leads)
    if request.method == "POST":
        print("POST Method Fire.")
        form = leadForm(request.POST)
        if form.is_valid():
            print("form is valid Lead Wala")
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']

            api_url = f"{base_url}/contactUs/"

            course_data = {
                'name': name,
                'phone_number': phone_number,
                'email': email,
            }

            response = requests.post(api_url, data=course_data)

            if response.status_code == 200:
                # Data successfully added
                messages.success(request, 'Data Added Succesfully')
                # downloadpdf()
                request.session['show_success']=True
                return redirect('/')
            else:
                messages.error(request, 'Your are already in our Contacts.')
                return redirect('/')
        else:
            print(form)
            print("form is not valid from Leads")
    else:
        form = leadForm()
        
    return render(request, 'index.html', {'Leads': leads})