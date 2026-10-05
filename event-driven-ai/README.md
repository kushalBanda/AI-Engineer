# Event-driven AI

[← AI Engineer](../README.md)

AI systems react to events: a push, a payment, a new message. This shelf covers how events reach your code (webhooks) and how you stream them between services (Kafka).

## Modules

| Module | What you'll build | Tier | Stack |
| :--- | :--- | :--- | :--- |
| [`webhooks/`](webhooks/) | An order notification system. One sender fans out to inventory, email, and analytics receivers | Beginner | FastAPI |
| [`github-sync/`](github-sync/) | A GitHub dashboard. A React client, a FastAPI server, and a Kafka producer and consumer | Advanced | React, Vite, FastAPI, Kafka |

## Reading order

1. `webhooks/`: learn the sender and receiver pattern first.
2. `github-sync/`: add a message broker and a full-stack client.

## Articles

Coming soon.
