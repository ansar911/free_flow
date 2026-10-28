from apscheduler.schedulers.background import BackgroundScheduler

from scheduler.jobs import monthly_billing_job


scheduler = BackgroundScheduler()


def start():

    if scheduler.running:
        return

    scheduler.add_job(
        monthly_billing_job,
        trigger="interval",
        minutes=1,
        id="monthly_billing",
        replace_existing=True,
    )

    scheduler.start()

    print("Scheduler Started")