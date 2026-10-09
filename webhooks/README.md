# Webhooks

[← AI Engineer](../README.md)

**Level:** 🟢 Beginner · **Type:** `Tutorial` · Commands run from the repo root.

A practical webhook example with FastAPI: an order notification system. When a customer places an order, the system notifies an inventory system (to update stock), an email service (to send confirmation), and an analytics service (to track metrics).

| File | Role |
| :--- | :--- |
| `receiver.py` | Webhook receiver: the services that get notified |
| `sender.py` | Webhook sender: the order system that sends notifications |
| `test.py` | Demo script |

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

## Run

```bash
cd webhooks
uvicorn receiver:app --port 8000 --reload   # terminal 1
uvicorn sender:app --port 8001 --reload     # terminal 2
python test.py                              # terminal 3
```

Interactive docs: receiver at `http://localhost:8000/docs`, sender at `http://localhost:8001/docs`.

## Test by hand

```bash
# 1. Register webhook subscribers
curl -X POST http://localhost:8001/subscribe \
  -H "Content-Type: application/json" \
  -d '{"url": "http://localhost:8000/webhook/inventory", "name": "Inventory"}'

curl -X POST http://localhost:8001/subscribe \
  -H "Content-Type: application/json" \
  -d '{"url": "http://localhost:8000/webhook/email", "name": "Email"}'

# 2. Create an order (triggers webhooks)
curl -X POST http://localhost:8001/order \
  -H "Content-Type: application/json" \
  -d '{"customer_email": "customer@example.com", "items": ["Laptop", "Mouse"], "total": 1050.00}'

# 3. Check subscribers
curl http://localhost:8001/subscribers
```

## Depends on

- Python 3 with the packages in `webhooks/requirements.txt`.
