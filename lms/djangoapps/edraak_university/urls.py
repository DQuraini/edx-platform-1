"""
URLs for the student support app.
"""
from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',  # nopep8
    url(
       r'^id/{}$'.format(settings.COURSE_ID_PATTERN),
       'edraak_university.views.university_id',
       name='edraak_university_id',
    ),
    url(
       r'^id/{}/success$'.format(settings.COURSE_ID_PATTERN),
       'edraak_university.views.university_id_success',
       name='edraak_university_id_success',
    ),
)
