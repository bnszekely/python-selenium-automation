# Created by brittanyszekely at 3/13/25
Feature: Target cart is empty test case


  Scenario: User can click on cart icon and correct message is shown
    Given Open target main page
    When Click on Cart Icon
    Then Verify correct message is shown