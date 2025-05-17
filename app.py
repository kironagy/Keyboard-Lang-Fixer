import pyperclip
import keyboard

# خريطة انجليزي → عربي مع الرموز حسب الكيبورد العربي
english_to_arabic = {
    'q': 'ض',
    'w': 'ص',
    'e': 'ث',
    'r': 'ق',
    't': 'ف',
    'y': 'غ',
    'u': 'ع',
    'i': 'ه',
    'o': 'خ',
    'p': 'ح',
    'a': 'ش',
    's': 'س',
    'd': 'ي',
    'f': 'ب',
    'g': 'ل',
    'h': 'ا',
    'j': 'ت',
    'k': 'ن',
    'l': 'م',
    ';': 'ك',
    '\'': 'ط',
    'z': 'ئ',
    'x': 'ء',
    'c': 'ؤ',
    'v': 'ر',
    'b': 'لا',
    'n': 'ى',
    'm': 'ة',
    ',': 'و',
    '.': 'ز',
    '/': 'ظ',
    '[': 'ج',
    ']': 'د',
    '`': 'و',
    '~': 'ذ',
}

# بالعكس عربي → انجليزي
arabic_to_english = {v: k for k, v in english_to_arabic.items()}

def convert_text(text: str) -> str:
    is_arabic = any('\u0600' <= ch <= '\u06FF' for ch in text)
    result = []

    if is_arabic:
        for ch in text:
            result.append(arabic_to_english.get(ch, ch))
    else:
        for ch in text:
            if ch in english_to_arabic:
                result.append(english_to_arabic[ch])
            elif ch.lower() in english_to_arabic:
                result.append(english_to_arabic[ch.lower()])
            else:
                result.append(ch)
    return ''.join(result)

def on_hotkey():
    try:
        text = pyperclip.paste()
        if not text.strip():
            print("Clipboard empty.")
            return
        converted = convert_text(text)
        pyperclip.copy(converted)
        print(f"✅ Converted text copied to clipboard:\n{converted}")
    except Exception as e:
        print(f"❌ Error: {e}")

keyboard.add_hotkey("ctrl+shift+q", on_hotkey)

print("⌨️ Press Ctrl + Shift + Q to convert clipboard text...")
keyboard.wait()
