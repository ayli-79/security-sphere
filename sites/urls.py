from django.urls import path
from .views import mvd, sredstva, chs, fire, test, video, yroc, valcovka, yroc2, yroc3, yroc4
from . import views
urlpatterns = [
    path('', mvd, name='mvd'),
    path('sredstva/', sredstva, name='sredstva'),
    path('chs/', chs, name='chs'),
    path('fire/', fire, name='fire'),
    path('test/', test, name='test'),
    path('video/', video, name='video'),
    path('yroc/', yroc, name='yroc'),
    path('valcovka/', valcovka, name='valcovka'),
    path('yroc2/', yroc2, name='yroc2'),
    path('yroc3/', yroc3, name='yroc3'),
    path('yroc4/', yroc4, name='yroc4'),
    path('submit_test/', views.submit_test, name='submit_test'),
]
