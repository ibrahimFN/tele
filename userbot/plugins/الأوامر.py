from userbot import iqthon

from ..core.managers import edit_or_reply

plugin_category = "الأوامر"


@iqthon.iq_cmd(
    pattern="جميع الاوامر$",
    command=("جميع الاوامر", plugin_category),
    info={
        "header": "جميع الاوامر",
        "usage": "جميع الاوامر",
    },
)
async def _(event):
    "جميع الاوامر"
    await edit_or_reply(
        event,
        "**• ⚜️ |  جميع الاوامر :**  \n\n.مسح جميع الردود\n.مسح رد\n.جميع الردود\n.اضف رد\n.صورة\n.رفع مشرف\n.تك\n.طرد\n.تثبيت\n.الغاء التثبيت\n.الاحداث\n.حظر\n.الغاء حظر\n.كتم\n.الغاء كتم\n.الاوامر\n.جميع الاوامر\n.الايدي\n.بنك\n.ترحيب\n.مسح الترحيبات\n.الترحيبات\n.رساله الترحيب السابقه\n.السورس\n.انتحال\n.الغاء الانتحال\n .بوسه\n.زرفه\n.بيبي\n.افكر\n.ضحك\n.ضايج\n.وقت\n.قلوب\n.رياضه\n.الارض\n.قمر\n.اقمار\n.قمور\n.فراشه\n.مكعبات\n.مطر\n.تحركات\n.ايموجيات\n.طائره\n.شرطه\n.النضام الشمسي\n.عين\n.ثعبان\n.رجل\n.مايكرو\n.رموزشيطانيه\n.قطار\n.موسيقى\n.رسم\n.تحميلات\n.اشكال مربع\n.دائره\n.قلب\n.مزاج\n.قرد\n.يد\n.العد التنازلي\n.الوان قلوب\n.غبي\n.تفجير\n.قتل\n.شنو\n.طوبه\n.مربعات\n.حلويات\n.نار\n.وضع بايو\n.وضع اسم\n.وضع صورة\n.وضع معرف\n.الحساب\n.حذف صوره\n.انشائي\n.تكرار\n.تكرار الملصق\n.تكرار بالحرف\n.تكرار بالكلمه\n.مؤقت\n.تليجراف ( ميديا او كتابه )\n.تحميل ص\n.تحميل ف\n.نتائج بحث + اسم الاغنيه\n.انستا\n.بحث + اسم الاغنيه\n.بحث فيديو\n.معلومات الاغنيه \n.اعاده تشغيل\n.اطفاء تليثون\n.اطفاء مؤقت +الوقت\n.التحديثات \n.المشرفين\n.البوتات\n.الأعضاء\n.معلومات\n.موقع \n .الحماية تشغيل\n.الحماية ايقاف \n.قبول - رفض ( للحماية) \n .مرفوض ( حظر من الخاص)\n.المقبولين ( عرض قائمة المقبولين في الحماية ) \n .الاذان\n.كورونا + اسم الدوله بالانكليزي\n.ايدي + رد على الشخص\n.صنع مجموعه خارقه او قناه + الاسم\n.الوقت - لضهور تاريخ والوقت\n.وقتي - لضهور تاريخ والوقت بملصق \n.تنظيف + الرد على الرساله ينضف مافي تحتها\n.حذف + رد على رساله يمسح الرساله\n.تنظيف رسائلي + عدد\n.اسم وقتي\n.نبذه وقتيه\n.صوره وقتيه\n.ايقاف اسم وقتي\n.ايقاف نبذه وقتيه\n.ايقاف صوره وقتيه \n `.ازعاج `\n `.الغاء الازعاج` \n `.مسح الازعاج`\n`.المزعجهم`\n `.ترجمه ar` ( من نكليزي الى عربي )\n `.ترجمه en` ( من عربي الى نكليزي ) \n `.تكلم en`  ( ترجمه صوتيه تحويل من عربي الى الانكلش )\n`.تكلم ar` ( ترجمه صوتيه تحويل من نكلش الى عربي )  \n `.المنع تشغيل` \n `.المنع ايقاف` -  ( لأيقاف وتشغيل مسح كلمات الممنوعه)\n`.منع +  الكلمة او الرد على الكلمة`\n `.الغاء منع + كلمة او الرد على الكلمة` \n⌔︙ `.قفل الدردشه`\n⌔︙` .قفل الوسائط`\n⌔︙` .قفل الملصقات`\n⌔︙` .قفل الروابط`\n⌔︙ `.قفل المتحركة`\n⌔︙` .قفل الالعاب`\n⌔︙` .قفل  الانلاين`\n⌔︙ `.قفل التصويت`\n⌔︙ `.قفل الاضافة`\n⌔︙ `.قفل التثبيت`\n⌔︙ `.قفل الكل`\n⌔︙ `.فتح +`  الصلاحية\n⌔︙`.الصلاحيات`   ( لأضهار صلاحيات مجموعة )\n⌔︙` .تحويل صورة ` ( لتحويل ملصق الى صوره)\n⌔︙ `.تحويل ملصق`  ( لتحويل صوره الى ملصق)\n⌔︙ `.تحويل صوت`  ( لتحويل البصمه الى mp3)\n⌔︙`.مغادره`\n⌔︙`.مسح المحضورين`\n⌔︙`.المحذوفين`\n⌔︙`.المحذوفين تنظيف`\n⌔︙`.احصائيات الاعضاء`\n⌔︙`.اضف فار`\n⌔︙`.حذف فار`\n⌔︙`.جلب فار`\n⌔︙`.احصائيات حسابي`\n⌔︙`.الصور جميعها` ( الرد على الشخص )\n⌔︙`الصوره + رقم صوره`\n⌔︙`.رابط الحساب`  ( الرد على الشخص )\n⌔︙`.سرعه الانترنيت`\n⌔︙`.تهكير`\n⌔︙ .تحويل فديو دائري  ⬇️\n( الرد على ملصق لتحويلة الى مرئيه دائرية ) \n⌔︙ .تحويل ملصق دائري  ⬇️\n ( الرد على ملصق لتحويلة الى ملصق دائري )\n⌔︙ .تحويل صوره ⬇️\n( الرد على ملصق لتحويلة الى صورة )\n⌔︙ .تحويل ملف + اسم ملف ⬇️\n( الرد على كتابه لتحويلها الى ملف بالاسم تريده )\n⌔︙ .تحويل رساله ⬇️\n( الرد على ملف لتحويله الى الكتابه التي بداخله )\n⌔︙ .تحويل ملف صوره ⬇️\n( الرد على ملف صوره لتحويله الى صوره حقيقه )\n⌔︙ .تحويل ملصق متحرك ⬇️\n( الرد على ملصقه متحركه تحويلها الى متحركه )\n⌔︙ .تحويل متحركه ⬇️\n( الرد على ملصق او صوره لتحويلها الى متحركه ) \n⌔︙ .تحويل فديو متحركه ⬇️\n( لتحويل الفديو الى متحركه )\n⌔︙ .احسب + المسئلة ⬇️\n( كمثال : .احسب 99+99 )\n⌔︙ .رسم شعار + الكلمة \n⌔︙ .رسم قلوب + الكلمة\n⌔︙ .وضع النائم ⬇️\n ( فقد ارسله بالخاص مالك اي شخص يرد عليك او يسويلك تاك يكله حاليا غير متواجد بس اذا راسلت بتليجرام تلقائيا ينلغي الوضع )\n⌔︙ `.اضف ترحيب خاص`   ⬇️ \nشرح : ترحيب اي شخص يدخل للكروب ترسله ترحيب بخاصه  \n⌔︙ `.مسح ترحيب خاص`\n⌔︙` .لسته ترحيب خاص  `\n⌔︙ `.جلب لقطات + عدد لقطات`  ⬇️\n شرح :  الرد على فيديو لجلب لقطات من الفديو مع العدد محدد  \n⌔︙` .ازاله التوجيه` ⬇️\nشرح : الرد على بصمه موجة او أي شئ يقوم بازالة توجيها  \n⌔︙ `.البحث اونلاين + الاسم`  ⬇️\nشرح : يرسل اليك صوره باسم البحث خاص بك مع رابط بحث \n⌔︙ `.البحث العام + الاسم ` ⬇️\nشرح : الرد على صوره او فيديو لجلب الاشياء التي تتعلق بة  \n⌔︙ `.كوكل بحث + الاسم` ⬇️\nشرح :  لأضهار جميع البحوثات التي تتعلق بة \n⌔︙` .تثبيت ملف` ⤵️\n( الرد على ملف تليثون بالأمر لتثبيتة) \n⌔︙ `.تثبيت ثانوي ` ⤵️\n( لأضافه نفـس أسم الملف الـذي أضفتة بتحديث اضافاتك ) \n⌔︙ `.حذف التثبيت + اسم ملف`  ⤵️\n(  ضع اسم الملف بجانب الامر لحذفه )  \n⌔︙ `.حذف جميع الملفات ` ⤵️\n( تنبية ⚠️ يقوم بحذف جميع ملفات تنصيبك) \n⌔︙ `.معلومات تنصيبي  `⤵️\n(  يجـلب جميع المعلومات والفـارات ومعلومات تنصيبك) \n⌔︙ `.تاريخ الرسالة ` ⤵️\n( الرد على الـرسالة لجـلب تـاريخ أرسالها و الوقت ) \n⌔︙ `.معلومات تخزين المجموعه ` ⤵️\n( لعرض معلومات مجموعتك عدد رسائل وصور وتخزين ) \n⌔︙ `.نص ثري دي + كلمة ` ⤵️\n( لتحويل الكلـمة الـى شعار او نص ثلاثي ابعاد )\n⌔︙ `.تاك للكل` ⤵️\n( يسوي تاك لكل الاشخاص بلكروب وبلقناه )\n⌔︙` .الكل` ⤵️\n( يسوي تاك لكل الاشخاص بلكروب وبلقناه ) \n⌔︙` .ابلاغ الادمنيه `⤵️\n( اي شخص مسوي ازعاج او تفليش مجرد دز الامر يسوي تاك لكل الادمنيه ويبلغهم) \n⌔︙ `.تاك بالكلام + معرف الشخص + الكلام  ` ⤵️\n( يدمج الرابط ويه الكلام مالك ويسوي تاك للشخص يعني يصير كلام بالرابط تاك)  \n⌔︙` .ماركدون `⤵️\n(يقوم بصنع ماركدون شفافيه لديك)  \n⌔︙` .تحذير تكرار + العدد `⤵️\n( يحذر الشخص بلكروب اي شخص يكرر يحذره ويسويله تاك حسب العدد الي محدده واذا كثر فدنوب تكرار يقيدة)  \n⌔︙` .رابط تطبيق + اسم تطبيق` ⤵️\n( يطلعلك رابط تطبيق ومعلوماته من سوق بلي) \n⌔︙`.مؤقته + الرساله + عدد الثواني` ⤵️\n( رساله وقتيه بس يخلص وقت الي محدده تنحذف رسالة )\n⌔︙` .تحويل ملكية + معرف شخص `⤵️\n( تنشره الامر بقناتك او بكروبك الي تريد تحوله لازم رافعه مشرف ومفعل تحقق بخطوتين )\n⌔︙` .وقتيه + عدد الثواني + الرساله `⤵️\n( رساله وقتيه تحدد الثواني مثل 10 ثواني بس تخلص يدز الرساله للشخص او للكروب)\n⌔︙ `.كود بالرابط + الرد على الكود`  ⤵️\n(  txt يخليلك كود بالرابط من تدخله تشوف كود ) \n⌔︙ `.سجل الاسماء + الرد على شخص ` ⤵️\n ( يطيك الاسماء القديمه للشخص) \n⌔︙ `.دعوه + معرفة ` ⤵️\n( اضافه شخص للكروب )  \n⌔︙ `.رابط التنصيب ` ⤵️\n( يطيك رابط تنصيب سورسنه) \n⌔︙ `.حساب كيثاب + اسم كيثاب`  ⤵️\n( يطيك جميع معلومات الكيثاب الي كتبته و كلشي عليه للمطورين )  \n⌔︙ `.بحوثات كوكل + الاسم `⤵️\n ( يطلعلك بحوثات عن الاسم بكوكل) \n⌔︙ `.بحوثات يوتيوب + الاسم `⤵️\n( يطلعلك بحوثات عن الاسم بل يوتيوب )\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",

    )

