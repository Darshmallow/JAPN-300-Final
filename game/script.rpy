# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

# initialize variables
default happiness = 50
default preparedness = 50
default heartBroken = 0

define d = Character('ドリョク', color="#c8ffc8")
define y = Character('ユウワク', color="#c8ffc8")
init:
    image bg home:
        "bg home.jpg"
        zoom 4
style days is text:
    size 200
    font "PottaOne-Regular.ttf"


# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:

    # 背景を表示します。デフォルトではプレースホルダー（仮画像）を使用しますが、
    # images ディレクトリーにファイル（ファイル名は "bg room.png" や "bg room.jpg"）
    # を追加することで表示できます。

    scene bg home

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


    d "私は、ドリョクです！"
    d "ブラン大学一年生で、たくさんの友達もいて、恋人（ユウワクさん）とも仲がいいです"
    d "しかし、期末試験がもうすぐ、金曜日にあります。今から勉強をしなければいけませんが、楽しい大学生活もしたいです"
    d "どうしましょう。。。"


label day1:
    #the text can use a lil styling
    image Sunday = Text("日曜日", style = "days")
    show Sunday at truecenter 
    with dissolve
    pause 1
    hide Sunday
    with dissolve

    scene bg home with fade
    show doryoku happy at center

    "ああ、試験まで五日しかありません。今日は勉強しよう。"
    "あれ？彼女が送信しました。。。えっと、「今晩シメキリの家でパーティーがあるよ。私はちょっと行きたいん、一緒に行きましょう」"
    menu:

        "楽しそう、行こう！":
            $ preparedness -= 15
            $ happiness += 15
            jump party

        "やぱっり一人で勉強しよう":
            $ preparedness += 15
            $ happiness -= 15
            $ heartBroken += 1
            d "試験があるから何にもできないな。。ユウワクは怒れていないでしょう"
            pause 1
            d "たくさん勉強した！よかったね"

label day2:
    scene bg home with fade
    show doryoku happy at right
    show yuuwaku happy at left

    image Monday = Text("月曜日", style = "days")   
    show Monday at truecenter
    with dissolve
    pause 1
    hide Monday
    with dissolve

    d "私は決めた。今日は絶対に勉強しようつもり。"
    y "ええ？でも今晩、コンサートがあるそうだ。好きな歌手も来るので、一緒に行かない？"
    menu:
        "行こう！":
            $ preparedness -= 15
            $ happiness += 10
            jump concert
        "やぱっり一人で勉強しよう":
            $ preparedness += 15
            $ happiness -= 15
            $ heartBroken += 1
            if (heartBroken >= 2):
                show yuuwaku sad 
            y "分かったよ。じゃあ、私一人で行くね。後悔しないで"
            "ああ、怒っているみたい。試験のあとでプレゼントを買おお。今一番大切なことは期末試験だ"
            pause 1
            d "たくさん勉強した！よかったね"

label day3:
    scene bg home with fade
    show doryoku happy at center

    image Tuesday = Text("火曜日", style = "days")   
    show Tuesday at truecenter
    with dissolve
    pause 1
    hide Tuesday
    with dissolve

label day4:

label day5:

    return

label party:
    scene bg party: 
        xzoom 3
        yzoom 3
    show doryoku happy at right
    show yuuwaku happy at left

    default drank = False

    d "わああ、人が多すぎだ。あそこにシメキリがいるね、お酒を飲んでみたい。"
    menu:
        "お酒を飲もう":
            d "いい感じ！"
            $ drank = True
        "ユウワクと話そう":
            y "ね、聞いた？あの子は東大から来たよ"
            d "え、すごいんだ"
    y "そこで色々な人が踊っているな。あ、これはドリョクくん大好きな歌でしょう。"
    menu:
        "一緒に踊りましょう":
            "（踊っている）"
        "もっとお酒を飲もう":
            d "お酒は最高だ！"
            if drank:
                d "あれ、頭が痛い。。。飲みすぎかもしれない。。。"
                $ happiness -= 10
                jump day2 
    d "楽しかった！そして疲れた。家に帰ろう"
    jump day2

label concert:
    scene bg concert
    show doryoku happy at right
    show yuuwaku happy at left

    d "こんでいるね。楽しかったが、好きな歌手はまだ来てないし、今もう十二時間になった。もうすぐ帰った方がいいかな。"
    menu:
        "好きな歌手を待とう":
            $ happiness += 20
            $ preparedness -= 5
            d "出た！私の好きな歌手。いい歌を聞いて感動した。"
        "遅くになったので、家に帰ろう":
            jump day3

