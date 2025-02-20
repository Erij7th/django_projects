from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'viewsbasics'
urlpatterns = [
    path('', TemplateView.as_view(template_name='viewsbasics/index.html')),
    path('funktionally', views.funktionally),
    path('danger', views.danger),
    path('safer', views.safer),
    path('prettyurldata/<thing>', views.prettyurldata),
    path('bounce', views.bounce),
    path('icecream', views.icecream.as_view()),
    path('bmi/<int:height>/<int:weight>', views.BMI.as_view()),
    path('distance/<speed>/<time>', views.distance.as_view())

    ]