@iqthon.iq_cmd(
    pattern="الاوامر$",
    command=("الاوامر", plugin_category),
    info={
        "header": "الاوامر",
        "usage": "الاوامر",
    },
)
async def _(event):
    "الاوامر"
    await edit_or_reply(
        event,
          "**• ⚜️ | لـ اوامر الادمن والمجموعه  :\n **  أرسل ~ ( `.م1 ` ) \n  **• ⚜️ | لـ اوامر متحركات تسلية  :\n **  أرسل ~ ( `.م2 ` )\n**• ⚜️ | لـ اوامر تغير حساب شخصي :\n **  أرسل ~ ( `.م3 ` )\n**• ⚜️ | لـ اوامر تكرار رسائل  وتليجراف :\n **  أرسل ~ ( `.م4 ` )\n**• ⚜️ | لـ اوامر تحميل من مواقع تواصل :\n **  أرسل ~ ( `.م5 ` )\n**• ⚜️ | لـ أوامر اعاده التشغيل والاطفاء :\n **  أرسل ~ ( `.م6 ` )\n**• ⚜️ | لـ اوامر الخاصة بلمجموعه :\n **  أرسل ~ ( `.م7 ` )\n**• ⚜️ | لـ اوامر رساله الحماية الخاص  :\n **  أرسل ~ ( `.م8 ` )\n**• ⚜️ | لـ اوامر كورونا والصنع والوقت  :\n **  أرسل ~ ( `.م9 ` )\n**• ⚜️ | لـ اوامر مسح وتنظيف رسائل  :\n **  أرسل ~ ( `.م10 ` )\n**• ⚜️ | لـ اوامر البروفايل الوقتي  :\n **  أرسل ~ ( `.م11 ` )\n**• ⚜️ | لـ  اوامـر الازعـاج والترجـمـة والمنـع   :\n **  أرسل ~ ( `.م12 ` )\n**• ⚜️ | لـ  اوامـر قفل من  الدردشه وتحويل الصيغ   :\n **  أرسل ~ ( `.م13 ` )\n**• ⚜️ | لـ  اوامر الاعضاء بلكروب و اضافه الفارات :\n **  أرسل ~ ( `.م14 ` )\n**• ⚜️ | لـ  اوامر جلب صوره و الاحصائيات :\n **  أرسل ~ ( `.م15 ` )\**• ⚜️ | لـ اوامر تحويلات الميديا و الوضع نائـم ورسوم :\n **  أرسل ~ ( `.م16 ` ) \n**• ⚜️ | لـ اوامر ترحيب الخاص و بحث كوكل و ازاله   :\n **  أرسل ~ ( `.م17 ` ) \n**• ⚜️ | لـ أوامر تثبيت الملفات ومعلومات تنصيب وتاريخ الرسالـة   : **  أرسل ~ ( `.م18 ` ) \n**• ⚜️ | لـ اوامر تاك للكل و ماركدون و اوامر اضافية  :\n **  أرسل ~ ( `.م19 ` ) \n**• ⚜️ | لـ اوامر  معلومات كيثاب و سجل الاسماء  و اوامر اضافية  :\n **  أرسل ~ ( `.م20 ` ) \n\n**⌔︙ قـناة السورس  :**  @M4_STORY",    ) 
    
