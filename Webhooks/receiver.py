"""
Webhook Receiver - Receives webhook notifications
Run: uvicorn receiver:app --port 8000 --reload
"""
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Webhook Receiver")


class WebhookPayload(BaseModel):
    event: str
    data: Dict[str, Any]


@app.post("/webhook/inventory")
async def inventory_webhook(payload: WebhookPayload):
    """Inventory system receives order notifications"""
    print(f"\nINVENTORY SYSTEM:")
    print(f"   Event: {payload.event}")
    print(f"   Order ID: {payload.data.get('order_id')}")
    print(f"   Items: {payload.data.get('items')}")
    print(f"   Action: Updating stock levels...\n")

    return {"status": "received", "system": "inventory"}


@app.post("/webhook/email")
async def email_webhook(payload: WebhookPayload):
    """Email service receives order notifications"""
    print(f"\nEMAIL SERVICE:")
    print(f"   Event: {payload.event}")
    print(f"   Customer: {payload.data.get('customer_email')}")
    print(f"   Order ID: {payload.data.get('order_id')}")
    print(f"   Action: Sending confirmation email...\n")

    return {"status": "received", "system": "email"}


@app.post("/webhook/analytics")
async def analytics_webhook(payload: WebhookPayload):
    """Analytics service receives order notifications"""
    print(f"\nANALYTICS SERVICE:")
    print(f"   Event: {payload.event}")
    print(f"   Total: ${payload.data.get('total', 0)}")
    print(f"   Action: Recording metrics...\n")

    return {"status": "received", "system": "analytics"}


@app.get("/")
def home():
    return {
        "service": "Webhook Receiver",
        "endpoints": [
            "/webhook/inventory",
            "/webhook/email",
            "/webhook/analytics"
        ]
    }
