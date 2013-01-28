
from django.shortcuts import render_to_response
from hello_polls.models import MyPoll

def index(request):
    three_newest_polls = MyPoll.objects.all().order_by('-pub_date')[:3]
    print three_newest_polls
    return render_to_response('hello_polls/index.html', {'three_newest_polls': three_newest_polls})