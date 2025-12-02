/**
 * Structural Design for VIP Discount System
 * Source: examples/vip_discount_typescript/spec.feature
 * Phase: 2 - Architecture
 */

// ============================================
// Enumerations (from categorical nouns)
// ============================================

/**
 * User type enum from Gherkin scenarios
 * Source: "Given user is VIP" and "Given user is NORMAL"
 */
export enum UserType {
  VIP = "VIP",
  NORMAL = "NORMAL"
}

// ============================================
// Data Models (from nouns in Gherkin)
// ============================================

/**
 * Represents a user in the system
 * Source: "Given user is VIP/NORMAL"
 */
export interface User {
  id: string;
  type: UserType;
}

/**
 * Represents a purchase transaction
 * Source: "When user makes a purchase of X USD"
 */
export interface Purchase {
  amount: number;
  currency: string;
}

/**
 * Represents the discount calculation result
 * Source: "Then final price should be X USD"
 */
export interface DiscountResult {
  /** Whether the operation succeeded */
  success: boolean;

  /** Final price after discount */
  finalPrice: number;

  /** Discount amount applied */
  discountAmount: number;

  /** Error message if success is false */
  errorMessage?: string;
}

// ============================================
// Service Interfaces (from verbs in Gherkin)
// ============================================

/**
 * Interface for VIP Discount Service
 * Implements scenarios from: spec.feature
 *
 * All scenarios must be satisfied by implementations of this interface.
 */
export interface IDiscountService {
  /**
   * Calculate discount for a purchase based on user type
   *
   * Satisfies Scenarios:
   * - "Apply 20% discount to VIP user" (line 6)
   * - "No discount for normal users" (line 12)
   * - "No discount for purchases under threshold" (line 18)
   * - "Reject invalid purchase amount" (line 24)
   *
   * Business Rules (from Gherkin):
   * - VIP users get 20% discount
   * - Minimum purchase threshold: $100 USD
   * - Normal users pay full price
   * - Negative amounts are rejected
   *
   * @param user - The user making the purchase
   * @param purchase - The purchase transaction details
   * @returns DiscountResult with final price and discount amount
   */
  calculateDiscount(user: User, purchase: Purchase): DiscountResult;
}

// ============================================
// Constants (Business Rules from Gherkin)
// ============================================

/** VIP discount rate: 20% (inferred from 1000 -> 800) */
export const VIP_DISCOUNT_RATE = 0.20;

/** Minimum purchase amount for discount: $100 (inferred from scenarios) */
export const MINIMUM_PURCHASE_AMOUNT = 100;
