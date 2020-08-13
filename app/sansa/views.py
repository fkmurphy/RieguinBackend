from django.http import HttpResponse

from datetime import datetime

def date_time(request):
#    import pdb; pdb.set_trace()
    now = datetime.now().strftime('%b %d,%Y - %H:%M hrs')
    return HttpResponse('Current server time is: {now}'.format(now=now))
