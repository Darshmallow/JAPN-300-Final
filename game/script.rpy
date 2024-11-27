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
define t = Character('ガイヘン', color="#c8ffc8")
define shimekiri = Character("シメキリ", color="#c8ffc8")
define shiken = Character("シケン先生", color="#c8ffc8")

init:
    image bg home:
        "bg home.jpg"
        zoom 1
    image Doryoku happy:
        "Doryoku happy.png"
        zoom 0.4
    image Yuuwaku happy:
        "Yuuwaku happy.png"
        zoom 0.4
    image Taihen happy:
        "Taihen happy.png"
        zoom 0.4
    image Shimekiri happy:
        "Shimekiri happy.png"
        zoom 0.4

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

    show Doryoku happy at center

    # トランジション（画面遷移効果）を使って表示を画面に反映させます。
    # 台詞を表示するか with None を使うと、トランジション無しで直ちに表示します。

    with dissolve

    # 音楽を再生します。
    # game ディレクトリーに "music.ogg" などのファイルを追加すると再生できます。

    # play music "music.ogg"

    # 以下は台詞を表示します。


    d "私は、ドリョクです！"
    d "ブラン大学一年生で、たくさんの友達もいて、恋人（ユウワク）とも仲がいいです"
    d "しかし、期末試験がもうすぐ、金曜日にある。今から勉強をしなければいけないが、楽しい大学生活もしたい"
    d "どうしましょう。。。"


label day1:
    #the text can use a lil styling
    scene bg home with fade
    image Sunday = Text("日曜日", style = "days")
    show Sunday at truecenter 
    with dissolve
    pause 1
    hide Sunday
    with dissolve

    show Doryoku happy at center

    "ああ、試験まで五日しかない。今日は勉強しよう。"
    "あれ？彼女が送信した。。。えっと、「今晩シメキリの家でパーティーがあるよ。私はちょっと行きたいん、一緒に行きましょう」"
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
            d "（勉強している）"
            pause 1
            d "でもたくさん勉強した！よかったね"

label day2:
    scene bg home with fade
    image Monday = Text("月曜日", style = "days")   
    show Monday at truecenter
    with dissolve
    pause 1
    hide Monday
    with dissolve

    show Doryoku happy at right
    show Yuuwaku happy at left


    d "私は決めた。今日は絶対に勉強しようつもり。"
    y "ええ？でも今晩、コンサートがあるそうだ。好きな歌手も来るので、行かない？"
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
                show Yuuwaku  
                y "分かったよ。じゃあ、私一人で行くね。後悔しないで"
                "ああ、怒っているみたい。試験のあとでプレゼントを買おお。今一番大切なことは期末試験だ"
            d "（勉強している）"
            pause 1
            d "たくさん勉強した！よかったね"

label day3:
    scene bg home with fade
    image Tuesday = Text("火曜日", style = "days")  
    show Tuesday at truecenter
    with dissolve
    pause 1
    hide Tuesday
    with dissolve

    show Taihen happy at center

    t "ね、試験はもうすぐだが、私はぜんぜんわからない。。。今日一緒に勉強しながら教えてくれない？"
    menu:
        "いいよ、勉強しよう！":
            jump room
        "今日はちょっと。。。(一人で勉強しよう)":
            $ preparedness += 15
            $ happiness -= 15
            d "（勉強している）"
            pause 1
            d "たくさん勉強した！よかったね"
    
    jump day4

label day4:
    scene bg home with fade
    image Wednesday = Text("水曜日", style = "days")  
    show Wednesday at truecenter
    with dissolve
    pause 1
    hide Wednesday
    with dissolve

    show Doryoku happy at center

    d "期末試験をもうパスした人がいるね、羨ましいなあ。外でちょっと騒音が聞こえて、何かあったか。"
    d "え、だれがドアをノックしている"
    pause 1
    show Shimekiri happy at right
    shimekiri "ねね、ユウワクと一緒にスマブラをしたい。超楽しいよ"
    menu: 
        "ユウワク、シメキリと一緒にスマブラをしよう":
            $ preparedness -= 15
            $ happiness += 10
            jump game
        "一人で勉強しよう":
            $ preparedness += 15
            $ happiness -= 15
            d "（勉強している）"
            pause 1
            d "たくさん勉強した！よかったね"


