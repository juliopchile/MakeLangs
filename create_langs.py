import os

# Directory containing (or to contain) the README files.
DOCS_DIR = "docs"

# Original alert text for reference
alert_text = ("**Nota importante sobre la traducción**\n\n"
            "El texto a continuación ha sido traducido mediante herramientas de IA (traducción automática). Dado que este proceso puede contener errores o imprecisiones, recomendamos consultar la versión original en inglés o español para garantizar la precisión de la información.\n\n"
            "---")

languages = {
    "en": {
        "name": "English",
        "badge_color": "blue",
        "needs_alert": False,
    },
    "es": {
        "name": "Español",
        "badge_color": "purple",
        "needs_alert": False,
    },
    "fr": {
        "name": "Français",
        "badge_color": "yellow",
        "needs_alert": True,
        "alert_text": (
            "**Note importante sur la traduction**\n\n"
            "Le texte ci-dessous a été traduit à l'aide d'outils d'IA (traduction automatique). "
            "Comme ce processus peut comporter des erreurs ou des imprécisions, nous recommandons de "
            "consulter la version originale en anglais ou en espagnol afin de garantir l'exactitude des "
            "informations.\n\n"
            "---"
        ),
    },
    "zh": {
        "name": "中文",
        "badge_color": "red",
        "needs_alert": True,
        "alert_text": (
            "**重要提示：关于翻译**\n\n"
            "下文使用了 AI（自动翻译）工具进行翻译。由于此过程可能包含错误或不准确之处，"
            "建议您查看英文或西班牙文原版，以确保信息的准确性。\n\n"
            "---"
        ),
    },
    "pt": {
        "name": "Português",
        "badge_color": "brightgreen",
        "needs_alert": True,
        "alert_text": (
            "**Importante sobre a tradução**\n\n"
            "O texto abaixo foi traduzido usando ferramentas de IA (tradução automática). Como esse "
            "processo pode conter erros ou imprecisões, recomendamos consultar a versão original em "
            "inglês ou espanhol para garantir a precisão das informações.\n\n"
            "---"
        ),
    },
    "de": {
        "name": "Deutsch",
        "badge_color": "blueviolet",
        "needs_alert": True,
        "alert_text": (
            "**Wichtiger Hinweis zur Übersetzung**\n\n"
            "Der nachfolgende Text wurde mithilfe von KI-Übersetzungstools (automatische Übersetzung) "
            "übersetzt. Da dieser Vorgang Fehler oder Ungenauigkeiten enthalten kann, empfehlen wir, "
            "zur Gewährleistung der Genauigkeit die Originalversion in Englisch oder Spanisch "
            "heranzuziehen.\n\n"
            "---"
        ),
    },
    "it": {
        "name": "Italiano",
        "badge_color": "orange",
        "needs_alert": True,
        "alert_text": (
            "**Nota importante sulla traduzione**\n\n"
            "Il testo seguente è stato tradotto mediante strumenti di intelligenza artificiale "
            "(traduzione automatica). Poiché questo processo potrebbe contenere errori o imprecisioni, "
            "si consiglia di consultare la versione originale in inglese o in spagnolo per garantire "
            "l’accuratezza delle informazioni.\n\n"
            "---"
        ),
    },
    "jp": {
        "name": "日本語",
        "badge_color": "yellowgreen",
        "needs_alert": True,
        "alert_text": (
            "**翻訳に関する重要な注意事項**\n\n"
            "以下のテキストは AI（自動翻訳）ツールを使用して翻訳されています。"
            "この過程には誤りや不正確さが含まれる可能性があるため、情報の正確性を確保するには "
            "英語またはスペイン語の原文を参照することをお勧めします。\n\n"
            "---"
        ),
    },
    "ar": {
        "name": "العربية",
        "badge_color": "lightgrey",
        "needs_alert": True,
        "alert_text": (
            "**ملاحظة مهمة حول الترجمة**\n\n"
            "تمت ترجمة النص أدناه باستخدام أدوات الذكاء الاصطناعي (الترجمة الآلية). "
            "نظرًا لإمكانية احتواء هذه العملية على أخطاء أو عدم دقة، نوصي بالرجوع إلى النسخة "
            "الأصلية باللغة الإنجليزية أو الإسبانية لضمان دقة المعلومات.\n\n"
            "---"
        ),
    },
    "he": {
        "name": "עברית",
        "badge_color": "teal",
        "needs_alert": True,
        "alert_text": (
            "**הערה חשובה לגבי התרגום**\n\n"
            "הטקסט הבא תורגם באמצעות כלים של בינה מלאכותית (תרגום אוטומטי). "
            "מכיוון שתהליך זה עלול לכלול שגיאות או חוסר דיוקים, אנו ממליצים לעיין "
            "בגרסה המקורית באנגלית או בספרדית כדי להבטיח את דיוק המידע.\n\n"
            "---"
        ),
    },
    "ru": {
        "name": "Русский",
        "badge_color": "lightblue",
        "needs_alert": True,
        "alert_text": (
            "**Важное примечание относительно перевода**\n\n"
            "Ниже приведён текст, переведённый с использованием инструментов искусственного интеллекта "
            "(автоматический перевод). Поскольку этот процесс может содержать ошибки или неточности, "
            "рекомендуется обратиться к оригиналу на английском или испанском языках для обеспечения точности информации.\n\n"
            "---"
        ),
    },
    "uk": {
        "name": "Українська",
        "badge_color": "skyblue",
        "needs_alert": True,
        "alert_text": (
            "**Важлива примітка щодо перекладу**\n\n"
            "Нижче наведено текст, перекладений за допомогою інструментів штучного інтелекту (автоматичний переклад). "
            "Оскільки цей процес може містити помилки або неточності, радимо звернутися до оригіналу англійською чи іспанською мовами "
            "для забезпечення точності інформації.\n\n"
            "---"
        ),
    },
}


