from django.conf.urls import url
from django.contrib import admin
from mainForm.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
]