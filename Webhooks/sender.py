"""
Webhook Sender - Main application that sends webhooks
Run: uvicorn sender:app --port 8001 --reload
"""
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any
import httpx
import asyncio

app = FastAPI(title="Order System (Webhook Sender)")

# Store webhook subscriptions
subscriptions: List[Dict] = []


class WebhookSubscription(BaseModel):
    url: HttpUrl
    name: str


class Order(BaseModel):
    customer_email: str
    items: List[str]
    total: float


async def send_webhook(url: str, event: str, data: Dict[str, Any]):
    """Send webhook to a URL"""
    payload = {"event": event, "data": data}

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(url, json=payload)
            print(f"Webhook sent to {url} - Status: {response.status_code}")
            return {"url": url, "status": "success"}
    except Exception as e:
        print(f"Failed to send webhook to {url}: {str(e)}")
        return {"url": url, "status": "failed", "error": str(e)}


@app.post("/subscribe")
def subscribe_webhook(subscription: WebhookSubscription):
    """Register a webhook URL"""
    sub = {
        "url": str(subscription.url),
        "name": subscription.name
    }
    subscriptions.append(sub)

    return {
        "message": "Webhook subscribed",
        "subscription": sub,
        "total_subscribers": len(subscriptions)
    }


@app.get("/subscribers")
def list_subscribers():
    """List all webhook subscribers"""
    return {"subscribers": subscriptions, "total": len(subscriptions)}


@app.post("/order")
async def create_order(order: Order):
    """Create an order and trigger webhooks"""
    order_id = f"ORD-{len(subscriptions) + 1001}"

    # Order data to send in webhook
    webhook_data = {
        "order_id": order_id,
        "customer_email": order.customer_email,
        "items": order.items,
        "total": order.total
    }

    print(f"\nNEW ORDER CREATED: {order_id}")
    print(f"Customer: {order.customer_email}")
    print(f"Items: {order.items}")
    print(f"Total: ${order.total}")
    print(f"\nSending webhooks to {len(subscriptions)} subscribers...\n")

    # Send webhooks to all subscribers
    tasks = [
        send_webhook(sub["url"], "order.created", webhook_data)
        for sub in subscriptions
    ]

    results = await asyncio.gather(*tasks)

    return {
        "order_id": order_id,
        "customer_email": order.customer_email,
        "total": order.total,
        "webhooks_sent": len(results),
        "webhook_results": results
    }


@app.get("/")
def home():
    return {
        "service": "Order System",
        "subscribers": len(subscriptions),
        "endpoints": {
            "create_order": "POST /order",
            "subscribe": "POST /subscribe",
            "list_subscribers": "GET /subscribers"
        }
    }
