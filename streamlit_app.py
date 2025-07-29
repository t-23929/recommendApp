import streamlit as st
import pandas as pd

# 仮データ
data = pd.read_csv("data.csv")

data["needs"] = data["needs"].apply(lambda x: [item.strip() for item in x.split(",")])

st.title("商品に応じたフードバンク推薦")

# 入力フォーム
user_item = st.text_input("寄付したい商品を入力してください（例：お米）")

if user_item:
    matched = data[data["needs"].apply(lambda need_list: any(user_item in item for item in need_list))]
    
    if not matched.empty:
        st.markdown("### この商品を必要としているフードバンク")
        st.dataframe(matched[["foodbank_name", "address"]])
    else:
        st.warning("この商品を必要としているフードバンクは見つかりませんでした。")
