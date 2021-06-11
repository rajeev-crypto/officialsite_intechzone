from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ContactForm, CareerForm
from django.contrib import messages


# Create your views here.


 #contacts
def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,"- Message sent..!")
            
            return redirect('contacts')
    else:
        f = ContactForm()
    return render(request, 'contacts.htm', {'form': f})

#careers page
def careers(request):
    if request.method == 'POST':
        f = CareerForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.add_message(request, messages.INFO, 'Sent.')
            messages.success(request,"Your Response is Recorded")
            return redirect('careers')
    else:
        f = CareerForm()
    return render(request, 'careers.htm', {'form': f})

#index
def index(request):
    template = loader.get_template('index.htm')
    return HttpResponse(template.render())

#services

#web services
def webservices(request):
    template = loader.get_template('services-web_development.htm')
    return HttpResponse(template.render())

def webecommerce(request):
    template = loader.get_template('services-web_development-E.htm')
    return HttpResponse(template.render())

def webchatbot(request):
    template = loader.get_template('services-web_development-CHAT.htm')
    return HttpResponse(template.render())

def webnode(request):
    template = loader.get_template('services-web_development-NODE.htm')
    return HttpResponse(template.render())

def webmeteor(request):
    template = loader.get_template('services-web_development-METEOR.htm')
    return HttpResponse(template.render())

#desktop services
def desktopservices(request):
    template = loader.get_template('services-desktop_applications.htm')
    return HttpResponse(template.render())

#desktop services
def proof(request):
    template = loader.get_template('services-proof.htm')
    return HttpResponse(template.render())

#outstaffing
def outstaffing(request):
    template = loader.get_template('services-outstaffing.htm')
    return HttpResponse(template.render())

def outstaffing_senior(request):
    template = loader.get_template('services-outstaffing-SENIOR.htm')
    return HttpResponse(template.render())

def outstaffing_team(request):
    template = loader.get_template('services-outstaffing-TEAM.htm')
    return HttpResponse(template.render())

def outstaffing_technical(request):
    template = loader.get_template('services-outstaffing-TECHNICAL.htm')
    return HttpResponse(template.render())

#mobile services
def mobileservices(request):
    template = loader.get_template('services-mobile_development.htm')
    return HttpResponse(template.render())

def mobileservices_android(request):
    template = loader.get_template('services-mobile_development-ANDROID.htm')
    return HttpResponse(template.render())

def mobileservices_apple(request):
    template = loader.get_template('services-mobile_development-APPLE.htm')
    return HttpResponse(template.render())


# about pages
def about_values(request):
    template = loader.get_template('about-values.htm')
    return HttpResponse(template.render())

def about_team(request):
    template = loader.get_template('about-team.htm')
    return HttpResponse(template.render())

def about_opensource(request):
    template = loader.get_template('about-open_source.htm')
    return HttpResponse(template.render())

def about_social(request):
    template = loader.get_template('about-social_side.htm')
    return HttpResponse(template.render())

def about_social_inner(request):
    template = loader.get_template('about-social_side-inner.htm')
    return HttpResponse(template.render())

#approach
def approach_agile(request):
    template = loader.get_template('approach-agile_project.htm')
    return HttpResponse(template.render())

def approach_cutting_edge(request):
    template = loader.get_template('approach-cutting_edge.htm')
    return HttpResponse(template.render())

def approach_high_performance(request):
    template = loader.get_template('approach-high_performance.htm')
    return HttpResponse(template.render())

def approach_high_quality(request):
    template = loader.get_template('approach-high_quality.htm')
    return HttpResponse(template.render())

def approach_lean(request):
    template = loader.get_template('approach-lean_approach.htm')
    return HttpResponse(template.render())

def approach_min(request):
    template = loader.get_template('approach-minimum_val_product.htm')
    return HttpResponse(template.render())

#blog
def blog(request):
    template = loader.get_template('blog.htm')
    return HttpResponse(template.render())

#portfolio
def portfolio(request):
    template = loader.get_template('portfolio.htm')
    return HttpResponse(template.render())


