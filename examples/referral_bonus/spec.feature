Feature: Referral Bonus System
  As a business, I want to reward users who invite friends
  to increase user acquisition and engagement.

  Scenario: Successful Referral Bonus
    Given User A invites User B
    And User A has 50 reward points
    When User B makes a purchase of 60.0 USD
    Then User A receives 100 additional reward points
    And User A has a total of 150 reward points

  Scenario: Purchase Amount Too Low
    Given User A invites User B
    And User A has 50 reward points
    When User B makes a purchase of 30.0 USD
    Then User A receives 0 additional reward points
    And User A still has 50 reward points

  Scenario: No Referral Relationship
    Given User A has not invited User B
    And User A has 50 reward points
    When User B makes a purchase of 60.0 USD
    Then User A receives 0 additional reward points
    And User A still has 50 reward points

  Scenario: Invalid Purchase Amount
    Given User A invites User B
    When User B attempts a purchase of -10.0 USD
    Then system rejects the purchase with error "Invalid purchase amount"
    And User A receives 0 reward points
