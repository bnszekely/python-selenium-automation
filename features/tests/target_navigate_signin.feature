Feature: Logged out user can navigate to Sign In

  Scenario: Logged out user can click on Sign In and correct form opens
   Given Open target main page
    When Click Sign In
    And Click Sign In from Drawer
    Then Verify Sign In Form Opens


  Scenario: Verify user can Login
    Given Open Target main page
    When Click Sign In
    And Click Sign In from Drawer
    And Input email and password on SignIn Page
    And Click Sign In on SignIn Page
    Then Verify user is logged in


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click Sign In
    And Click Sign In from Drawer
    And Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window
    And User can switch back to original window