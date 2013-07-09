from django.conf.urls import url, patterns

from apps.hello.views import HomeTemplateView

urlpatterns = patterns(
    '',
    url(r'^$', HomeTemplateView.as_view(), name='hello_home'),
)