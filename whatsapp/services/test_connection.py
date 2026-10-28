from .meta_service import MetaWhatsAppService


class WhatsAppConnectionTest:

    @staticmethod
    def test():

        try:

            response = MetaWhatsAppService.send_text_message(

                phone="919999999999",

                message="FeeFlow Connection Test",

            )

            if response.status_code == 200:

                return (
                    True,
                    "Connection successful.",
                )

            return (
                False,
                response.text,
            )

        except Exception as e:

            return (
                False,
                str(e),
            )