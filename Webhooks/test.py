"""
Simple test script to demonstrate webhooks
"""
import requests
import time

SENDER = "http://localhost:8001"
RECEIVER = "http://localhost:8000"


def main():
    print("\n" + "="*60)
    print("WEBHOOK DEMO - Order Notification System")
    print("="*60)

    # Step 1: Register webhook subscribers
    print("\nRegistering webhook subscribers...")

    subscribers = [
        {"url": f"{RECEIVER}/webhook/inventory", "name": "Inventory System"},
        {"url": f"{RECEIVER}/webhook/email", "name": "Email Service"},
        {"url": f"{RECEIVER}/webhook/analytics", "name": "Analytics Service"}
    ]

    for sub in subscribers:
        response = requests.post(f"{SENDER}/subscribe", json=sub)
        print(f"Registered: {sub['name']}")

    time.sleep(1)

    # Step 2: Create an order (this will trigger webhooks)
    print("\nCreating a new order...")

    order = {
        "customer_email": "customer@example.com",
        "items": ["Laptop", "Mouse", "Keyboard"],
        "total": 1299.99
    }

    response = requests.post(f"{SENDER}/order", json=order)
    result = response.json()

    print(f"\n   Order Created: {result['order_id']}")
    print(f"   Webhooks Sent: {result['webhooks_sent']}")

    # Step 3: Show results
    print("\nWebhook Delivery Results:")
    for webhook in result['webhook_results']:
        print(f"   {webhook['url']} - {webhook['status']}")

    print("\n" + "="*60)
    print("DEMO COMPLETED!")
    print("="*60)
    print("\nCheck the terminal windows where you started the services")
    print("to see the webhook processing in action!\n")


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\nERROR: Could not connect to services")
        print("\nMake sure both services are running:")
        print("   Terminal 1: uvicorn receiver:app --port 8000 --reload")
        print("   Terminal 2: uvicorn sender:app --port 8001 --reload")
        print("   Terminal 3: python test.py\n")
