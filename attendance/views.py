from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SubmitAttendanceForm
from datetime import datetime
from .controller import ResultController


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
    def __init__(self):
        """
        初期化処理
        """
        # インスタンス作成
        self.result_controller = ResultController()

    def post(self, request):
        form = SubmitAttendanceForm(request.POST)
        now = datetime.now()

        obj = form.save(commit=False)
        obj.in_out = request.POST["in_out"]
        obj.staff = request.user
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        obj.save()

        # コントローラーからコメントを作成
        comment = self.result_controller.create_comment(request, now)

        context = {
            # 'in_out': SubmitAttendance.IN_OUT_STATUS[int(obj.in_out)][1],
            'comment': comment,
        }
        return render(request, 'attendance/result.html', context)
