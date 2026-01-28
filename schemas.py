def build_ad_payload(state):
    return {
        "campaign_name": state["campaign_name"],
        "objective": state["objective"],
        "creative": {
            "text": state["ad_text"],
            "cta": state["cta"],
            "music_id": state["music_id"]
        }
    }

