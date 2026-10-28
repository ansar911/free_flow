import calendar
from students.models import Student

from settings_app.models import AcademySettings


class BillingPreview:

    @staticmethod
    def get(month, year):

        settings = AcademySettings.objects.first()

        from datetime import date

        last_day = calendar.monthrange(year, month)[1]

        billing_date = date(
            year,
            month,
            last_day,
        )

        students = Student.objects.filter(
            status="ACTIVE",
            joined_date__lte=billing_date,
        ).select_related("parent")

        total_students = students.count()

        total_parents = (
            students.values("parent")
            .distinct()
            .count()
        )

        monthly_fee = settings.monthly_fee

        expected_income = (
            monthly_fee * total_students
        )

        return {

            "month": month,
            "year": year,

            "students": total_students,

            "parents": total_parents,

            "fee": monthly_fee,

            "expected_income": expected_income,

        }