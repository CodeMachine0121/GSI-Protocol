"""
Implementation for Referral Bonus System
Implements: examples/referral_bonus/structure.py
Satisfies: examples/referral_bonus/spec.feature

Phase: 3 - Implementation
"""

from decimal import Decimal
from structure import (
    IReferralService,
    User,
    Purchase,
    ReferralResult,
    REFERRAL_BONUS_POINTS,
    MINIMUM_PURCHASE_AMOUNT
)


class ReferralService(IReferralService):
    """
    Concrete implementation of IReferralService.

    Scenario Coverage:
    - ✓ Successful Referral Bonus
    - ✓ Purchase Amount Too Low
    - ✓ No Referral Relationship
    - ✓ Invalid Purchase Amount
    """

    def process_referral_purchase(
        self,
        inviter: User,
        invitee: User,
        purchase: Purchase,
        has_referral_relationship: bool = True
    ) -> ReferralResult:
        """
        Process referral purchase and award points if applicable.

        Implements all scenarios from spec.feature:
        - Line 6: Successful Referral Bonus
        - Line 13: Purchase Amount Too Low
        - Line 20: No Referral Relationship
        - Line 27: Invalid Purchase Amount
        """

        # ============================================
        # Scenario: "Invalid Purchase Amount"
        # Given: User A invites User B
        # When: User B attempts a purchase of -10.0 USD
        # Then: system rejects with error "Invalid purchase amount"
        # ============================================
        if purchase.amount < 0:
            return ReferralResult(
                success=False,
                inviter=inviter,
                points_awarded=0,
                error_message="Invalid purchase amount"
            )

        # ============================================
        # Scenario: "No Referral Relationship"
        # Given: User A has not invited User B
        # When: User B makes a purchase of 60.0 USD
        # Then: User A receives 0 additional reward points
        # ============================================
        if not has_referral_relationship:
            return ReferralResult(
                success=True,
                inviter=inviter,
                points_awarded=0
            )

        # ============================================
        # Scenario: "Purchase Amount Too Low"
        # Given: User A invites User B, User A has 50 points
        # When: User B makes a purchase of 30.0 USD
        # Then: User A receives 0 additional reward points
        # ============================================
        if purchase.amount <= MINIMUM_PURCHASE_AMOUNT:
            return ReferralResult(
                success=True,
                inviter=inviter,
                points_awarded=0
            )

        # ============================================
        # Scenario: "Successful Referral Bonus"
        # Given: User A invites User B, User A has 50 points
        # When: User B makes a purchase of 60.0 USD
        # Then: User A receives 100 additional reward points
        #       And User A has a total of 150 reward points
        # ============================================
        if purchase.amount > MINIMUM_PURCHASE_AMOUNT:
            # Award bonus points
            updated_inviter = inviter.copy()
            updated_inviter.points += REFERRAL_BONUS_POINTS

            return ReferralResult(
                success=True,
                inviter=updated_inviter,
                points_awarded=REFERRAL_BONUS_POINTS
            )

        # Default case (should not reach here)
        return ReferralResult(
            success=False,
            inviter=inviter,
            points_awarded=0,
            error_message="Unhandled scenario"
        )


# ============================================
# Verification (Quick Checks)
# ============================================

def verify_implementation():
    """
    Quick verification that implementation matches Gherkin scenarios.
    This is NOT the official Phase 4 verification - just a sanity check.
    """
    service = ReferralService()

    print("Running quick verification checks...\n")

    # Test Scenario 1: Successful Referral Bonus
    print("Test 1: Successful Referral Bonus")
    user_a = User(id="A", points=50)
    user_b = User(id="B", points=0)
    purchase = Purchase(amount=Decimal("60.0"), currency="USD")

    result = service.process_referral_purchase(
        inviter=user_a,
        invitee=user_b,
        purchase=purchase,
        has_referral_relationship=True
    )

    assert result.success == True, "Should succeed"
    assert result.points_awarded == 100, f"Should award 100 points, got {result.points_awarded}"
    assert result.inviter.points == 150, f"Inviter should have 150 points, got {result.inviter.points}"
    print("✓ Scenario 1: Successful referral bonus - PASSED\n")

    # Test Scenario 2: Purchase Amount Too Low
    print("Test 2: Purchase Amount Too Low")
    user_a = User(id="A", points=50)
    user_b = User(id="B", points=0)
    purchase = Purchase(amount=Decimal("30.0"), currency="USD")

    result = service.process_referral_purchase(
        inviter=user_a,
        invitee=user_b,
        purchase=purchase,
        has_referral_relationship=True
    )

    assert result.success == True, "Should succeed"
    assert result.points_awarded == 0, f"Should award 0 points, got {result.points_awarded}"
    assert result.inviter.points == 50, f"Inviter should still have 50 points, got {result.inviter.points}"
    print("✓ Scenario 2: Purchase too low - PASSED\n")

    # Test Scenario 3: No Referral Relationship
    print("Test 3: No Referral Relationship")
    user_a = User(id="A", points=50)
    user_b = User(id="B", points=0)
    purchase = Purchase(amount=Decimal("60.0"), currency="USD")

    result = service.process_referral_purchase(
        inviter=user_a,
        invitee=user_b,
        purchase=purchase,
        has_referral_relationship=False  # No referral
    )

    assert result.success == True, "Should succeed"
    assert result.points_awarded == 0, f"Should award 0 points, got {result.points_awarded}"
    assert result.inviter.points == 50, f"Inviter should still have 50 points, got {result.inviter.points}"
    print("✓ Scenario 3: No referral relationship - PASSED\n")

    # Test Scenario 4: Invalid Purchase Amount
    print("Test 4: Invalid Purchase Amount")
    user_a = User(id="A", points=50)
    user_b = User(id="B", points=0)
    purchase = Purchase(amount=Decimal("-10.0"), currency="USD")

    result = service.process_referral_purchase(
        inviter=user_a,
        invitee=user_b,
        purchase=purchase,
        has_referral_relationship=True
    )

    assert result.success == False, "Should fail"
    assert result.points_awarded == 0, f"Should award 0 points, got {result.points_awarded}"
    assert result.error_message == "Invalid purchase amount", f"Wrong error message: {result.error_message}"
    print("✓ Scenario 4: Invalid purchase amount - PASSED\n")

    print("=" * 60)
    print("✅ All scenarios verified successfully!")
    print("=" * 60)
    print("\nReady for Phase 4: Formal Verification")


if __name__ == "__main__":
    verify_implementation()