def build_language_links():
    """
    Constructs the list of language links using the dictionary values.
    Returns a string with all badges (each on its own line).
    """
    links = []
    for lang_code, info in languages.items():
        badge = (
            f"[![{info['name']}]"
            f"(https://img.shields.io/badge/lang-{info['name']}-{info['badge_color']})]"
            f"(README.{lang_code}.md)"
        )
        links.append(badge)
    # Join all badge links with newline characters.
    return "\n".join(links)


def update_readme(file_path, lang_info, language_links_text):
    """
    Reads the README file if it exists, then:
      - Prepends the alert text (if needed and if not already present).
      - Appends the language links badge section (if not already present).
    Finally, writes the modified content back, or creates a new file if it doesn't exist.
    """
    # If file exists, read its contents; if not, start with empty content.
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as err:
            print(f"Error reading {file_path}: {err}")
            return
    else:
        content = ""

    # If this language requires an alert and the alert is not already present,
    # prepend it to the file content.
    if lang_info.get("needs_alert") and lang_info.get("alert_text"):
        # A simple check for French example; you may want to make this check more robust.
        if lang_info["alert_text"].strip().split("\n", 1)[0] not in content:
            content = lang_info["alert_text"] + content

    # Append the language links if not already included.
    if language_links_text not in content:
        content = content.rstrip() + "\n\n" + language_links_text + "\n"

    # Write the updated content back to the file (creating it if needed).
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated or created: {file_path}")
    except Exception as err:
        print(f"Error writing {file_path}: {err}")


def main():
    # Ensure the docs directory exists.
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR, exist_ok=True)

    # Get the text of all language links (badges).
    language_links_text = build_language_links()

    # For each language, update or create the corresponding README file.
    for lang_code, lang_info in languages.items():
        readme_filename = f"README.{lang_code}.md"
        file_path = os.path.join(DOCS_DIR, readme_filename)
        update_readme(file_path, lang_info, language_links_text)


if __name__ == "__main__":
    main()
