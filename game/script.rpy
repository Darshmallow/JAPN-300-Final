# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

# initialize variables
default happiness = 50
default preparedness = 50
define e = Character('Eileen', color="#c8ffc8")
define shimekiri = Character("シメキリ", color="#c8ffc8")
define shiken = Character("シケン先生", color="#c8ffc8")

# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:

    # 背景を表示します。デフォルトではプレースホルダー（仮画像）を使用しますが、
    # images ディレクトリーにファイル（ファイル名は "bg room.png" や "bg room.jpg"）
    # を追加することで表示できます。

    scene bg room

    # スプライト（立ち絵）を表示します。ここではプレースホルダーを使用していますが、
    # images ディレクトリーに "eileen happy.png" などと命名したファイルを追加すると
    # 表示することができます。

    # at ステートメントは画像の表示する位置を調整します。
    # at center は中央に下揃えで表示します。これは省略しても同じ結果になります。
    # その他に at right、at left などがデフォルトで定義されています。

    show eileen happy at center

    # トランジション（画面遷移効果）を使って表示を画面に反映させます。
    # 台詞を表示するか with None を使うと、トランジション無しで直ちに表示します。

    with dissolve

    # 音楽を再生します。
    # game ディレクトリーに "music.ogg" などのファイルを追加すると再生できます。

    # play music "music.ogg"

    # 以下は台詞を表示します。


    e "私は、ブラン大学の一年生、「ドリョク」と言います。   "
    e "期末試験まで、あと一週間しかありません。。。"


label day1:
    "ああ、試験まで五日しかありません。今日は勉強しよう。"
    "あれ？彼女が送信しました。。。えっと、「今晩シメキリの家でパーティーがあるよ。私はちょっと行きたいん、一緒に行きましょう」"
    menu:
        "行こうか"

        "絶対に行く！":
            $ preparedness -= 15
            $ happiness += 15
            jump party

        "。。一人で勉強しましょう":
            $ preparedness += 15
            $ happiness -= 15
            e "たくさん勉強した！よかったね"
label day2:

    # return でゲームを終了します。


label party:
    "party"


label day4:
    shimekiri "明日は期末試験の日だ！準備をしなければいけないんだ。そして、今日勉強しよう。え？"
    "今日、シメキリと一緒に勉強したい。どうしよう？"

    menu:
        "シメキリさんと勉強する":
            $ preparedness += 30
            $ loops = 0
            label loop:
                shimekiri "この問題を見て!"
                $ loops += 1
                menu:
                    "ううん":
                        $ preparedness -= 1
                        $ happiness += 1
                    "うん":
                        $ happiness += 1
                        $ preparedness += 2
                if loops == 10:
                    jump day5
                jump loop
            jump day5

        "一人で勉強する":
            $ preparedness += 15*(happiness/100)
            $ happiness -= 10

label day5:
    "期末試験（きまつしけん） が来ましたああああああ！"
    shiken "期末試験を始まります"
    if preparedness < 10:
        shiken "龜の読み方は？"
        menu:
            "知らない":
                $ ans = True
            "読めない":
                $ ans = False
            "わからない":
                $ ans = False
            "できない":
                $ ans = False
    elif preparedness < 20:
        shiken "ADD HARD QUESTION"
        menu:
            "知らない":
                $ ans = False
            "読めない":
                $ ans = False
            "できない":
                $ ans = False
            "わからない":
                $ ans = True
    elif preparedness < 30:
        shiken "ADD MEDIUM QUESTION"
        menu:
            "2x^2 + c":
                $ ans = True
            "x^2":
                $ ans = False
            "x":
                $ ans = False
            "2x^2":
                $ ans = False
    else:
        shiken "1 + 1 ＝ 何"
        menu:
            "3":
                $ ans = False
            "5":
                $ ans = False
            "2":
                $ ans = True
            "1":
                $ ans = False

label end:
    if ans:
        if happiness < 15:
            "受かった。。。でも友達がわかれたし、かなしくなったし、割に会いましたか？"
        else:
            "受かった！おめでとうございます。"
    else:
        if happiness > 20:
            "受からなかったが、学校以外にも色々なことをしました。"
        else:
            "受からなかった"
