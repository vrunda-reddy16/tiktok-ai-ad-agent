from rules import (
    validate_campaign_name,
    validate_objective,
    validate_ad_text,
    validate_cta,
    validate_music_choice,
    enforce_music_rules   
)
from tiktok_api import authenticate, submit_ad, OAuthError, ApiError
from schemas import build_ad_payload

def get_input(prompt):
    return input(prompt).strip()

def main():
    print("=== TikTok AI Ad Agent ===")
    print("I will help you create a TikTok Ad via conversation.\n")

    state = {
        "campaign_name": None,
        "objective": None,
        "ad_text": None,
        "cta": None,
        "music_choice": None,
        "music_id": None
    }

    # 1. Campaign Name
    while state["campaign_name"] is None:
        name = get_input("Enter campaign name: ")
        error = validate_campaign_name(name)
        if error:
            print(f"❌ {error}")
        else:
            state["campaign_name"] = name

    # 2. Objective
    while state["objective"] is None:
        obj = get_input("Enter objective (Traffic / Conversions): ")
        error = validate_objective(obj)
        if error:
            print(f"❌ {error}")
        else:
            state["objective"] = obj

    # 3. Ad Text
    while state["ad_text"] is None:
        text = get_input("Enter ad text (max 100 chars): ")
        error = validate_ad_text(text)
        if error:
            print(f"❌ {error}")
        else:
            state["ad_text"] = text

    # 4. CTA
    while state["cta"] is None:
        cta = get_input("Enter Call-To-Action (CTA): ")
        error = validate_cta(cta)
        if error:
            print(f"❌ {error}")
        else:
            state["cta"] = cta

    # 5. Music Selection
    while state["music_choice"] is None:
        print("\nMusic options:")
        print("1. existing  (use an existing TikTok music ID)")
        print("2. custom    (upload your own music)")
        print("3. none      (no music)")

        choice = get_input("Choose music option (existing/custom/none): ").lower()
        error = validate_music_choice(choice)
        if error:
            print(f"❌ {error}")
            continue

        rule_error = enforce_music_rules(state["objective"], choice)
        if rule_error:
            print(f"❌ {rule_error}")
            continue

        state["music_choice"] = choice

        if choice == "existing":
            music_id = get_input("Enter existing music ID: ")
            state["music_id"] = music_id

        elif choice == "custom":
            print("🎵 Simulating custom music upload...")
            state["music_id"] = "custom_music_123"

        elif choice == "none":
            state["music_id"] = None

    print("\n✅ All ad details collected successfully.\n")

    print("Final ad configuration:")
    print(state)
    
    print("\nSubmitting ad to TikTok Ads API...\n")

    try:
        access_token = authenticate()
        payload = build_ad_payload(state)

        response = submit_ad(access_token, payload)

        print("✅ Ad submitted successfully!")
        print("Ad ID:", response["ad_id"])

    except OAuthError as e:
        print("❌ Authentication failed.")
        print("Reason:", str(e))
        print("Suggested action: Re-authorize the TikTok Ads application.")

    except ApiError as e:
        print("❌ Ad submission failed.")
        print("Reason:", e.message)
        if e.retryable:
            print("Suggested action: Fix the issue and retry submission.")
        else:
            print("Suggested action: Check account permissions or settings.")





if __name__ == "__main__":
    main()

