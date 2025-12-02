"""
Structural Design for Referral Bonus System
Generated from: examples/referral_bonus/spec.feature

This module defines the data models and service interfaces
required to implement the Gherkin scenarios.

Phase: 2 - Architecture
"""

from pydantic import BaseModel, Field, validator
from abc import ABC, abstractmethod
from typing import Optional
from decimal import Decimal


# ============================================
# Data Models (Nouns from Gherkin)
# ============================================

class User(BaseModel):
    """
    Represents a user in the system.

    Source Scenarios:
    - "Successful Referral Bonus" (Given User A/B)
    - "Purchase Amount Too Low" (Given User A/B)
    """
    id: str = Field(..., description="Unique user identifier")
    points: int = Field(default=0, ge=0, description="Reward points balance (from Given/Then)")

    @validator('points')
    def validate_points(cls, v):
        """Points must be non-negative."""
        if v < 0:
            raise ValueError("Points cannot be negative")
        return v


class Purchase(BaseModel):
    """
    Represents a purchase transaction.

    Source Scenarios:
    - "Successful Referral Bonus" (When...purchase of 60.0 USD)
    - "Invalid Purchase Amount" (When...purchase of -10.0 USD)
    """
    amount: Decimal = Field(..., description="Purchase amount in USD")
    currency: str = Field(default="USD", description="Currency code")

    @validator('amount')
    def validate_amount(cls, v):
        """
        Amount validation implied by error scenario.
        From: Scenario "Invalid Purchase Amount"
        """
        if v < 0:
            raise ValueError("Invalid purchase amount")
        return v


class ReferralResult(BaseModel):
    """
    Represents the outcome of processing a referral purchase.

    Source Scenarios:
    - All scenarios (Then statements)
    """
    success: bool = Field(..., description="Whether operation succeeded")
    inviter: User = Field(..., description="Updated inviter with new points")
    points_awarded: int = Field(default=0, description="Points awarded in this transaction")
    error_message: Optional[str] = Field(None, description="Error message if success=False")


# ============================================
# Service Interfaces (Verbs from Gherkin)
# ============================================

class IReferralService(ABC):
    """
    Interface for Referral Bonus Service.

    Implements scenarios from: examples/referral_bonus/spec.feature

    All scenarios must be satisfied by implementations of this interface.
    """

    @abstractmethod
    def process_referral_purchase(
        self,
        inviter: User,
        invitee: User,
        purchase: Purchase,
        has_referral_relationship: bool = True
    ) -> ReferralResult:
        """
        Process a purchase and award referral bonus if applicable.

        Satisfies Scenarios:
        - Scenario: "Successful Referral Bonus" (line 6)
        - Scenario: "Purchase Amount Too Low" (line 13)
        - Scenario: "No Referral Relationship" (line 20)
        - Scenario: "Invalid Purchase Amount" (line 27)

        Business Rules (from Gherkin):
        - Referral bonus: 100 points
        - Minimum purchase threshold: $50 USD
        - Only awarded if referral relationship exists
        - Invalid purchases are rejected

        Args:
            inviter: The user who made the referral
            invitee: The user who was invited (making the purchase)
            purchase: The purchase transaction details
            has_referral_relationship: Whether inviter referred invitee

        Returns:
            ReferralResult containing:
            - success: True if operation completed, False if error
            - inviter: Updated User object with new point balance
            - points_awarded: Number of points awarded (0 or 100)
            - error_message: Error description if success=False

        Scenario Mapping:
        - When purchase >= $50 AND referral exists: award 100 points
        - When purchase < $50 OR no referral: award 0 points
        - When purchase < 0: reject with error
        """
        pass


# ============================================
# Constants (Business Rules from Gherkin)
# ============================================

REFERRAL_BONUS_POINTS = 100  # From: "Then User A receives 100 additional reward points"
MINIMUM_PURCHASE_AMOUNT = Decimal("50.0")  # Inferred from scenarios (boundary at $50)
