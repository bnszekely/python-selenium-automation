# Created by brittanyszekely at 3/13/25
Feature: Logged out user can navigate to Sign In


  Scenario: Logged out user can click on Sign In and correct form opens
   Given Open target main page
    When Click Sign In
    And Click Sign In from Right Side Menu
    Then Verify Sign In Form Opens