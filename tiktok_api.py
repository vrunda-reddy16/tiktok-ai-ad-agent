class OAuthError(Exception):
    pass

class ApiError(Exception):
    def __init__(self, message, retryable=False):
        self.message = message
        self.retryable = retryable
        super().__init__(message)


def authenticate():
    """
    Simulate OAuth authentication
    """
    # Change this value to simulate failures
    token_status = "valid"  # options: valid, expired, invalid, geo_blocked

    if token_status == "expired":
        raise OAuthError("Access token has expired.")
    if token_status == "invalid":
        raise OAuthError("Invalid client credentials.")
    if token_status == "geo_blocked":
        raise OAuthError("Access blocked due to geo-restriction.")

    return "mock_access_token_123"


def submit_ad(access_token, ad_payload):
    """
    Simulate TikTok Ads API submission
    """
    if not access_token:
        raise ApiError("Missing or invalid access token.", retryable=False)

    if ad_payload["creative"]["music_id"] == "invalid_music":
        raise ApiError("Invalid music ID provided.", retryable=True)

    # Simulate success
    return {
        "status": "success",
        "ad_id": "tiktok_ad_456"
    }

