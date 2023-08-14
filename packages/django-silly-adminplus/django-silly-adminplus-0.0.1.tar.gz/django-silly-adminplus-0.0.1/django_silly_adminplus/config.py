from django.conf import settings


SILLY_ADMINPLUS = {
    'TEMPLATE': 'adminplus.html',
    'DSAP_PREFIX': 'dsap/',
}


for key in settings.SILLY_ADMINPLUS:
    SILLY_ADMINPLUS[key] = settings.SILLY_ADMINPLUS[key]
