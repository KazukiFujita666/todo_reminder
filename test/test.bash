#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kazuki Fujita
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が失敗"
    res=1
}

res=0

# 正常系: "宿題やる" を追加
out=$(ros2 topic pub /todo_add std_msgs/msg/String "data: '宿題やる'" -1)
[ "$?" = 0 ] || ng "$LINENO"

# 正常系: "掃除する" を追加
out=$(ros2 topic pub /todo_add std_msgs/msg/String "data: '掃除する'" -1)
[ "$?" = 0 ] || ng "$LINENO"

# 異常入力: 空文字
out=$(ros2 topic pub /todo_add std_msgs/msg/String "data: ''" -1 2>/dev/null)
[ "$?" = 0 ] || ng "$LINENO"

[ "$res" = 0 ] && echo "OK"
exit $res

