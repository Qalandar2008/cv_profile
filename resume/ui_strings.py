"""Gettext bo‘lmasa ham ishlaydigan UI qatorlari (en / uz / ru)."""

from django.utils.translation import get_language

_TEXTS: dict[str, dict[str, str]] = {
    "en": {
        "resume": "Resume",
        "language": "Language",
        "about_me": "About me",
        "certificates": "Certificates",
        "interests": "Interests",
        "website": "Website",
        "view_document": "View document",
        "built_with_django": "Built with Django",
        "admin_title": "CV resume administration",
        "admin_site": "CV Admin",
        "admin_dashboard": "Dashboard",
        "cv_content_lang": "CV content language",
        "cv_content_lang_hint": "Fields below show text for the selected language only. Switch language, then Save.",
    },
    "uz": {
        "resume": "Rezyume",
        "language": "Til",
        "about_me": "O‘zim haqimda",
        "certificates": "Sertifikatlar",
        "interests": "Qiziqishlar",
        "website": "Veb-sayt",
        "view_document": "Hujjatni ko‘rish",
        "built_with_django": "Django yordamida yig‘ilgan",
        "admin_title": "CV rezyume boshqaruvi",
        "admin_site": "CV admin",
        "admin_dashboard": "Boshqaruv paneli",
        "cv_content_lang": "CV matni tili",
        "cv_content_lang_hint": "Quyidagi maydonlar faqat tanlangan til uchun. Tilni almashtiring, keyin Saqlash.",
    },
    "ru": {
        "resume": "Резюме",
        "language": "Язык",
        "about_me": "Обо мне",
        "certificates": "Сертификаты",
        "interests": "Интересы",
        "website": "Сайт",
        "view_document": "Открыть документ",
        "built_with_django": "Сделано на Django",
        "admin_title": "Администрирование резюме",
        "admin_site": "CV Админ",
        "admin_dashboard": "Панель управления",
        "cv_content_lang": "Язык текста резюме",
        "cv_content_lang_hint": "Поля ниже — только для выбранного языка. Смените язык и нажмите «Сохранить».",
    },
}


def ui_text(key: str) -> str:
    lang = (get_language() or "en")[:2]
    bucket = _TEXTS.get(lang) or _TEXTS["en"]
    return bucket.get(key) or _TEXTS["en"].get(key, key)