@iqthon.iq_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
    info={
        "header": "م1",
        "usage": "م1",
    },
)
async def _(event):
    "م1"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر الادمن والمجموعه :**  \n\n⌔︙  `.مسح جميع الردود` \n⌔︙ `.مسح رد`\n⌔︙ `.بنك` \n⌔︙ `.جميع الردود`\n⌔︙ `.اضف رد`\n⌔︙ `.صورة`\n⌔︙ `.رفع مشرف`\n⌔︙ `.تك`\n⌔︙ `.طرد`\n⌔︙ `.تثبيت`\n⌔︙ `.الغاء التثبيت`\n⌔︙ `.الاحداث`\n⌔︙ `.حظر`\n⌔︙ `.الغاء حظر`\n⌔︙ `.كتم`\n⌔︙ `.الغاء كتم`\n⌔︙ `.الاوامر`\n⌔︙ `.جميع الاوامر`\n⌔︙ `.الايدي`\n⌔︙ `.بنك`\n⌔︙ `.ترحيب`\n⌔︙ `.مسح الترحيبات`\n⌔︙ `.الترحيبات`\n⌔︙ `.رساله الترحيب السابقه`\n⌔︙ `.السورس`\n⌔︙ `.انتحال`\n⌔︙ `.الغاء الانتحال`",
    )
