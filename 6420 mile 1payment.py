class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount, is_paid=False):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.is_paid = is_paid

    def process_payment(self):
        self.is_paid = True
        print(f"Payment of {self.amount} for policyholder {self.policyholder_id} processed successfully.")

    def send_reminder(self):
        if not self.is_paid:
            print(f"Reminder: Payment for policyholder {self.policyholder_id} is pending.")

    def apply_penalty(self, penalty_amount):
        if not self.is_paid:
            self.amount += penalty_amount
            print(f"Penalty of {penalty_amount} applied. Total due: {self.amount}")

    def __str__(self):
        status = "Paid" if self.is_paid else "Pending"
        return f"Payment ID: {self.payment_id}, Policyholder ID: {self.policyholder_id}, Product ID: {self.product_id}, Amount: {self.amount}, Status: {status}"
