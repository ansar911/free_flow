from logs.models import ActivityLog


class Logger:

    @staticmethod
    def log(user, action, description):

        ActivityLog.objects.create(
            user=user,
            action=action,
            description=description,
        )