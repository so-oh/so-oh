#ドリームジャンボ宝くじ2024の賞金一覧
Reward = [700000000, 150000000, 10000000, 1000000, 100000, 50000, 10000, 3000, 300]

#賞金の獲得確率
probability = [1/20000000, 1/10000000, 1/2500000, 1/50000, 1/100503, 1/10000, 1/1000, 1/100, 1/10]

#新しいリストを作成しておく
alter = []

#期待値を初期化
EV = 0

#インデックスを初期化
i = 0
j = 0

#範囲は賞金のリストの長さでappendメソッドを使ってそれぞれの期待値をalterリストに格納する
for i in range(len(Reward)):
  #それぞれの期待値をcurrent_alterで定義
   current_alter = Reward[i] * probability[i]
   alter.append(current_alter)
   #ここで一応確認
   print(alter)
   #合計の期待値を出す
   EV += current_alter

print("期待値：",EV,'円')

#期待値リストの中から期待値が1以下となる（それひとつしかなかったら一円もリターンがない）金額を特定する
for j in range(len(alter)):
  if alter[j] < 1:
    print('期待値1以下の金額：',Reward[j],'円')
   





