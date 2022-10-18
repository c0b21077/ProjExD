# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造が変化する

### 操作方法
- 矢印キーでこうかとんを上下左右に移動する

### 追加機能
- スタート地点とゴール地点を追加
- 穴をランダムな場所に追加
- 経過時間を計測し、ゴール時に表示
- ゴールした時、「おめでとう！！！何秒かかった！」と表示
- 穴に落ちたとき、「ゲームオーバー」と表示

### ToDo（実装しようと思ったけど時間がなかった）
- 穴の色の変更
- 床の部分にだけ穴が生成されるようにすること
- 通り道の色を変更すること