from policyholder import PolicyHolder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = PolicyHolder(holder_id=1, name="John Doe", email="john@example.com")
policyholder2 = PolicyHolder(holder_id=2, name="Jane Smith", email="jane@example.com")

# Create products
product1 = Product(product_id=101, name="Health Insurance", price=500.0)
product2 = Product(product_id=102, name="Car Insurance", price=300.0)

# Register policyholders
policyholder1.register()
policyholder2.register()

# Suspend and reactivate policyholder
policyholder2.suspend()
policyholder2.reactivate()

# Create payments
payment1 = Payment(payment_id=1001, policyholder_id=1, product_id=101, amount=500.0)
payment2 = Payment(payment_id=1002, policyholder_id=2, product_id=102, amount=300.0)

# Process payments
payment1.process_payment()
payment2.process_payment()

# Display details
print("\nPolicyholder Details:")
print(policyholder1)
print(policyholder2)

print("\nProduct Details:")
print(product1)
print(product2)

print("\nPayment Details:")
print(payment1)
print(payment2)