@iqthon.iq_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
    info={
        "header": "م2",
        "usage": "م2",
    },
)
async def _(event):
    "م2"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر متحركات تسلية :** \n\n.بنوك \n.بوسه\n.زرفه\n.بيبي\n.افكر\n.ضحك\n.ضايج\n.وقت\n.قلوب\n.رياضه\n.الارض\n.قمر\n.اقمار\n.قمور\n.فراشه\n.مكعبات\n.مطر\n.تحركات\n.ايموجيات\n.طائره\n.شرطه\n.النضام الشمسي\n.عين\n.ثعبان\n.رجل\n.مايكرو\n.رموزشيطانيه\n.قطار\n.موسيقى\n.رسم\n.تحميلات\n.اشكال مربع\n.دائره\n.قلب\n.مزاج\n.قرد\n.يد\n.العد التنازلي\n.الوان قلوب\n.غبي\n.تفجير\n.قتل\n.شنو\n.طوبه\n.مربعات\n.حلويات\n.نار",
    )
@iqthon.iq_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
    info={
        "header": "م3",
        "usage": "م3",
    },
)
async def _(event):
    "م3"
    await edit_or_reply(
        event,
        "**• ⚜️ | اوامر تغير حساب شخصي :** \n\n⌔︙ `.وضع بايو`\n⌔︙ `.وضع اسم`\n⌔︙ `.وضع صورة`\n⌔︙ `.وضع معرف`\n⌔︙ `.الحساب`\n⌔︙ `.حذف صوره`\n⌔︙ `.انشائي`",
    )
