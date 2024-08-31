user_input = str(input('ここに好きな単語を入力してください。:'))

#テキストを,で区切り単語リストにする
word_list = user_input.split()

#単語リスト表示（デバッグ用）
print(word_list)

#空辞書作成
word_count = {}

for word in word_list:
    if(word in word_count):
        word_count[word] += 1 #word_countリストのwordというkeyでカウントを増やす
    else:
        word_count[word] = 1 #新しくでたwordは１

#辞書の出力
print(word_count)

