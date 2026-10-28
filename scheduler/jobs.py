from datetime import datetime

from billing.models import BillingCycle
from billing.services.billing_generator import BillingGenerator
from whatsapp.services.whatsapp_service import WhatsAppService
from logs.models import ActivityLog


def monthly_billing_job():

    today = datetime.today()

    exists = BillingCycle.objects.filter(
        month=today.month,
        year=today.year,
    ).exists()

    if exists:
        print("Billing already exists.")
        return

    try:

        BillingGenerator.generate(
            today.month,
            today.year,
        )

        WhatsAppService.queue_pending_messages()

        ActivityLog.objects.create(
            user=None,
            action="AUTO_BILLING",
            description=f"Automatic billing generated for {today.strftime('%B %Y')}",
        )

        print("Monthly billing completed.")

    except Exception as e:

        print(e)