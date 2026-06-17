import datetime

def get_plan():

    weekday = datetime.datetime.now().weekday()

    plans = [
        "胸 + 三头（卧推/夹胸/俯卧撑）",
        "背 + 二头（下拉/划船/哑铃）",
        "腿 + 核心（倒蹬/卷腹/深蹲）",
        "肩 + 手臂（推举/侧平举）",
        "全身轻训练 + 有氧",
        "燃脂训练 + 跑步",
        "恢复 + 拉伸"
    ]

    return plans[weekday]
