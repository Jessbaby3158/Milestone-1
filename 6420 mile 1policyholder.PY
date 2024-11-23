class PolicyHolder:
    def __init__(self, holder_id, name, email, is_active=True):
        self.holder_id = holder_id
        self.name = name
        self.email = email
        self.is_active = is_active

    def register(self):
        self.is_active = True
        print(f"Policyholder {self.name} registered successfully.")

    def suspend(self):
        self.is_active = False
        print(f"Policyholder {self.name} suspended successfully.")

    def reactivate(self):
        self.is_active = True
        print(f"Policyholder {self.name} reactivated successfully.")

    def __str__(self):
        status = "Active" if self.is_active else "Suspended"
        return f"ID: {self.holder_id}, Name: {self.name}, Email: {self.email}, Status: {status}"
