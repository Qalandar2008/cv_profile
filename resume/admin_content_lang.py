"""Admin forma kontenti qaysi tilda ko‘rsatilishini sessiya orqali saqlash."""

SESSION_KEY = "admin_content_lang"
VALID = frozenset({"en", "uz", "ru"})


def get_content_lang(request) -> str:
    if not request:
        return "en"
    lang = request.session.get(SESSION_KEY, "en")
    return lang if lang in VALID else "en"


def content_lang_label(code: str) -> str:
    return {"en": "English", "uz": "Oʻzbekcha", "ru": "Русский"}.get(code, code)
