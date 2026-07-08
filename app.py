import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة تسجيل الرغبات - جامعة المنيا", layout="wide", initial_sidebar_state="collapsed")

# 2. تعريف مسار ملف حفظ البيانات (تم تغييره لإنشاء ملف جديد بالتنسيق العربي)
DATA_FILE = "students_data_final.csv"

# الأعمدة المطابقة تماماً لملف الإكسيل الخاص بالقسم
COLUMNS = [
    "م", 
    "طابع زمني", 
    "الاسم رباعي", 
    "الرقم القومي", 
    "مجموع درجات بالأرقام (بدون نسب مئؤية)", 
    "رقم هاتف الواتساب", 
    "(1) الرغبة الأولى:", 
    "(2) الرغبة الثانية:", 
    "(3) الرغبة الثالثة:", 
    "(4) الرغبة الرابعة:", 
    "(5) الرغبة الخامسة والأخيرة:"
]

def init_db():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')

init_db()

# 3. تنسيق مخصص عبر CSS
st.markdown("""
    <style>
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, h5, h6, label {
        text-align: right !important;
        direction: rtl !important;
    }
    .header-text { text-align: center !important; font-weight: bold; color: #1E3A8A; font-size: 22px; line-height: 1.6; direction: rtl; }
    .instructions-box { background-color: #F8FAFC; border-right: 6px solid #1E3A8A; padding: 22px; border-radius: 8px; margin-top: 20px; margin-bottom: 25px; direction: rtl; text-align: right; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .instructions-box li { margin-bottom: 10px; font-size: 15px; }
    .logo-placeholder { border: 2px dashed #CBD5E1; padding: 20px; text-align: center; border-radius: 8px; color: #64748B; font-size: 14px; margin-top: 15px; }
    div.stButton > button:first-child { background-color: #1E3A8A; color: white; font-weight: bold; font-size: 18px; width: 100%; padding: 10px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية للإدارة ---
st.sidebar.markdown("<h3 style='text-align: right; direction: rtl;'>لوحة تحكم الإدارة</h3>", unsafe_allow_html=True)
admin_pass = st.sidebar.text_input("أدخل كلمة المرور:", type="password", key="admin_pass")

if admin_pass == "admin2026":
    st.sidebar.success("✅ تم تسجيل الدخول للإدارة")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as file:
            st.sidebar.download_button(
                label="📥 تحميل بيانات الطلاب (Excel/CSV)",
                data=file,
                file_name="البيانات_النهائية_لتنسيق_الطلاب.csv",
                mime="text/csv"
            )
# --------------------------------

# 4. الترويسة والشعارات
col1, col2, col3 = st.columns([1, 3, 1])
with col1: 
    if os.path.exists("fac_logo.png"): st.image("fac_logo.png", use_container_width=True)
    else: st.markdown('<div class="logo-placeholder">مصر<br>[ مكان شعار كلية علوم الرياضة ]</div>', unsafe_allow_html=True)

with col2:
    st.markdown('''
        <div class="header-text">جامعة المنيا - كلية علوم الرياضة<br>قسم الرياضات الجماعية وألعاب المضرب<br>
        <span style="color: #2563EB; font-size: 20px;">منصة تسجيل رغبات التخصصات لطلاب الفرقة الرابعة للعام الجامعي 2026/2025</span></div>
    ''', unsafe_allow_html=True)

with col3: 
    if os.path.exists("uni_logo.png"): st.image("uni_logo.png", use_container_width=True)
    else: st.markdown('<div class="logo-placeholder">جامعة المنيا<br>[ مكان شعار جامعة المنيا ]</div>', unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

# 5. صندوق التعليمات الإرشادية
st.markdown("""
<div class="instructions-box">
    <h4 style="color: #DC2626; margin-top: 0; font-weight: bold;">⚠️ تنبيه وإرشادات هامة جداً للطلاب قبل التسجيل:</h4>
    <ol>
        <li><b>التسجيل لمرة واحدة فقط:</b> يُسمح لكل طالب بتسجيل رغباته <b>مرة واحدة فقط</b> باستخدام الرقم القومي الخاص به.</li>
        <li><b>الرقم القومي:</b> يجب كتابة الرقم القومي كاملاً (14 رقماً باللغة الإنجليزية) بدقة تامة.</li>
        <li><b>مجموع الدرجات:</b> يُكتب مجموع درجاتك <b>بالأرقام فقط</b> (مثال: 1350)، ويُحظر تماماً كتابة نصوص أو علامات النسبة المئوية (%).</li>
        <li><b>منع تكرار الرغبات:</b> المنصة مصممة برمجياً لمنع تكرار اختيار التخصص.</li>
        <li><b>رقم الواتساب:</b> يجب إدخال رقم هاتف محمول صحيح ومكون من 11 رقماً.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# 6. القسم الأول: البيانات الأساسية
st.markdown('<h3 style="color: #1E3A8A;">أولاً: البيانات الأساسية</h3>', unsafe_allow_html=True)
col_left, col_right = st.columns(2)
with col_right:
    name = st.text_input("الاسم الرباعي:")
    national_id = st.text_input("الرقم القومي (14 رقماً):", max_chars=14)
with col_left:
    score = st.text_input("مجموع الدرجات بالأرقام (بدون أي علامات):")
    whatsapp = st.text_input("رقم هاتف الواتساب (11 رقماً):", max_chars=11)

st.markdown("<hr>", unsafe_allow_html=True)

# 7. القسم الثاني: الرغبات
st.markdown('<h3 style="color: #1E3A8A;">ثانياً: ترتيب الرغبات التخصصية</h3>', unsafe_allow_html=True)
st.info("💡 قم باختيار الرغبة الأولى لتفعيل باقي الرغبات. لا يمكن اختيار نفس التخصص مرتين.")
all_sports = ["كرة القدم", "الكرة الطائرة", "كرة السلة", "كرة اليد", "ألعاب المضرب"]

pref1 = st.selectbox("الرغبة الأولى:", ["اختر التخصص..."] + all_sports)
options2 = ["اختر التخصص..."] + [s for s in all_sports if s != pref1]
pref2 = st.selectbox("الرغبة الثانية:", options2, disabled=(pref1 == "اختر التخصص..."))
options3 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2]]
pref3 = st.selectbox("الرغبة الثالثة:", options3, disabled=(pref2 == "اختر التخصص..."))
options4 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2, pref3]]
pref4 = st.selectbox("الرغبة الرابعة:", options4, disabled=(pref3 == "اختر التخصص..."))
options5 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2, pref3, pref4]]
pref5 = st.selectbox("الرغبة الخامسة والأخيرة:", options5, disabled=(pref4 == "اختر التخصص..."))
st.markdown("<br>", unsafe_allow_html=True)