@iqthon.iq_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
    info={
        "header": "م4",
        "usage": "م4",
    },
)
async def _(event):
    "م4"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر تكرار رسائل  وتليجراف :**\n\n⌔︙ `.تكرار`\n⌔︙ `.تكرار الملصق`\n⌔︙ `.تكرار بالحرف`\n⌔︙ `.تكرار بالكلمه`\n⌔︙ `.مؤقت`\n⌔︙ `.تليجراف ميديا `\n ⌔︙ `.تليجراف كتابه `\n",
    )           
@iqthon.iq_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
    info={
        "header": "م5",
        "usage": "م5",
    },
)
async def _(event):
    "م5"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر تحميل من مواقع تواصل :**   \n\n⌔︙ `.تحميل ص `\n⌔︙ `.تحميل ف `\n⌔︙ `.نتائج بحث + اسم الاغنيه `\n⌔︙ `.انستا `\n⌔︙ `.بحث + اسم الاغنيه`\n⌔︙ `.بحث فيديو `\n⌔︙ `.معلومات الاغنيه `\n",
    )
@iqthon.iq_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
    info={
        "header": "م6",
        "usage": "م6",
    },
)
async def _(event):
    "م6"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اعاده التشغيل والاطفاء :**  \n\n⌔︙ `.اعاده تشغيل`\n⌔︙ `.اطفاء تليثون`\n⌔︙ `.اطفاء مؤقت +الوقت`\n⌔︙ `.التحديثات تشغيل`\n⌔︙ `.التحديثات ايقاف`",
    ) 
@iqthon.iq_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
    info={
        "header": "م7",
        "usage": "م7",
    },
)
async def _(event):
    "م7"
    await edit_or_reply(
        event,
        "**• ⚜️ | اوامر الخاصة بلمجموعه :** \n\n⌔︙ `.المشرفين`\n⌔︙ `.البوتات`\n⌔︙ `.الأعضاء`\n⌔︙ `.معلومات`\n⌔︙ `.موقع`",
    )
@iqthon.iq_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
    info={
        "header": "م8",
        "usage": "م8",
    },
)
async def _(event):
    "م8"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر رساله الحماية الخاص :**  \n\n⌔︙ `.الحماية تشغيل`\n`.الحماية ايقاف` \n⌔︙ `.قبول - رفض ( للحماية) `\n ⌔︙ `.مرفوض ( حظر من الخاص)`\n⌔︙ `.المقبولين ( عرض قائمة المقبولين في الحماية ) `",
    ) 
@iqthon.iq_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
    info={
        "header": "م9",
        "usage": "م9",
    },
)
async def _(event):
    "م9"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر كورونا والصنع والوقت  :** \n\n⌔︙ `.الاذان`\n⌔︙ `.كورونا + اسم الدوله بالانكليزي`\n⌔︙ `.ايدي + رد على الشخص`\n⌔︙ `.صنع مجموعه خارقه او قناه + الاسم`\n⌔︙ `.الوقت - لضهور تاريخ والوقت`\n⌔︙ `.وقتي - لضهور تاريخ والوقت بملصق `",
    )
