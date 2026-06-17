def get_meals(state):

    # 🥗 午餐固定轻食
    lunch = "轻食沙拉 + 鸡胸肉 + 全麦碳水"

    # 🍳 早餐轮换
    breakfast_list = [
        "热干面 + 鸡蛋",
        "蒸饺 + 鸡蛋"
    ]

    breakfast = breakfast_list[state["food_index"] % 2]

    state["food_index"] += 1

    # 🌙 晚餐
    if state["fatigue"] > 70:
        dinner = "蛋白粉 + 沙拉（低碳）"
    elif state["fatigue"] > 40:
        dinner = "鸡胸肉 + 鸡蛋"
    else:
        dinner = "热干面 + 鸡蛋（补能）"

    return f"早餐：{breakfast}\n午餐：{lunch}\n晚餐：{dinner}"