#technical pages

#api integration
def api(request):
    template = loader.get_template('tech-api_integration.htm')
    return HttpResponse(template.render())

def api_brain(request):
    template = loader.get_template('tech-api_integration-BRAIN.htm')
    return HttpResponse(template.render())

def api_elastic(request):
    template = loader.get_template('tech-api_integration-ELASTIC.htm')
    return HttpResponse(template.render())

def api_grap(request):
    template = loader.get_template('tech-api_integration-GRAP.htm')
    return HttpResponse(template.render())

def api_paypal(request):
    template = loader.get_template('tech-api_integration-PAYPAL.htm')
    return HttpResponse(template.render())

def api_rest(request):
    template = loader.get_template('tech-api_integration-REST.htm')
    return HttpResponse(template.render())

def api_stripe(request):
    template = loader.get_template('tech-api_integration-STRIPE.htm')
    return HttpResponse(template.render())
    

#apps
def apps(request):
    template = loader.get_template('tech-apps.htm')
    return HttpResponse(template.render())

def apps_ACC(request):
    template = loader.get_template('tech-apps-ACC.htm')
    return HttpResponse(template.render())

def apps_cordova(request):
    template = loader.get_template('tech-apps-CORDOVA.htm')
    return HttpResponse(template.render())

def apps_electron(request):
    template = loader.get_template('tech-apps-ELECTRON.htm')
    return HttpResponse(template.render())
        
def apps_phone(request):
    template = loader.get_template('tech-apps-PHONE.htm')
    return HttpResponse(template.render())

def apps_prog(request):
    template = loader.get_template('tech-apps-PROG.htm')
    return HttpResponse(template.render())
    
def apps_rn(request):
    template = loader.get_template('tech-apps-RN.htm')
    return HttpResponse(template.render())


#backend pages
def backend(request):
    template = loader.get_template('tech-back_end.htm')
    return HttpResponse(template.render())

def backend_express(request):
    template = loader.get_template('tech-back_end-EXPRESS.htm')
    return HttpResponse(template.render())

def backend_hapi(request):
    template = loader.get_template('tech-back_end-HAPI.htm')
    return HttpResponse(template.render())

def backend_METEOR(request):
    template = loader.get_template('tech-back_end-meteor.htm')
    return HttpResponse(template.render())

#database
def database(request):
    template = loader.get_template('tech-data_base.htm')
    return HttpResponse(template.render())

def database_mongo(request):
    template = loader.get_template('tech-data_base-MONGO.htm')
    return HttpResponse(template.render())

def database_mysql(request):
    template = loader.get_template('tech-data_base-MYSQL.htm')
    return HttpResponse(template.render())

def database_neo(request):
    template = loader.get_template('tech-data_base-NEO.htm')
    return HttpResponse(template.render())

def database_post(request):
    template = loader.get_template('tech-data_base-POST.htm')
    return HttpResponse(template.render())

#frontend
def frontend(request):
    template = loader.get_template('tech-front_end.htm')
    return HttpResponse(template.render())

def frontend_angular(request):
    template = loader.get_template('tech-front_end-ANGULAR.htm')
    return HttpResponse(template.render())

def frontend_angular2(request):
    template = loader.get_template('tech-front_end-ANGULAR_2.htm')
    return HttpResponse(template.render())

def frontend_aurelia(request):
    template = loader.get_template('tech-front_end-AURELIA.htm')
    return HttpResponse(template.render())

def frontend_next(request):
    template = loader.get_template('tech-front_end-NEXT.htm')
    return HttpResponse(template.render())

def frontend_react(request):
    template = loader.get_template('tech-front_end-REACT.htm')
    return HttpResponse(template.render())

def frontend_reactnative(request):
    template = loader.get_template('tech-front_end-REACT_N.htm')
    return HttpResponse(template.render())

def frontend_redux(request):
    template = loader.get_template('tech-front_end-REDUX.htm')
    return HttpResponse(template.render())

def frontend_vue(request):
    template = loader.get_template('tech-front_end-VUE.htm')
    return HttpResponse(template.render())