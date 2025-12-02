Feature: VIP Discount System
  As a business, I want to reward VIP customers with discounts
  to increase customer loyalty and repeat purchases.

  Scenario: Apply 20% discount to VIP user
    Given user is VIP
    When user makes a purchase of 1000 USD
    Then final price should be 800 USD
    And discount amount should be 200 USD

  Scenario: No discount for normal users
    Given user is NORMAL
    When user makes a purchase of 1000 USD
    Then final price should be 1000 USD
    And discount amount should be 0 USD

  Scenario: No discount for purchases under threshold
    Given user is VIP
    When user makes a purchase of 50 USD
    Then final price should be 50 USD
    And discount amount should be 0 USD

  Scenario: Reject invalid purchase amount
    Given user is VIP
    When user attempts a purchase of -100 USD
    Then system should reject with error "Invalid purchase amount"
