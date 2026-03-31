import random
from django.shortcuts import render
from .models import Passage

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TypingRecord

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max

# Create your views here.
@login_required
def typing_test(request):

    # Get difficulty from URL
    difficulty = request.GET.get('difficulty', 'easy')

    # Filter passages by difficulty
    passages = Passage.objects.filter(difficulty=difficulty)

    # If no passages exist
    if not passages.exists():
        return render(
            request, 'typeit/typing_test.html',
            {
                'passage': None,
                'difficulty': difficulty
            }
        )

    # Pick random passage
    passage = random.choice(passages)

    return render(
        request,
        'typeit/typing_test.html',
        {
            'passage': passage,
            'difficulty': difficulty
        }
    )

@login_required
def save_result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        TypingRecord.objects.create(
            user=request.user,  # it's important as it connect records to logged-in user
            duration=data['duration'],
            total_chars=data['total_chars'],
            correct_chars=data['correct_chars'],

            errors=data['errors'],
            wpm=data['wpm'],
            accuracy=data['accuracy']
        )

        return JsonResponse({"status": "success"})


@login_required
def typing_history(request):
    records = (TypingRecord.objects.filter(user=request.user).order_by('-created_at'))

    return render(request, 'typeit/history.html', {'records': records})


@login_required
def dashboard(request):

    records = TypingRecord.objects.filter(user=request.user)

    # Total tests
    total_tests = records.count()

    # Best WPM
    best_wpm = records.aggregate(Max('wpm'))['wpm__max']

    # Average WPM
    avg_wpm = records.aggregate(Avg('wpm'))['wpm__avg']

    # Latest Accuracy
    latest_record = records.order_by('-created_at').first()

    # get wpm data for graph show
    wpm_records = records.order_by('created_at')
    wpm_data = []

    for record in wpm_records:
        wpm_data.append(record.wpm)

    if latest_record:
        latest_accuracy = latest_record.accuracy
    else:
        latest_accuracy = 0

    # get accuracy data for graph show
    accuracy_records = records.order_by('created_at')
    accuracy_data = []

    for record in accuracy_records:
        accuracy_data.append(record.accuracy)

    # get date labels for graph
    date_labels = []
    for record in wpm_records:
        date_labels.append(
            record.created_at.strftime("%d-%b")
        )

    context = {
        'total_tests': total_tests,
        'best_wpm': best_wpm or 0,
        'avg_wpm': round(avg_wpm or 0, 2),
        'latest_accuracy': latest_accuracy,

        # Graph data
        'wpm_data': wpm_data,
        'accuracy_data': accuracy_data,
        'date_labels': date_labels,
    }

    return render(request, 'typeit/dashboard.html', context)


@login_required
def profile(request):

    # get profile details
    user_profile = request.user.userprofile

    # get typing records
    records = TypingRecord.objects.filter(user=request.user)

    # total tests
    total_tests = records.count()

    # best wpm
    best_wpm = records.aggregate(Max('wpm'))['wpm__max']

    # Average WPM
    avg_wpm = records.aggregate(Avg('wpm'))['wpm__avg']

    context = {
        'profile': user_profile,
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'total_tests': total_tests,
        'best_wpm': best_wpm or 0,
        'avg_wpm': round(avg_wpm or 0, 2)
    }

    return render(request, 'typeit/profile.html', context)


@login_required
def leaderboard(request):
    from django.contrib.auth.models import User
    users = User.objects.all()

    leaderboard_data = []

    for user in users:
        records = TypingRecord.objects.filter(user=user)

        best_wpm = records.aggregate(Max('wpm'))['wpm__max']

        if best_wpm:
            profile = user.userprofile
            leaderboard_data.append({
                'full_name': profile.full_name,
                'best_wpm': best_wpm
            })

    # sort data in descending wpm
    leaderboard_data.sort(key=lambda x: x['best_wpm'], reverse=True)

    # Take top 10
    leaderboard_data = leaderboard_data[:10]

    context = {
        'leaderboard': leaderboard_data
    }

    return render(request, 'typeit/leaderboard.html', context)