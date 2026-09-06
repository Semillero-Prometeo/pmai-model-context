import torch
import re

DEVICE = "cpu"


PROTECTED_WORDS = {
    "robot", "robots", "niño", "niña", "nino", "nina",
    "man", "woman", "child", "children", "boy", "girl",
    "baby", "person", "people", "mascot", "mascots",
    "cat", "dog", "bird", "bear", "horse",
    "car", "table", "chair", "screen", "laptop",
    "camera", "phone", "computer",
    "white", "black", "red", "blue", "green", "yellow",
    "small", "large", "big", "tall",
    "standing", "sitting", "walking", "holding", "wearing",
    "looking", "working"
}

SUSPICIOUS_WORDS = {
    "credit", "likely", "probably", "maybe", "seems",
    "appears", "could", "might", "perhaps", "possibly",
    "apparently", "allegedly", "supposedly",
    "nasa", "unknown", "unidentified", "unclear",
    "sebre", "seiree", "sere", "seire","spain","spain's","spains","spain's","spain's","spain's",
    "russia","russia's","russias","russia's","russia's","russia's",
    "germany","germany's","germanys","germany's","germany's","germany's",
    "france","france's","frances","france's","france's","france's",
    "peru","peru's","perus","peru's","peru's","peru's",
    "bolivia","bolivia's","bolivias","bolivia's","bolivia's","bolivia's",
    "le l' estrange","le l' estranges","le l' estrange's","le l' estrange's","le l' estrange's",
    "le", "l'", "le's", "le's", "le's",
    "l' ","estr","estrange","estranges","estrange's","estrange's","estrange's",
    "l' est","le l' est","le l' est","le l' est's","le l' est's","le l' est's","how do i' m"
    "crochel", "keychais", "croche","keychain","that say", "that reads", "says", "reads","triumph","triumphs","triumphing","triumphant",
    " le jet ete", " le jet ete's", " le jet etes", " le jet etes'", " le jet etes's",
}

HALLUCINATION_PATTERNS = [
    r'\b(\w{4,})\s+\1\b',
    r'\b(a man|a woman).{0,15}(a man|a woman)\b',
    r'\b(is|are|was|were)\s+(is|are|was|were)\b',
    r'\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},?\s*\d{4}\b',
    r'\b(19|20)\d{2}\b',
    r"\b(says|reads|that says|that reads)\s+['\"`\u2018\u2019]+[^'\"\u2018\u2019`]{0,40}['\"`\u2018\u2019]+",
    r"[`\u2018\u2019]{2,}",
    r'\bin\s+(st\.?\s+petersburg|barcelona|paris|london|new york|moscow|berlin|tokyo)\b',
    r"nasa\s*'?s?\s*\w*",
    r'\b(mascots?|robots?|people)\b(.{0,30})\b\1\b',
]


def clean_caption(caption: str) -> str:
    words = caption.split()

    filtered = []
    for w in words:
        clean_w = w.strip(".,!?;:`\u2018\u2019'\"").lower()
        # Si está protegida, pasa siempre
        if clean_w in PROTECTED_WORDS:
            filtered.append(w)
        # Si está en sospechosas, se elimina
        elif clean_w in SUSPICIOUS_WORDS:
            continue
        else:
            filtered.append(w)

    caption = " ".join(filtered).strip()

    # Aplica patrones pero protege palabras clave
    for pattern in HALLUCINATION_PATTERNS:
        match = re.search(pattern, caption, flags=re.IGNORECASE)
        if match:
            matched_text = match.group(0)
            # No elimina si el match contiene una palabra protegida
            contains_protected = any(
                pw in matched_text.lower().split()
                for pw in PROTECTED_WORDS
            )
            if not contains_protected:
                caption = re.sub(pattern, '', caption, flags=re.IGNORECASE).strip()

    # Limpieza de puntuación huérfana
    caption = re.sub(r"\s([.,!?;:'])", r'\1', caption)
    caption = re.sub(r"[,;]\s*$", '', caption)
    caption = re.sub(r"\s*'\s*s\b", "'s", caption)
    caption = re.sub(r'\s{2,}', ' ', caption).strip()

    if caption:
        caption = caption[0].upper() + caption[1:]

    return caption


def generate_context(pil_image, processor, model):

    prompt = ""

    gen_kwargs = dict(
        max_length=88,
        min_length=18,
        num_beams=10,
        repetition_penalty=1.4,
        early_stopping=True,
        length_penalty=1.05,
        no_repeat_ngram_size=3,
        use_cache=True,
    )

    inputs = processor(
        images=pil_image,
        text=prompt,
        return_tensors="pt",
        truncation=True,
    ).to(DEVICE)

    with torch.inference_mode():
        output = model.generate(**inputs, **gen_kwargs)

    raw_caption = processor.batch_decode(output, skip_special_tokens=True)[0]
    context = clean_caption(raw_caption)

    return context, prompt


def generate_context_from_base64(base64_string: str, processor, model):
    """Genera contexto visual directamente desde una imagen Base64."""
    from utils.decoder import base64_to_image

    image = base64_to_image(base64_string)
    return generate_context(image, processor, model)