@iqthon.iq_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
    info={
        "header": "م10",
        "usage": "م10",
    },
)
async def _(event):
    "م10"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر مسح وتنظيف رسائل :** \n\n⌔︙ `.تنظيف + الرد على الرساله ينضف مافي تحتها`\n⌔︙ `.حذف + رد على رساله يمسح الرساله`\n⌔︙ `.تنظيف رسائلي + عدد`\n",
    )
@iqthon.iq_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
    info={
        "header": "م11",
        "usage": "م11",
    },
)
async def _(event):
    "م11"
    await edit_or_reply(
        event,
        "**• ⚜️ |  اوامر البروفايل الوقتي :** \n\n⌔︙ `.اسم وقتي`\n⌔︙ `.نبذه وقتيه`\n⌔︙ `.صوره وقتيه`\n⌔︙ `.ايقاف اسم وقتي`\n⌔︙ `.ايقاف نبذه وقتيه`\n⌔︙ `.ايقاف صوره وقتيه`",
    ) 
@iqthon.iq_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
    info={
        "header": "م12",
        "usage": "م12",
    },
)
async def _(event):
    "م12"
    await edit_or_reply(
        event,
        "**•  ⚜️ |  اوامـر الازعـاج والترجـمـة والمنـع  :**  \n\n⌔︙ `.ازعاج `\n⌔︙ `.الغاء الازعاج` \n⌔︙ `.مسح الازعاج`\n⌔︙`.المزعجهم`\n •••••••••••••••••••••••••••••• \n⌔︙ `.ترجمه ar` ( من نكليزي الى عربي )\n⌔︙ `.ترجمه en` ( من عربي الى نكليزي ) \n⌔︙ `.تكلم en`  ( ترجمه صوتيه تحويل من عربي الى الانكلش )\n⌔︙ `.تكلم ar` ( ترجمه صوتيه تحويل من نكلش الى عربي ) \n •••••••••••••••••••••••••••••• \n⌔︙  `.المنع تشغيل` \n⌔︙  `.المنع ايقاف` -  ( لأيقاف وتشغيل مسح كلمات الممنوعه)\n⌔︙ `.منع +  الكلمة او الرد على الكلمة`\n ⌔︙ `.الغاء منع + كلمة او الرد على الكلمة` \n⌔︙ `.قائمة المنع ( لأضهار جميع الكلمات الممنوعه)`",
    )
@iqthon.iq_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
    info={
        "header": "م13",
        "usage": "م13",
    },
)
async def _(event):
    "م13"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ اوامـر قفل من  الدردشه وتحويل الصيغ   :   م13 **\n\n⌔︙ `.قفل الدردشه`\n⌔︙` .قفل الوسائط`\n⌔︙` .قفل الملصقات`\n⌔︙` .قفل الروابط`\n⌔︙ `.قفل المتحركة`\n⌔︙` .قفل الالعاب`\n⌔︙` .قفل  الانلاين`\n⌔︙ `.قفل التصويت`\n⌔︙ `.قفل الاضافة`\n⌔︙ `.قفل التثبيت`\n⌔︙ `.قفل الكل`\n\n**• ⚜️ | في حالة الفتح : **\n⌔︙ `.فتح +`  الصلاحية\n⌔︙`.الصلاحيات`   ( لأضهار صلاحيات مجموعة ) \n•• •• •• •• •• ••\n⌔︙` .تحويل صورة ` ( لتحويل ملصق الى صوره)\n⌔︙ `.تحويل ملصق`  ( لتحويل صوره الى ملصق)\n⌔︙ `.تحويل صوت`  ( لتحويل البصمه الى mp3)",
    ) 
@iqthon.iq_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
    info={
        "header": "م14",
        "usage": "م14",
    },
)
async def _(event):
    "م14"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ اوامر الاعضاء بلكروب و اضافه الفارات :  .م14 **\n⌔︙`.مغادره`\n⌔︙`.مسح المحضورين`\n⌔︙`.المحذوفين`\n⌔︙`.المحذوفين تنظيف`\n⌔︙`.احصائيات الاعضاء`\n⌔︙`.اضف فار`\n⌔︙`.حذف فار`\n⌔︙`.جلب فار`\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    )
