from multiprocessing import context
from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The homepage"""
    return render(request, 'learning_logs/learning_logs/templates/index.html')

def topics(request):
    """Show all topics"""

    #  database query asking for Topics and sorting by the date_added attributed
    topics = Topic.objects.order_by('date_added')

    # context sent to the template. A context is a dictionary in which the keys are
    # names used in the template to access data, and the values are the data we to
    # send to the template. 
    context = {'topics': topics}
    
    # when building a page that uses data, you have to pass the `context` variable to
    # `render()` as well as the `request` object and the path to the template.
    return render(request, 'learning_logs/learning_logs/templates/topics.html', context)


# The function accepts the value captured by `/<int:topic_id>/` and stores it in 
# `topic_id`
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}


    return render(request, 'learning_logs/learning_logs/templates/topic.html', context)

def new_topic(request):
    """Add a new topic."""

    # Determine whether or not POST is used. The request is not POST return a blank form.
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submited; process data. Make an instance of `TopicForm` and
        # pass it the data entered by the user, stored in `request.POST`.
        form = TopicForm(data=request.POST)
        if form.is_valid(): # form object returned contains the info the user submitted.
            form.save() # write to database
            return redirect('learning_logs:topics') # send user to topics page.


    context = {'form':form}

    # Send the form the template in the context dictionary.
    return render(request, 'learning_logs/learning_logs/templates/new_topic.html', context)

def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/learning_logs/templates/new_entry.html',context)
