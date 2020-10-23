# -*- coding: utf-8 -*-
__author__ = "陈章"
__date__ = "2020/10/23 10:18"
from typing import List, Any


def large_list_to_small_list_list(
    large_list: List[Any], k: int = 200
) -> List[List[Any]]:

    # 把大list转成k个一组的小list   【1,2,3,4,5] k = 2  ->  [[1,2],[3,4],[5]]
    if len(large_list) <= k:
        return [large_list]
    tail = 0
    small_list = []
    while tail < len(large_list):
        small_list.append(large_list[tail : tail + k])
        tail = tail + k
    return small_list
