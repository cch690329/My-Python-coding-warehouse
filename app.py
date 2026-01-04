import streamlit as st

# 設定網頁標題與圖標
st.set_page_config(page_title="梁社漢排骨 - 線上點餐", page_icon="🍱")

# 模擬菜單數據
menu = {
    "炸排骨飯": 115,
    "滷排骨飯": 115,
    "炸雞腿飯": 130,
    "黃金塔塔鱈魚堡": 95,
    "椒麻雞飯": 130
}

# --- 網頁介面設計 ---
st.title("🍱 梁社漢排骨 - 點餐系統")
st.markdown("---")

# 建立兩欄式佈局：左邊是菜單，右邊是購物車
col1, col2 = st.columns([2, 1])

with col1:
    st.header("主食菜單")
    order_list = {}
    
    # 動態產生菜單項目
    for item, price in menu.items():
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"### {item}")
            st.write(f"價格: ${price}")
        with c2:
            # 使用數值輸入框讓使用者選擇數量
            # count = st.number_input(f"數量 ({item})", min_value=0, max_value=10, key=item)
            count = st.selectbox(f"數量 ({item})", options=list(range(10)), key=item)
            if count > 0:
                order_list[item] = {"price": price, "count": count}
        st.write("---")

with col2:
    st.header("🛒 結帳清單")
    total_price = 0
    if not order_list:
        st.info("尚未選擇餐點")
    else:
        for item, info in order_list.items():
            subtotal = info["price"] * info["count"]
            total_price += subtotal
            st.write(f"**{item}** x {info['count']} = ${subtotal}")
        
        st.markdown("---")
        st.write(f"### 總計金額： **${total_price}**")
        
        if st.button("送出訂單", type="primary"):
            st.success("訂單已送達廚房，請稍候！")
            st.balloons()