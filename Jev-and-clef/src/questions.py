"""The four triage questions, sent together in one Decisions request per ticket.

`category` and `intent` have ground-truth labels in the Bitext dataset and are
scored for accuracy. `urgency` and `needs_human` are unlabelled, so the report
compares how often the models agree on them.
"""

from collections.abc import Mapping
from typing import Any, Final

CATEGORIES: Final[Mapping[str, str]] = {
    "ACCOUNT": (
        "Creating, editing, deleting or switching an account, password recovery, sign-up problems"
    ),
    "CANCEL": "Asking about the fee for cancelling a service or contract",
    "CONTACT": "Wants to reach customer service or a human agent",
    "DELIVERY": "Delivery options, carriers, or how long delivery takes",
    "FEEDBACK": "Leaving a complaint or a review about the service",
    "INVOICE": "Viewing, checking or downloading an invoice or bill",
    "ORDER": "Placing, changing, cancelling or tracking an order",
    "PAYMENT": "Accepted payment methods or a problem making a payment",
    "REFUND": "Refund policy, requesting a refund, or tracking a refund",
    "SHIPPING": "Setting up or changing a shipping address",
    "SUBSCRIPTION": "Subscribing to or unsubscribing from the newsletter",
}

INTENTS: Final[Mapping[str, str]] = {
    "cancel_order": "Cancel an order already placed",
    "change_order": "Modify items or details of an existing order",
    "change_shipping_address": "Change an existing shipping address",
    "check_cancellation_fee": "Ask what cancelling will cost",
    "check_invoice": "Look at or verify an invoice",
    "check_payment_methods": "Ask which payment methods are accepted",
    "check_refund_policy": "Ask about the refund or money-back policy",
    "complaint": "Complain about the service, product or staff",
    "contact_customer_service": "Ask how to reach customer service",
    "contact_human_agent": "Ask to talk to a real person instead of a bot",
    "create_account": "Open or sign up for a new account",
    "delete_account": "Close or remove an account",
    "delivery_options": "Ask which delivery or shipping methods exist",
    "delivery_period": "Ask when an item will arrive or how long delivery takes",
    "edit_account": "Update profile or account details",
    "get_invoice": "Request or download an invoice",
    "get_refund": "Request money back",
    "newsletter_subscription": "Subscribe to or unsubscribe from the newsletter",
    "payment_issue": "Report a failed or problematic payment",
    "place_order": "Buy something or start a new order",
    "recover_password": "Reset or recover a forgotten password",
    "registration_problems": "Report an error while signing up",
    "review": "Leave a review or general feedback",
    "set_up_shipping_address": "Add a new shipping address",
    "switch_account": "Change to a different account or plan",
    "track_order": "Ask where an order is or its status",
    "track_refund": "Ask about the status of a refund already requested",
}

URGENCY_LEVELS: Final[tuple[str, ...]] = (
    "Low: general question, no time pressure",
    "Medium: customer is inconvenienced but can wait",
    "High: customer is blocked, losing money, or clearly upset",
    "Critical: security risk, repeated failure, or threat to leave or take legal action",
)

QUESTIONS: Final[Mapping[str, Mapping[str, Any]]] = {
    "category": {
        "type": "choice",
        "instructions": "Which support category does this customer message belong to?",
        "criteria": dict(CATEGORIES),
    },
    "intent": {
        "type": "choice",
        "instructions": "What exactly does the customer want to do?",
        "criteria": dict(INTENTS),
    },
    "urgency": {
        "type": "score",
        "instructions": "How urgent is this customer message?",
        "criteria": list(URGENCY_LEVELS),
    },
    "needs_human": {
        "type": "noul",
        "instructions": "Should a human agent handle this message instead of an automated reply?",
        "criteria": {
            "true": (
                "It involves money, account security, an angry customer, "
                "or an explicit request for a person"
            ),
            "false": "A routine question that a help-center article or automated reply can answer",
        },
    },
}


def build_state(ticket: str) -> dict[str, str]:
    """Wrap a ticket in the state object the models reason over."""
    return {"context": "Customer support inbox for an online store.", "ticket": ticket}
