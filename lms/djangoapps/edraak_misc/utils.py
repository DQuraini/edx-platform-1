from courseware.access import has_access
from django.conf import settings


def is_certificate_allowed(user, course):
    if not settings.FEATURES.get('ENABLE_ISSUE_CERTIFICATE'):
        return False

    return course.has_ended() or has_access(user, 'staff', course.id)


def sort_closed_courses_to_bottom(courses):
    """
    Sorts the courses by their `has_ended()`, open courses come first.
    """

    open_courses = [course for course in courses if not course.has_ended()]
    ended_courses = [course for course in courses if course.has_ended()]

    return open_courses + ended_courses


def filter_invitation_only_courses(courses):
    """
    Filter out the courses with invitation_only flag set to true.
    """

    return [course for course in courses if not course.invitation_only]


def edraak_courses_logic(courses):
    courses = filter_invitation_only_courses(courses)
    courses = sort_closed_courses_to_bottom(courses)
    return courses


def get_absolute_url_prefix(request):
    schema = 'https' if request.is_secure() else 'http'
    prefix = '{schema}://{host}'.format(schema=schema, host=settings.SITE_NAME)
    return prefix


def validate_email(email):
    """
    Validate email, the strict or the quick way depending on `FEATURES['EMAIL_STRICT_VERIFICATION']`.
    """
    is_strict = settings.FEATURES.get('EMAIL_STRICT_VERIFICATION', True)
    log.info(u'Validating user email=%(email)s, strict_verification=%(is_strict)s', {
        'email': email,
        'is_strict': is_strict,
    })

    if is_strict:
        is_valid = strict_validate_email(
            email=email,
            check_mx=True,
            debug=True,
        )
    else:
        try:
            django_validate_email(email)
            is_valid = True
        except DjangoValidationError:
            is_valid = False

    log.info(u'Validating user email=%(email)s, strict_verification=%(is_strict)s, is_valid=%(is_valid)s', {
        'email': email,
        'is_strict': is_strict,
        'is_valid': is_valid,
    })

    return is_valid