label day5:
    scene bg home with fade
    image Thursday = Text("木曜日", style = "days")  
    show Thursday at truecenter
    with dissolve
    pause 1
    hide Thursday
    with dissolve

    show Doryoku happy at right
    show Shimekiri happy at left

    shimekiri "明日は期末試験の日だ！準備をしなければいけないんだ。そして、今日勉強しよう。え？"
    "今日、シメキリと一緒に勉強したい。どうしよう？"

    menu:
        "シメキリさんと勉強しよう":
            $ preparedness += 30
            $ happiness -= 10
            jump studyRoom

        "一人で勉強しよう":
            $ preparedness += 15*(happiness/100)
            $ happiness -= 10
            d "（勉強している）"
            pause 1
            d "たくさん勉強した！よかったね" 
    jump day6
    

label day6:
    scene bg home with fade
    image Friday = Text("金曜日", style = "days")  
    show Friday at truecenter
    with dissolve
    pause 1
    hide Friday
    with dissolve

    show Doryoku happy at center
    "今日は期末試験だ！"
    menu:
        "試験の場所に行こう":
            jump test

label end:
    scene bg home with fade

    show Doryoku happy at center

    d "緊張している。。今日は試験結果を出すの日だ"
    if (happiness > 50):
        show Yuuwaku happy at left
        show Taihen happy at right
        d "え、みんななんでここに来たの？"
        y "驚き！私たちは、ドリョクを応援するためにここにいます"
    if ans:
        if happiness < 50:
            d "合格した！今日はユウワクとちゃんと晩ご飯をたべよう。今電話をかける"
            "（電話中...）"
            d "あのさ、今日はーー" 
            y "もういいよ、約束を守らないやつは大嫌いだ。別れることにした"
            d "え、ちょっと聞いて、おい"
            "電話を切りました。。。"
            d "休みだから、暇すぎ。彼女が別れたら、何かしようか。今は疲れて、とてもつまらない"
            d "え、私、好きな物はなんだって。"
            d "楽しいという感情は、もう感じられない"
            "合格だが。。。でも友達がわかれたし、かなしくなったし、割に会いましたか？"
        else:
            d "合格した！"
            y "わあああやっぱり。ドリョクは最高だから。"
            t "おめでとう！！！今晩はぼくおごるよ"
            d "みんなも、ずっと応援してありがとうね"
            "すごい！本当にHappy Endingだよ"
    else:
        if happiness > 50:
            d "合格しなかった。。。失敗した。。。"
            y "大丈夫大丈夫、来学期頑張ればきっと満点を取れるから。"
            t "そうだよ。ドリョクなら問題がない"
            d "君たちのような友達がいて、本当によかった。"
            "合格できなくても、学校以外にも色々なことをしました。最悪じゃないでしょう"
        else:
            d "合格しなかった。。。失敗した。。。"
            d "あのさ、今日はーー" 
            y "もういいよ、約束を守らないやつは大嫌いだ。別れることにした"
            d "え、ちょっと聞いて、おい"
            "電話を切りました。。。"
            d "休みだから、暇すぎ。彼女が別れたら、何かしようか。今は疲れて、とてもつまらない"
            d "え、私、好きな物はなんだって。"
            d "楽しいという感情は、もう感じられない"
            "合格しなかった。そして、学校以外のこともしなかった。もう一回なら、ちゃんと選べばよかったね。"
    jump gameEnd


