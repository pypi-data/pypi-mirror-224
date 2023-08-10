import arabic_reshaper
from bidi.algorithm import get_display

def adopt_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text