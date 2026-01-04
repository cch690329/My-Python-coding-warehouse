import streamlit as st

# 1. 設定網頁分頁資訊
st.set_page_config(page_title="我的最愛排骨飯 - 線上點餐", page_icon="🍱", layout="wide")

# 2. 注入自定義 CSS 樣式 (調整顏色)
st.markdown("""
    <style>
    /* 調整網頁主背景顏色 */
    .stApp {
        background-color: #F5F5F0; /* 輕微的米白色，增加質感 */
    }

    /* 調整標題顏色 (深綠色) */
    h1, h2, h3 {
        color: #1B4D3E !important;
    }

    /* 調整側邊欄或按鈕的品牌色 */
    .stButton>button {
        background-color: #1B4D3E;
        color: white;
        border-radius: 5px;
        border: none;
    }

    /* 滑鼠移過按鈕時的顏色 (金色/木質感) */
    .stButton>button:hover {
        background-color: #D4AF37;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 顯示品牌 Logo
# 你可以換成你自己的圖片路徑，例如：st.image("logo.png")
logo_url = "https://www.buygood.com.tw/images/logo.png"  # 範例網址
st.image(logo_url, width=200)

# 模擬菜單數據
menu = {
    "炸排骨飯": 115,
    "滷排骨飯": 115,
    "炸雞腿飯": 130,
    "黃金塔塔鱈魚堡": 95,
    "椒麻雞飯": 130
}

# --- 網頁介面設計 ---
st.title("🍱 專業排骨・兩岸馳名")
st.subheader("歡迎使用線上點餐系統")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("✨ 精選主食")
    order_list = {}

    for item, price in menu.items():
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"### {item}")
            st.write(f"價格: **${price}**")
        with c2:
            count = st.selectbox(f"數量", options=list(range(11)), key=item)
            if count > 0:
                order_list[item] = {"price": price, "count": count}
        st.write("---")

with col2:
    # 使用 st.info 建立一個美觀的區塊
    with st.container():
        st.header("🛒 我的購物車")
        total_price = 0
        if not order_list:
            st.write("目前購物車空空如也...")
        else:
            for item, info in order_list.items():
                subtotal = info["price"] * info["count"]
                total_price += subtotal
                st.write(f"**{item}** x {info['count']} = `${subtotal}`")

            st.markdown("---")
            st.write(f"## 總計金額： :green[${total_price}]")

            if st.button("確認下單", use_container_width=True):
                st.success("訂單已送達！請至櫃檯結帳取餐。")
                st.balloons()

# 頁尾資訊
st.markdown("---")
st.caption("我最愛的排骨飯模擬點餐系統_2026")