from django.conf import settings
from django.conf.urls import patterns, url
from django.core.urlresolvers import LocaleRegexURLResolver

urlpatterns = patterns('',
        url(r'^contact_send$', 'edraak_contact.views.contact', name="edraak_contact_send"),
)
