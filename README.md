# TODO Reminder
![test](https://github.com/KazukiFujita666/robosys2025/actions/workflows/test.yml/badge.svg)

ROS2を使ったTODOリマインダーです。  
メッセージを送信すると、指定時間後にリマインドします。
デフォルトのリマインド時間は5秒です。

## インストール方法

~~~
$ git clone https://github.com/KazukiFujita666/todo_reminder.git
$ cd todo_reminder
$ colcon build --symlink-install
$ source install/setup.bash
~~~

## 使用方法

ノードの起動
~~~
$ ros2 run todo_reminder todo_reminder
~~~
TODOの追加
~~~
$ ros2 topic pub /todo_add std_msgs/msg/String "data: '宿題やる'" -1
~~~

## 必要なソフトウェア
- ROS2
- Python

## テスト環境
- Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Kazuki Fujita
