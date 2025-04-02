Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in url


  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for notebook
    And Click add to cart button
    And Confirm add to cart from side menu
    And Click View cart from Side Menu
    Then Verify notebook is in cart
