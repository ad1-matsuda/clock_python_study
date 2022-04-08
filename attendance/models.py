from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, 'Bar Foo'),
        (2, 'Bar Baz'),
        (3, 'Bar Qux'),
        (4, 'Bar Quux'),
        (5, 'Bar Corge'),
        (6, 'Bar Grault'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')
