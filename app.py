import os
from dotenv import load_dotenv
load_dotenv()  # .env から OPENAI_API_KEY を読み込み

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# OpenAI APIキーは環境変数 OPENAI_API_KEY から自動取得されます
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

st.title("専門家を選択して、質問に回答するアプリ")

st.write("##### 世界旅行の専門家: 国を指定して、その国の観光地を教えてくれます。")
st.write("##### 日本国内旅行の専門家: 地域を指定して、その地域の観光地を教えてくれます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["世界旅行の専門家", "日本国内旅行の専門家"]
)

st.divider()

if selected_item == "世界旅行の専門家":
    input_message = st.text_input("国名を入力してください。")
else:
    input_message = st.text_input("地域名を入力してください。")

if st.button("実行"):
    st.divider()
    if not input_message:
        st.error("入力してから「実行」ボタンを押してください。")
    else:
        st.write(f"{'国名' if selected_item=='世界旅行の専門家' else '地域名'}: **{input_message}**")
        # メッセージ生成
        system_prompt = (
            "You are a World Travel Expert."
            if selected_item == "世界旅行の専門家"
            else "You are an expert in domestic travel in Japan."
        )
        user_prompt = (
            f"世界旅行の専門家として、{input_message}の観光地を教えてください。"
            if selected_item == "世界旅行の専門家"
            else f"日本国内旅行の専門家として、{input_message}の観光地を教えてください。"
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]
        # 回答生成
        result = llm(messages)
        st.write(f"##### 回答:\n{result.content}")