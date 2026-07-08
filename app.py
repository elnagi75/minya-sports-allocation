import streamlit as st

# 1. إعدادات الصفحة العامة
st.set_page_config(
    page_title="منصة تسجيل الرغبات - جامعة المنيا",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تنسيق مخصص عبر CSS لضبط واجهة التصفح من اليمين إلى اليسار (RTL) والألوان الرسمية
st.markdown("""
    <style>
    /* ضبط محاذاة النصوص للحقول والقوائم */
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, h5, h6, label {
        text-align: right !important;
        direction: rtl !important;
    }
    /* تنسيق العنوان الرئيسي */
    .header-text {
        text-align: center !important;
        font-weight: bold;
        color: #1E3A8A;
        font-size: 22px;
        line-height: 1.6;
        direction: rtl;
    }
    /* تنسيق صندوق التعليمات الإرشادية */
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
    /* ضبط الصناديق الافتراضية للشعارات */
    .logo-placeholder {
        border: 2px dashed #CBD5E1;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
        color: #64748B;
        font-size: 14px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allowed_code=True)

# 3. الترويسة والشعارات (تقسيم الشاشة إلى 3 أعمدة متناسقة)
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    # مكان شعار الكلية (يسار الشاشة)
    st.markdown('<div class="logo-placeholder">مصر<br>[ مكان شعار كلية علوم الرياضة ]</div>', unsafe_allowed_code=True)
    # ملاحظة: لاحقاً سنستبدله بـ st.image("faculty_logo.png") بمجرد رفع الصورة

with col2:
    # عنوان المنصة الرسمي (منتصف الشاشة)
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
    # مكان شعار الجامعة (يمين الشاشة)
    st.markdown('<div class="logo-placeholder">جامعة المنيا<br>[ مكان شعار جامعة المنيا ]</div>', unsafe_allowed_code=True)
    # ملاحظة: لاحقاً سنستبدله بـ st.image("university_logo.png") بمجرد رفع الصورة

st.markdown("<br><hr>", unsafe_allowed_code=True)

# 4. صندوق التعليمات الإرشادية الملزم للطلاب
st.markdown("""
<div class="instructions-box">
    <h4 style="color: #DC2626; margin-top: 0; font-weight: bold;">⚠️ تنبيه وإرشادات هامة جداً للطلاب قبل التسجيل:</h4>
    <ol>
        <li><b>التسجيل لمرة واحدة فقط:</b> يُسمح لكل طالب بتسجيل رغباته <b>مرة واحدة فقط</b> باستخدام الرقم القومي الخاص به. بمجرد الضغط على زر الحفظ النهائي، سيتم قفل الحساب تلقائياً ولن يُسمح لك بالدخول أو التعديل تحت أي ظرف.</li>
        <li><b>الرقم القومي:</b> يجب كتابة الرقم القومي كاملاً (14 رقماً باللغة الإنجليزية) بدقة تامة. أي خطأ في الرقم القومي يتحمل الطالب مسؤوليته الكاملة.</li>
        <li><b>مجموع الدرجات:</b> يُكتب مجموع درجاتك <b>بالأرقام فقط</b> كما هو معلن في النتائج الرسمية (مثال: 1350)، ويُحظر تماماً كتابة نصوص أو علامات النسبة المئوية (%).</li>
        <li><b>منع تكرار الرغبات:</b> المنصة مصممة برمجياً لمنع تكرار اختيار التخصص؛ بمجرد اختيارك لتخصص معين في الرغبة الأولى، سيختفي تلقائياً من خيارات الرغبة الثانية، وهكذا. لذا يرجى ترتيب رغباتك الخمس بعناية شديدة وفقاً لأولوياتك الفعلية.</li>
        <li><b>رقم الواتساب:</b> يجب إدخال رقم هاتف محمول صحيح ومكون من 11 رقماً (مفعّل عليه خدمة الواتساب) لضمان إمكانية التواصل الرسمي معك.</li>
    </ol>
</div>
""", unsafe_allowed_code=True)