label party:
    scene bg party: 
        xzoom 1
        yzoom 1
    with fade
    show Doryoku happy at right
    show Yuuwaku happy at left

    default drank = False
    d "わああ、人が多すぎ。あそこにシメキリがいるね、お酒を飲んでみたい。"
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
                y "大丈夫？顔色が悪い。ね、ドリョク、聞こえる？"
                d "すべてが消え去っていく。。。"
                jump day2 
    d "楽しかった！そして疲れた。家に帰ろう"
    jump day2


label concert:
    scene bg concert with fade
    show Doryoku happy at right
    show Yuuwaku happy at left

    y "こんでいるね、みんあエネルギーがたくさんある。音楽と踊りましょう！"
    pause 1
    d "楽しかったが、好きな歌手はまだ来てないし、今もう十二時間になった。もうすぐ帰った方がいいかな。"
    menu:
        "好きな歌手を待とう":
            $ happiness += 20
            $ preparedness -= 5
            d "出た！私の好きな歌手。いい歌を聞いて感動した。"
        "遅くになったので、家に帰ろう":
            jump day3
    jump day3

label room:
    scene bg library:
        xzoom 1.8
        yzoom 1.8
    with fade
    show Taihen happy at left
    show Doryoku happy at right
    pause 2

    t "このかっこいいチックトックリールを見よう"
    menu:
        "ううん、勉強しなきゃ":
            $ happiness += 5
            $ preparedness -= 5
        "うん、見せて":
            $ happiness -= 5
            $ preparedness += 2
    pause 1
    t "このおもしろいチックトックリールを見よう"
    menu:
        "ううん、勉強しなきゃ":
            $ happiness += 5
            $ preparedness -= 5
        "うん、見せて":
            $ happiness -= 5
            $ preparedness += 2
    pause 1
    t "この人気があるチックトックリールを見よう"
    menu:
        "ううん、勉強しなきゃ":
            $ happiness += 5
            $ preparedness -= 5
        "うん、見せて":
            $ happiness -= 5
            $ preparedness += 2
    pause 1
    t "今日は楽しかったぜ。そろそろ帰ろう"
    d "あ、はい。じゃ、またね"
    "ずっと図書館にいっても、何も習わないな。。。"
    jump day4

label game:
    scene bg lounge with fade
    show Shimekiri happy at left
    show Doryoku happy at center
    show Yuuwaku happy at right

    "（ゲームが進行中）"
    "負けた！もう一回しましょうか？"
    menu:
        "うん":
            d "もう一回！今度は絶対に勝ちます"
            shimekiri "無理だよ、今度も私の勝"
            $ happiness += 10
            $ preparedness -= 10
        "ここで止める":
            d "勉強しなければいけない。みんな、またあした！"
            $ preparedness += 5
            $ happiness -= 5
    jump day5

label studyRoom:
    scene bg library:
        xzoom 1.8
        yzoom 1.8
    with fade
    show Shimekiri happy at left
    show Doryoku happy at right

    $ loops = 0
    label loop:
        "シメキリと一緒に、なんとなく静かになった。とても集中できる"
        shimekiri "この問題を見て!"
        $ loops += 1
        menu:
            "ううん":
                $ preparedness -= 2
                $ happiness += 2
                        
            "うん":
                $ happiness += 2
                $ preparedness += 4
                shimekiri "まず、そうしよう。かっこいい問題でしょう？"
                d "あ、すごい！この問題はとても簡単になった！"
        if loops == 5:
            jump day6
    jump loop

label test:
    scene bg classroom with fade
    show shiken at center

    shiken "期末試験を始まります"
    if preparedness < 30:
        shiken "龜の読み方は？"
        menu:
            "知らない":
                $ ans = False
            "読めない":
                $ ans = False
            "わからない":
                $ ans = False
            "できない":
                $ ans = False

    elif preparedness < 60:
        shiken "挨拶の読み方は"
        menu:
            "あいさつ":
                $ ans = True
            "あいせま":
                $ ans = False
            "けいさつ":
                $ ans = False
            "えさ":
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
    jump end

label gameEnd:
    $ MainMenu(confirm=False)()
