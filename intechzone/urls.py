"""intechzone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header = "Contact Admin"
admin.site.site_title = "Contact Admin Portal"
admin.site.index_title = "Welcome to Contact Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    # index
    path('',views.index,name='index'),

    #contacts
    path('contacts/',views.contact,name='contacts'),

    # careers
    path('careers/',views.careers,name='careers'),

    #webservices
    path('webservices/',views.webservices,name='webservices'),
    path('webservices/ecommerce/',views.webecommerce,name='web-ecommerce'),
    path('webservices/chat-bots/',views.webchatbot,name='web-chatbot'),
    path('webservices/nodejs/',views.webnode,name='web-node'),
    path('webservices/meteor/',views.webmeteor,name='web-meteor'),

    #desktopservices
    path('desktopservices/',views.desktopservices,name='desktopservices'),

    #outstaffing
    path('outstaffing/',views.outstaffing,name='outstaffing'),
    path('outstaffing/Senior/',views.outstaffing_senior,name='out_senior'),
    path('outstaffing/Team/',views.outstaffing_team,name='out_team'),
    path('outstaffing/Technical/',views.outstaffing_technical,name='out_tech'),

    # mobileservices
    path('mobileservices/',views.mobileservices,name='mobileservices'),
    path('mobileservices/android',views.mobileservices_android,name='mobileservices_android'),
    path('mobileservices/apple',views.mobileservices_apple,name='mobileservices_apple'),

    #proof of concept
    path('proof-of-concept/',views.proof,name='proof'),

    #about
    path('about/team/',views.about_team,name='team'),
    path('about/values/',views.about_values,name='values'),
    path('about/opensource/',views.about_opensource,name='opensource'),
    path('about/socialside/',views.about_social,name='social'),
    path('about/socialside/inner/',views.about_social_inner,name='socialinner'),

    #approach
    path('approach/agile-project/',views.approach_agile,name='agile_project'),
    path('approach/cutting-edge/',views.approach_cutting_edge,name='cutting_edge'),
    path('approach/high-performance/',views.approach_high_performance,name='high_performance'),
    path('approach/high-quality/',views.approach_high_quality,name='high_quality'),
    path('approach/lean_approach/',views.approach_lean,name='lean_approach'),
    path('approach/minimum_val_product/',views.approach_min,name='minimum_val'),

    #portfolio
    path('portfolio/',views.portfolio,name='portfolio'),

    #blog
    path('blog/',views.blog,name='blog'),


    #technical pages
    #apis
    path('api-integration/',views.api,name='api'),
    path('api-integration/brain/',views.api_brain,name='api_brain'),
    path('api-integration/elastic/',views.api_elastic,name='api_elastic'),
    path('api-integration/grap/',views.api_grap,name='api_grap'),
    path('api-integration/paypal/',views.api_paypal,name='api_paypal'),
    path('api-integration/rest/',views.api_rest,name='api_rest'),
    path('api-integration/stripe/',views.api_stripe,name='api_stripe'),

    #apps
    path('tech-apps/',views.apps,name='apps'),
    path('tech-apps/ACC/',views.apps_ACC,name='apps_acc'),
    path('tech-apps/cordova/',views.apps_cordova,name='apps_cordova'),
    path('tech-apps/electron/',views.apps_electron,name='apps_electron'),
    path('tech-apps/phone/',views.apps_phone,name='apps_phone'),
    path('tech-apps/prog/',views.apps_prog,name='apps_prog'),
    path('tech-apps/rn/',views.apps_rn,name='apps_rn'),

    #backend
    path('backend/',views.backend,name='backend'),
    path('backend/express/',views.backend_express,name='backend_express'),
    path('backend/hapi/',views.backend_hapi,name='backend_hapi'),
    path('backend/meteor/',views.backend_METEOR,name='backend_meteor'),

    # database
    path('database/',views.database,name='database'),
    path('database/mongo/',views.database_mongo,name='database_mongo'),
    path('database/mysql/',views.database_mysql,name='database_mysql'),
    path('database/neo/',views.database_neo,name='database_neo'),
    path('database/post/',views.database_post,name='database_post'),

    #frontend
    path('frontend/',views.frontend,name='frontend'),
    path('frontend/angular',views.frontend_angular,name='frontend_angular'),
    path('frontend/angular2',views.frontend_angular2,name='frontend_angular2'),
    path('frontend/aurelia',views.frontend_aurelia,name='frontend_aurelia'),
    path('frontend/next',views.frontend_next,name='frontend_next'),
    path('frontend/react/',views.frontend_react,name='frontend_react'),
    path('frontend/react-native/',views.frontend_reactnative,name='frontend_reactnative'),
    path('frontend/redux/',views.frontend_redux,name='frontend_redux'),
    path('frontend/vue/',views.frontend_vue,name='frontend_vue'),
    

]