# 8. زر الإرسال وبرمجة الحفظ
submit_btn = st.button("إرسال واعتماد الرغبات نهائياً")

if submit_btn:
    if not name or not national_id or not score or not whatsapp or pref1 == "اختر التخصص..." or pref5 == "اختر التخصص...":
        st.error("❌ يرجى استكمال جميع البيانات وتحديد الرغبات الخمس قبل الإرسال.")
    elif len(national_id) != 14 or not national_id.isdigit():
        st.error("❌ عذراً.. الرقم القومي يجب أن يتكون من 14 رقماً صحيحاً.")
    elif len(whatsapp) != 11 or not whatsapp.isdigit():
        st.error("❌ عذراً.. رقم الواتساب يجب أن يتكون من 11 رقماً صحيحاً.")
    else:
        df = pd.read_csv(DATA_FILE)
        if str(national_id) in df["الرقم القومي"].astype(str).values:
            st.error(f"⚠️ عذراً يا {name}! تم تسجيل رغباتك مسبقاً بهذا الرقم القومي، ولا يُسمح بالتسجيل أكثر من مرة.")
        else:
            # ترتيب الأعمدة وتوليد رقم المسلسل تلقائياً
            serial_number = len(df) + 1
            new_data = pd.DataFrame([{
                "م": serial_number,
                "طابع زمني": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "الاسم رباعي": name,
                "الرقم القومي": str(national_id),
                "مجموع درجات بالأرقام (بدون نسب مئؤية)": score,
                "رقم هاتف الواتساب": str(whatsapp),
                "(1) الرغبة الأولى:": pref1,
                "(2) الرغبة الثانية:": pref2,
                "(3) الرغبة الثالثة:": pref3,
                "(4) الرغبة الرابعة:": pref4,
                "(5) الرغبة الخامسة والأخيرة:": pref5
            }])
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')
            st.success(f"✅ تم حفظ رغباتك بنجاح واعتمادها يا {name}. نتمنى لك التوفيق!")
