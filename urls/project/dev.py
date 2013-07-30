from urls.dev import *


urlpatterns += (
    url(r'', include('apps.hello.urls')),
    url(r'^polls/', include('apps.polls.urls', namespace='polls')),
)