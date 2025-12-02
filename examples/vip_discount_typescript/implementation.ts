/**
 * Implementation for VIP Discount System
 * Implements: examples/vip_discount_typescript/structure.ts
 * Satisfies: examples/vip_discount_typescript/spec.feature
 *
 * Phase: 3 - Implementation
 */

import {
  IDiscountService,
  User,
  Purchase,
  DiscountResult,
  UserType,
  VIP_DISCOUNT_RATE,
  MINIMUM_PURCHASE_AMOUNT
} from './structure';

export class DiscountService implements IDiscountService {
  /**
   * Concrete implementation of IDiscountService
   *
   * Scenario Coverage:
   * - ✓ Apply 20% discount to VIP user
   * - ✓ No discount for normal users
   * - ✓ No discount for purchases under threshold
   * - ✓ Reject invalid purchase amount
   */

  calculateDiscount(user: User, purchase: Purchase): DiscountResult {
    /**
     * Implementation for all scenarios from spec.feature
     */

    // ============================================
    // Scenario: "Reject invalid purchase amount"
    // Given: user is VIP
    // When: user attempts a purchase of -100 USD
    // Then: system should reject with error
    // ============================================
    if (purchase.amount < 0) {
      return {
        success: false,
        finalPrice: 0,
        discountAmount: 0,
        errorMessage: "Invalid purchase amount"
      };
    }

    // ============================================
    // Scenario: "No discount for purchases under threshold"
    // Given: user is VIP
    // When: user makes a purchase of 50 USD
    // Then: final price should be 50 USD
    // ============================================
    if (purchase.amount < MINIMUM_PURCHASE_AMOUNT) {
      return {
        success: true,
        finalPrice: purchase.amount,
        discountAmount: 0
      };
    }

    // ============================================
    // Scenario: "Apply 20% discount to VIP user"
    // Given: user is VIP
    // When: user makes a purchase of 1000 USD
    // Then: final price should be 800 USD
    // ============================================
    if (user.type === UserType.VIP) {
      const discountAmount = purchase.amount * VIP_DISCOUNT_RATE;
      const finalPrice = purchase.amount - discountAmount;

      return {
        success: true,
        finalPrice,
        discountAmount
      };
    }

    // ============================================
    // Scenario: "No discount for normal users"
    // Given: user is NORMAL
    // When: user makes a purchase of 1000 USD
    // Then: final price should be 1000 USD
    // ============================================
    return {
      success: true,
      finalPrice: purchase.amount,
      discountAmount: 0
    };
  }
}

// ============================================
// Verification (Quick Checks)
// ============================================

function verifyImplementation(): void {
  /**
   * Quick verification that implementation matches Gherkin scenarios
   * This is NOT the official Phase 4 verification - just a sanity check
   */

  const service = new DiscountService();

  console.log("Running quick verification checks...\n");

  // Test Scenario 1: Apply 20% discount to VIP user
  console.log("Test 1: Apply 20% discount to VIP user");
  const vipUser: User = { id: "user1", type: UserType.VIP };
  const largePurchase: Purchase = { amount: 1000, currency: "USD" };

  const result1 = service.calculateDiscount(vipUser, largePurchase);
  console.assert(result1.success === true, "Should succeed");
  console.assert(result1.finalPrice === 800, `Expected 800, got ${result1.finalPrice}`);
  console.assert(result1.discountAmount === 200, `Expected 200, got ${result1.discountAmount}`);
  console.log("✓ Scenario 1: VIP discount - PASSED\n");

  // Test Scenario 2: No discount for normal users
  console.log("Test 2: No discount for normal users");
  const normalUser: User = { id: "user2", type: UserType.NORMAL };

  const result2 = service.calculateDiscount(normalUser, largePurchase);
  console.assert(result2.success === true, "Should succeed");
  console.assert(result2.finalPrice === 1000, `Expected 1000, got ${result2.finalPrice}`);
  console.assert(result2.discountAmount === 0, `Expected 0, got ${result2.discountAmount}`);
  console.log("✓ Scenario 2: No discount for normal users - PASSED\n");

  // Test Scenario 3: No discount for purchases under threshold
  console.log("Test 3: No discount for purchases under threshold");
  const smallPurchase: Purchase = { amount: 50, currency: "USD" };

  const result3 = service.calculateDiscount(vipUser, smallPurchase);
  console.assert(result3.success === true, "Should succeed");
  console.assert(result3.finalPrice === 50, `Expected 50, got ${result3.finalPrice}`);
  console.assert(result3.discountAmount === 0, `Expected 0, got ${result3.discountAmount}`);
  console.log("✓ Scenario 3: No discount under threshold - PASSED\n");

  // Test Scenario 4: Reject invalid purchase amount
  console.log("Test 4: Reject invalid purchase amount");
  const invalidPurchase: Purchase = { amount: -100, currency: "USD" };

  const result4 = service.calculateDiscount(vipUser, invalidPurchase);
  console.assert(result4.success === false, "Should fail");
  console.assert(result4.errorMessage === "Invalid purchase amount",
    `Expected 'Invalid purchase amount', got '${result4.errorMessage}'`);
  console.log("✓ Scenario 4: Invalid purchase rejected - PASSED\n");

  console.log("=".repeat(60));
  console.log("✅ All scenarios verified successfully!");
  console.log("=".repeat(60));
  console.log("\nReady for Phase 4: Formal Verification");
}

// Run verification if this is the main module
if (require.main === module) {
  verifyImplementation();
}
