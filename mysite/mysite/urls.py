from django.conf.urls import include, url
from django.contrib import admin

# from django.conf import settings

# from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# admin.autodiscover()

urlpatterns = [
    url(r'^ex/', include('simp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# if settings.DEBUG:
#     from django.views.static import serve
#     urlpatterns += [
#         url(r'^(?P<path>favicon\..*)$', serve, {'document_root': settings.STATIC_ROOT}),
#         url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
#         url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], serve, dict(insecure=True)),
#     ]

