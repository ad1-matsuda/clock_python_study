from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, '開発部'),
        (2, '営業部'),
        (3, '自宅'),
        (4, '客先'),
    )
    IN_OUT = (
        (1, '出勤'),
        (0, '退勤'),
        (2, 'リモート'),
        (3, '外出'),
        (3, '早退'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')
