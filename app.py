import streamlit as st
from engine import load_state, save_state, update_state
from planner import get_plan
from nutrition import get_meals
import datetime

st.set_page_config(page_title="AI健身系统", layout="wide")

st.title("🔥 AI健身教练系统（Clean V1）")

state = load_state()

plan = get_plan()
meals = get_meals(state)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("体重", f"{state['weight']} kg")

with col2:
    st.metric("疲劳", state["fatigue"])

with col3:
    st.metric("恢复", state["recovery"])

st.divider()

st.subheader("🏋️ 今日训练")
st.success(plan)

st.subheader("🍽 今日饮食")
st.info(meals)

st.divider()

if st.button("✅ 完成训练"):
    state = update_state(state, "train")
    save_state(state)
    st.success("已记录训练🔥")

if st.button("🛌 休息一天"):
    state = update_state(state, "rest")
    save_state(state)
    st.warning("已进入恢复模式")
