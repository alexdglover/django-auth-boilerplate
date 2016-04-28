from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

app_name = 'simpleauthexample'
urlpatterns = patterns('',
   url(r'^login/', 'simpleauthexample.views.loginview', name='login'),
   url(r'^logout/', 'simpleauthexample.views.logout_view', name='logout'),
   url(r'^auth/', 'simpleauthexample.views.auth_and_login', name='auth'),
   url(r'^signup/', 'simpleauthexample.views.sign_up_in', name='signupin'),
   url(r'^$', 'simpleauthexample.views.secured', name='root'),
)