@iqthon.iq_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
    info={
        "header": "م15",
        "usage": "م15",
    },
)
async def _(event):
    "م15"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ اوامر جلب صوره و الاحصائيات  :  .م15 **\n⌔︙`.احصائيات حسابي`\n⌔︙`.الصور جميعها` ( الرد على الشخص )\n⌔︙`الصوره + رقم صوره`\n⌔︙`.رابط الحساب`  ( الرد على الشخص )\n⌔︙`.سرعه الانترنيت`\n⌔︙`.تهكير`\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    )       
@iqthon.iq_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
    info={
        "header": "م16",
        "usage": "م16",
    },
)
async def _(event):
    "م16"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ اوامر تحويلات الميديا و الوضع نائـم :**  `.م16`\n⌔︙` .تحويل فديو دائري`  ⬇️\n( الرد على ملصق لتحويلة الى مرئيه دائرية ) \n⌔︙ `.تحويل ملصق دائري ` ⬇️\n ( الرد على ملصق لتحويلة الى ملصق دائري )\n⌔︙ `.تحويل صوره` ⬇️\n( الرد على ملصق لتحويلة الى صورة )\n⌔︙ `.تحويل ملف + اسم ملف` ⬇️\n( الرد على كتابه لتحويلها الى ملف بالاسم تريده )\n⌔︙ `.تحويل رساله `⬇️\n( الرد على ملف لتحويله الى الكتابه التي بداخله )\n⌔︙ `.تحويل ملف صوره ⬇️`\n( الرد على ملف صوره لتحويله الى صوره حقيقه )\n⌔︙ `.تحويل ملصق متحرك `⬇️\n( الرد على ملصقه متحركه تحويلها الى متحركه )\n⌔︙ `.تحويل متحركه` ⬇️\n( الرد على ملصق او صوره لتحويلها الى متحركه ) \n⌔︙ `.تحويل فديو متحركه `⬇️\n( لتحويل الفديو الى متحركه )\n⌔︙ `.احسب + المسئلة `⬇️\n( كمثال : .احسب 99+99 )\n⌔︙ `.رسم شعار + الكلمة `\n⌔︙ `.رسم قلوب + الكلمة`\n⌔︙ `.وضع النائم` ⬇️\n ( فقد ارسله بالخاص مالك اي شخص يرد عليك او يسويلك تاك يكله حاليا غير متواجد بس اذا راسلت بتليجرام تلقائيا ينلغي الوضع )\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    )  
@iqthon.iq_cmd(
    pattern="م17$",
    command=("م17", plugin_category),
    info={
        "header": "م17",
        "usage": "م17",
    },
)
async def _(event):
    "م17"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ اوامر ترحيب الخاص و بحث كوكل و ازاله توجيه :  .م17 **\n\n⌔︙ `.اضف ترحيب خاص`   ⬇️ \nشرح : ترحيب اي شخص يدخل للكروب ترسله ترحيب بخاصه  \n⌔︙ `.حذف ترحيب خاص`\n⌔︙` .لسته ترحيب خاص  `\n⌔︙ `.جلب لقطات + عدد لقطات`  ⬇️\n شرح :  الرد على فيديو لجلب لقطات من الفديو مع العدد محدد  \n⌔︙` .ازاله التوجيه` ⬇️\nشرح : الرد على بصمه موجة او أي شئ يقوم بازالة توجيها  \n⌔︙ `.البحث اونلاين + الاسم`  ⬇️\nشرح : يرسل اليك صوره باسم البحث خاص بك مع رابط بحث \n⌔︙ `.البحث العام + الاسم ` ⬇️\nشرح : الرد على صوره او فيديو لجلب الاشياء التي تتعلق بة  \n⌔︙ `.كوكل بحث + الاسم` ⬇️\nشرح :  لأضهار جميع البحوثات التي تتعلق بة\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    ) 
