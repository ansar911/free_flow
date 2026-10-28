import requests

from settings_app.models import AcademySettings


class MetaWhatsAppService:

    @staticmethod
    def send_text_message(phone, message):

        settings = AcademySettings.objects.first()

        if not settings:
            raise Exception(
                "Academy Settings not found."
            )

        if not settings.whatsapp_enabled:
            raise Exception(
                "WhatsApp is disabled."
            )

        url = (
            f"https://graph.facebook.com/"
            f"{settings.whatsapp_api_version}/"
            f"{settings.whatsapp_phone_number_id}/messages"
        )

        headers = {
            "Authorization": (
                f"Bearer {settings.whatsapp_access_token}"
            ),
            "Content-Type": "application/json",
        }

        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message,
            },
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30,
        )

        if response.status_code not in (200, 201):
            raise Exception(
                f"Meta Error: {response.text}"
            )

        return response.json()