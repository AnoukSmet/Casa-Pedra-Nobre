import datetime


def date_now(request):
    return {'date_now': datetime.datetime.now()}
