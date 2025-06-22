
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st
import os


#セット　OPENAI モデル
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


st.title("専門家を選択して、質問に回答するアプリ")

st.write("##### 世界旅行の専門家: 国を指定して、その国の観光地を教えてくれます。")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで回答を受け取れます。")
st.write("##### 日本国内旅行の専門家: 地域を指定して、その地域の観光地を教えてくれます。")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで回答を受け取れます。。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["世界旅行の専門家", "日本国内旅行の専門家"]
)

st.divider()

if selected_item == "世界旅行の専門家":
    input_message = st.text_input(label="国名を入力してください。")

else:
    input_message = st.text_input(label="地域名を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "世界旅行の専門家":
        if input_message:
            st.write(f"国名: **{input_message}**")

            #メッセージ生成
            messages = [
                SystemMessage(content="You are a World Travel Expert."),
                HumanMessage(content=f"世界旅行の専門家として、{input_message}の観光地を教えてください。")]
            #回答生成
            result = llm(messages)
            st.write(f"##### 回答: {result}")
        else:
            st.error("国名を入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(f"地域名: **{input_message}**")

            #メッセージ生成
            messages = [
                SystemMessage(content="You are an expert in domestic travel in Japan"),
                HumanMessage(content=f"日本国内旅行の専門家として、{input_message}の観光地を教えてください。")]
            #回答生成
            result = llm(messages)
            st.write(f"##### 回答: {result}")
        else:
            st.error("地域名を入力してから「実行」ボタンを押してください。")
