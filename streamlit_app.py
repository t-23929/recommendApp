import streamlit as st
import pandas as pd

# 仮データ
data = pd.DataFrame({
    "foodbank_name": ["あおぞらフードバンク", "ひまわり食堂"],
    "address": ["東京都渋谷区", "東京都杉並区"],
    "needs": [["お米", "缶詰"], ["ミルク", "離乳食"]]
})

st.title("商品に応じたフードバンク推薦")

# 入力フォーム
user_item = st.text_input("寄付したい商品を入力してください（例：お米）")

if user_item:
    matched = data[data["needs"].apply(lambda x: user_item in x)]
    if not matched.empty:
        st.markdown("### この商品を必要としているフードバンク")
        st.dataframe(matched[["foodbank_name", "address"]])
    else:
        st.write("この商品を必要としているフードバンクは見つかりませんでした。")
