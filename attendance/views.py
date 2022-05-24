from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubmitAttendance
from .forms import SubmitAttendanceForm
from datetime import datetime


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        form = SubmitAttendanceForm
        context = {
            'form': form,
            "user": request.user,
        }
        return render(request, 'attendance/index.html', context)


class ResultView(View):
    def post(self, request):
        form = SubmitAttendanceForm(request.POST)
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        now_date = str(month) + "月" + str(day) + "日" + str(hour) + "時" + str(minute) + "分"

        obj = form.save(commit=False)
        obj.place = request.POST["place"]
        obj.in_out = request.POST["in_out"]
        obj.staff = request.user
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        obj.save()
        if request.POST["in_out"] == '1':
            comment = now_date + "\n" + "出勤確認しました。今日も頑張りましょう！"
        elif request.POST["in_out"] == '2':
            comment = now_date + "\n" + "外出確認しました。行ってらっしゃい！(^-^)/"
        elif request.POST["in_out"] == '3':
            comment = now_date + "\n" + "早退確認しました。お疲れ様でした！(^-^)"
        else:
            comment = now_date + "\n" + "退勤確認しました。お疲れ様でした(^-^)!"
        context = {
            'place': SubmitAttendance.PLACES[int(obj.place)-1][1],
            'comment': comment,
        }
        return render(request, 'attendance/result.html', context)
