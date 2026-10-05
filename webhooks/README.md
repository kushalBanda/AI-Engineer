# Simple Webhook Example with FastAPI

A clean, practical example of webhooks: Order notification system.

## What This Does

When a customer places an order, the system automatically notifies:

- Inventory System (to update stock)
- Email Service (to send confirmation)
- Analytics Service (to track metrics)

## Files

- `receiver.py` - Webhook receiver (the services that GET notified)
- `sender.py` - Webhook sender (the order system that SENDS notifications)
- `test.py` - Demo script

## Quick Start

### Terminal 1: Start Receiver

```bash
uvicorn receiver:app --port 8000 --reload
```

### Terminal 2: Start Sender

```bash
uvicorn sender:app --port 8001 --reload
```

### Terminal 3: Run Test

```bash
python test.py
```

## Manual Testing

### 1. Register webhook subscribers

```bash
curl -X POST http://localhost:8001/subscribe \
  -H "Content-Type: application/json" \
  -d '{"url": "http://localhost:8000/webhook/inventory", "name": "Inventory"}'

curl -X POST http://localhost:8001/subscribe \
  -H "Content-Type: application/json" \
  -d '{"url": "http://localhost:8000/webhook/email", "name": "Email"}'
```

### 2. Create an order (triggers webhooks)

```bash
curl -X POST http://localhost:8001/order \
  -H "Content-Type: application/json" \
  -d '{
    "customer_email": "customer@example.com",
    "items": ["Laptop", "Mouse"],
    "total": 1050.00
  }'
```

### 3. Check subscribers

```bash
curl http://localhost:8001/subscribers
```

## How It Works

```
Customer places order
        ↓
Order System (sender.py)
        ↓
Sends webhooks to all subscribers
        ↓
    ┌───┴───┬────────┐
    ↓       ↓        ↓
Inventory Email  Analytics
(receiver.py endpoints)
```

## Interactive Docs

- Receiver: http://localhost:8000/docs
- Sender: http://localhost:8001/docs
