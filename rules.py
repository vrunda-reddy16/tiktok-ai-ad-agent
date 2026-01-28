def validate_campaign_name(name):
    if not name or len(name) < 3:
        return "Campaign name must be at least 3 characters."
    return None

def validate_objective(obj):
    if obj not in ["Traffic", "Conversions"]:
        return "Objective must be either 'Traffic' or 'Conversions'."
    return None

def validate_ad_text(text):
    if not text:
        return "Ad text is required."
    if len(text) > 100:
        return "Ad text must be 100 characters or less."
    return None

def validate_cta(cta):
    if not cta:
        return "CTA is required."
    return None

def validate_music_choice(choice):
    if choice not in ["existing", "custom", "none"]:
        return "Music choice must be: existing, custom, or none."
    return None

def enforce_music_rules(objective, music_choice):
    if objective == "Conversions" and music_choice == "none":
        return "Music is required for Conversion campaigns."
    return None

