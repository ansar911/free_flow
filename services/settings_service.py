from settings_app.models import AcademySettings


class SettingsService:

    @staticmethod
    def get_settings():

        settings = AcademySettings.objects.first()

        if not settings:

            settings = AcademySettings.objects.create()

        return settings