import pandas as pd

def user_click(beforesomeday):
    #使用crosstab统计用户前几天各种操作在各个小时的计数
    user_act_count = pd.crosstab([beforesomeday.user_id,beforesomeday.behavior_type],beforesomeday.hour,dropna=False)
    user_act_count = user_act_count.unstack(fill_value = 0)#fill_value参数表示替换缺失值的值
    return user_act_count

def user_liveday(train_user_window1):
    #用户各个行为活跃的天数
    user_live = train_user_window1.groupby(by = ['user_id','behavior_type']).agg({"daystime":lambda x:x.nunique()})
    user_live = user_live.unstack(fill_value=0)
    return user_live

def user_item_click(beforesomeday):
    #统计用户对每种商品每种行为在每个小时的点击数
    user_item_act_count = pd.crosstab([beforesomeday.user_id,beforesomeday.item_id,beforesomeday.behavior_type],beforesomeday.hour)
    user_item_act_count = user_item_act_count.unstack(fill_value = 0)
    return user_item_act_count

def user_cate_click(beforesomeday):
    ＃统计用户对每种商品类别每种行为在每个小时的点击数
    user_cate_act_count = pd.crosstab([beforesomeday.user_id,beforesomeday.item_category,beforesomeday.behavior_type],beforesomeday.hour)
    user_cate_act_count = user_cate_act_count.unstack(fill_value=0)
    return user_cate_act_count

def user_item_long_touch(train_user_window1):
    _live = train_user_window1.groupby(by = ['user_id','item_id']).agg({"daystime":lambda x:(x.max()-x.min()).days})
    return _live

def user_cate_long_touch(train_user_window1):
    _live = train_user_window1.groupby(by = ['user_id','item_category']).agg({"daystime":lambda x:(x.max()-x.min()).days})
    return _live
