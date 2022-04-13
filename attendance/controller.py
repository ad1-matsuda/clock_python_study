import locale


class ResultController():
    def __init__(self):
        """
        初期化処理
        """
        # 時刻の文字列変換に必要な設定
        locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

    def create_comment(self, request, time):
        """
        result画面に表示するコメントを作る
        """
        # 時刻の文字列変換
        time_text = time.strftime('%m月%d日%H時%M分%S秒')

        # user名の取得
        user_name = request.user.username
        # 出退勤状態の取得
        in_out = request.POST["in_out"]

        # 出退勤状態に応じてコメントを作成
        if in_out == '1':
            comment = user_name+"さんが"+time_text+"に出勤しました。今日も頑張りましょう！"
        else:
            comment = user_name+"さんが"+time_text+"に退勤しました。お疲れ様でした(^-^)!"

        return comment