@iqthon.iq_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
    info={
        "header": "م18",
        "usage": "م18",
    },
)
async def _(event):
    "م18"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ أوامر تثبيت الملفات ومعلومات تنصيب وتاريخ الرسالـة :  .م18 **\n⌔︙` .تثبيت ملف` ⤵️\n( الرد على ملف تليثون بالأمر لتثبيتة) \n⌔︙ `.تثبيت ثانوي ` ⤵️\n( لأضافه نفـس أسم الملف الـذي أضفتة بتحديث اضافاتك ) \n⌔︙ `.حذف التثبيت + اسم ملف`  ⤵️\n(  ضع اسم الملف بجانب الامر لحذفه )  \n⌔︙ `.حذف جميع الملفات ` ⤵️\n( تنبية ⚠️ يقوم بحذف جميع ملفات تنصيبك) \n⌔︙ `.معلومات تنصيبي  `⤵️\n(  يجـلب جميع المعلومات والفـارات ومعلومات تنصيبك) \n⌔︙ `.تاريخ الرسالة ` ⤵️\n( الرد على الـرسالة لجـلب تـاريخ أرسالها و الوقت ) \n⌔︙ `.معلومات تخزين المجموعه ` ⤵️\n( لعرض معلومات مجموعتك عدد رسائل وصور وتخزين ) \n⌔︙ `.نص ثري دي + كلمة ` ⤵️\n( لتحويل الكلـمة الـى شعار او نص ثلاثي ابعاد )\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    ) 
@iqthon.iq_cmd(
    pattern="م19$",
    command=("م19", plugin_category),
    info={
        "header": "م19",
        "usage": "م19",
    },
)
async def _(event):
    "م19"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ أوامر تاك للكل و ماركدون و اوامر اضافية    : `.م19` **\n\n⌔︙ `.تاك للكل` ⤵️\n( يسوي تاك لكل الاشخاص بلكروب وبلقناه )\n⌔︙` .الكل` ⤵️\n( يسوي تاك لكل الاشخاص بلكروب وبلقناه ) \n⌔︙` .ابلاغ الادمنيه `⤵️\n( اي شخص مسوي ازعاج او تفليش مجرد دز الامر يسوي تاك لكل الادمنيه ويبلغهم) \n⌔︙ `.تاك بالكلام + معرف الشخص + الكلام  ` ⤵️\n( يدمج الرابط ويه الكلام مالك ويسوي تاك للشخص يعني يصير كلام بالرابط تاك)  \n⌔︙` .ماركدون `⤵️\n(يقوم بصنع ماركدون شفافيه لديك)  \n⌔︙` .تحذير تكرار + العدد `⤵️\n( يحذر الشخص بلكروب اي شخص يكرر يحذره ويسويله تاك حسب العدد الي محدده واذا كثر فدنوب تكرار يقيدة)  \n⌔︙` .رابط تطبيق + اسم تطبيق` ⤵️\n( يطلعلك رابط تطبيق ومعلوماته من سوق بلي) \n⌔︙`.مؤقته + الرساله + عدد الثواني` ⤵️\n( رساله وقتيه بس يخلص وقت الي محدده تنحذف رسالة )\n⌔︙` .تحويل ملكية + معرف شخص `⤵️\n( تنشره الامر بقناتك او بكروبك الي تريد تحوله لازم رافعه مشرف ومفعل تحقق بخطوتين )\n⌔︙` .وقتيه + عدد الثواني + الرساله `⤵️\n( رساله وقتيه تحدد الثواني مثل 10 ثواني بس تخلص يدز الرساله للشخص او للكروب)\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    ) 
@iqthon.iq_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
    info={
        "header": "م20",
        "usage": "م20",
    },
)
async def _(event):
    "م20"
    await edit_or_reply(
        event,
        "**• ⚜️ | لـ أوامر معلومات كيثاب و سجل الاسماء  و اوامر اضافية    : .م20  **\n\n⌔︙ `.كود بالرابط + الرد على الكود`  ⤵️\n(  txt يخليلك كود بالرابط من تدخله تشوف كود ) \n⌔︙ `.سجل الاسماء + الرد على شخص ` ⤵️\n ( يطيك الاسماء القديمه للشخص) \n⌔︙ `.دعوه + معرفة ` ⤵️\n( اضافه شخص للكروب )  \n⌔︙ `.رابط التنصيب ` ⤵️\n( يطيك رابط تنصيب سورسنه) \n⌔︙ `.حساب كيثاب + اسم كيثاب`  ⤵️\n( يطيك جميع معلومات الكيثاب الي كتبته و كلشي عليه للمطورين )  \n⌔︙ `.بحوثات كوكل + الاسم `⤵️\n ( يطلعلك بحوثات عن الاسم بكوكل) \n⌔︙ `.بحوثات يوتيوب + الاسم `⤵️\n( يطلعلك بحوثات عن الاسم بل يوتيوب )\n\n**⌔︙ قـناة السورس  :**  @M4_STORY",
    )
