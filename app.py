import streamlit as st

# 1. إعدادات الصفحة العامة
st.set_page_config(
    page_title="منصة تسجيل الرغبات - جامعة المنيا",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تنسيق مخصص عبر CSS لضبط واجهة التصفح
st.markdown("""
    <style>
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, h5, h6, label {
        text-align: right !important;
        direction: rtl !important;
    }
    .header-text {
        text-align: center !important;
        font-weight: bold;
        color: #1E3A8A;
        font-size: 22px;
        line-height: 1.6;
        direction: rtl;
    }
    .instructions-box {
        background-color: #F8FAFC;
        border-right: 6px solid #1E3A8A;
        padding: 22px;
        border-radius: 8px;
        margin-top: 20px;
        margin-bottom: 25px;
        direction: rtl;
        text-align: right;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .instructions-box li {
        margin-bottom: 10px;
        font-size: 15px;
    }
    .logo-placeholder {
        border: 2px dashed #CBD5E1;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
        color: #64748B;
        font-size: 14px;
        margin-top: 15px;
    }
    /* تنسيق زر الإرسال ليكون بارزاً */
    div.stButton > button:first-child {
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        font-size: 18px;
        width: 100%;
        padding: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allowed_code=True)

# 3. الترويسة والشعارات
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.markdown('<div class="logo-placeholder">مصر<br>[ مكان شعار كلية علوم الرياضة ]</div>', unsafe_allowed_code=True)

with col2:
    st.markdown('''
        <div class="header-text">
            جامعة المنيا - كلية علوم الرياضة<br>
            قسم الرياضات الجماعية وألعاب المضرب<br>
            <span style="color: #2563EB; font-size: 20px;">
            منصة تسجيل رغبات التخصصات لطلاب الفرقة الرابعة للعام الجامعي 2026/2025
            </span>
        </div>
    ''', unsafe_allowed_code=True)

with col3:
    st.markdown('<div class="logo-placeholder">جامعة المنيا<br>[ مكان شعار جامعة المنيا ]</div>', unsafe_allowed_code=True)

st.markdown("<br><hr>", unsafe_allowed_code=True)

# 4. صندوق التعليمات الإرشادية
st.markdown("""
<div class="instructions-box">
    <h4 style="color: #DC2626; margin-top: 0; font-weight: bold;">⚠️ تنبيه وإرشادات هامة جداً للطلاب قبل التسجيل:</h4>
    <ol>
        <li><b>التسجيل لمرة واحدة فقط:</b> يُسمح لكل طالب بتسجيل رغباته <b>مرة واحدة فقط</b> باستخدام الرقم القومي الخاص به. بمجرد الضغط على زر الحفظ النهائي، سيتم قفل الحساب تلقائياً.</li>
        <li><b>الرقم القومي:</b> يجب كتابة الرقم القومي كاملاً (14 رقماً باللغة الإنجليزية) بدقة تامة.</li>
        <li><b>مجموع الدرجات:</b> يُكتب مجموع درجاتك <b>بالأرقام فقط</b> كما هو معلن في النتائج الرسمية (مثال: 1350)، ويُحظر تماماً كتابة نصوص أو علامات النسبة المئوية (%).</li>
        <li><b>منع تكرار الرغبات:</b> المنصة مصممة برمجياً لمنع تكرار اختيار التخصص؛ بمجرد اختيارك لتخصص معين في الرغبة الأولى، سيختفي تلقائياً من خيارات الرغبة الثانية، وهكذا.</li>
        <li><b>رقم الواتساب:</b> يجب إدخال رقم هاتف محمول صحيح ومكون من 11 رقماً (مفعّل عليه خدمة الواتساب).</li>
    </ol>
</div>
""", unsafe_allowed_code=True)

# 5. القسم الأول: البيانات الأساسية
st.markdown('<h3 style="color: #1E3A8A;">أولاً: البيانات الأساسية</h3>', unsafe_allowed_code=True)

col_a, col_b = st.columns(2)
with col_a:
    name = st.text_input("الاسم الرباعي:")
    national_id = st.text_input("الرقم القومي (14 رقماً):", max_chars=14)
with col_b:
    score = st.text_input("مجموع الدرجات بالأرقام (بدون أي علامات):")
    whatsapp = st.text_input("رقم هاتف الواتساب (11 رقماً):", max_chars=11)

st.markdown("<hr>", unsafe_allowed_code=True)

# 6. القسم الثاني: الرغبات (الديناميكية المترابطة)
st.markdown('<h3 style="color: #1E3A8A;">ثانياً: ترتيب الرغبات التخصصية</h3>', unsafe_allowed_code=True)
st.info("💡 قم باختيار الرغبة الأولى لتفعيل باقي الرغبات. لاحظ أنه لا يمكن اختيار نفس التخصص مرتين.")

# قائمة التخصصات
all_sports = ["كرة القدم", "الكرة الطائرة", "كرة السلة", "كرة اليد", "ألعاب المضرب"]

# الرغبة الأولى
pref1 = st.selectbox("الرغبة الأولى:", ["اختر التخصص..."] + all_sports)

# الرغبة الثانية (تستبعد اختيار الرغبة الأولى وتظل مغلقة حتى يختار الطالب الرغبة الأولى)
options2 = ["اختر التخصص..."] + [s for s in all_sports if s != pref1]
pref2 = st.selectbox("الرغبة الثانية:", options2, disabled=(pref1 == "اختر التخصص..."))

# الرغبة الثالثة (تستبعد 1 و 2)
options3 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2]]
pref3 = st.selectbox("الرغبة الثالثة:", options3, disabled=(pref2 == "اختر التخصص..."))

# الرغبة الرابعة (تستبعد 1 و 2 و 3)
options4 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2, pref3]]
pref4 = st.selectbox("الرغبة الرابعة:", options4, disabled=(pref3 == "اختر التخصص..."))

# الرغبة الخامسة (تستبعد 1 و 2 و 3 و 4)
options5 = ["اختر التخصص..."] + [s for s in all_sports if s not in [pref1, pref2, pref3, pref4]]
pref5 = st.selectbox("الرغبة الخامسة والأخيرة:", options5, disabled=(pref4 == "اختر التخصص..."))

st.markdown("<br>", unsafe_allowed_code=True)

# 7. زر الإرسال واعتماد الرغبات
submit_btn = st.button("إرسال واعتماد الرغبات نهائياً")

if submit_btn:
    st.success("✅ الواجهة تعمل بنجاح! هذه رسالة تجريبية، سيتم برمجة حفظ البيانات لمنع التكرار في الخطوة القادمة.")
