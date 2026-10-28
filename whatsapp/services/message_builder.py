class MessageBuilder:

    @staticmethod
    def build(invoice):

        student_names = []

        for item in invoice.items.all():
            student_names.append(item.student.name)

        students = "\n".join(
            [f"• {name}" for name in student_names]
        )

        balance = invoice.total_amount - invoice.paid_amount

        return f"""
🏆 Indian Fitness

Dear {invoice.parent.name},

Monthly Fee Reminder

Billing Month:
{invoice.billing_cycle.name}

Student(s):
{students}

Outstanding Amount:
₹{balance}

Please complete your payment.

Thank you.
""".strip()