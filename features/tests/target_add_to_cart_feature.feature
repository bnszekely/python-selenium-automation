Feature: Target cart contains product test case

  Scenario: User can add a product to cart and confirm it is there
    Given Open Target main page
    When Search for notebook
    And Click add to cart button
    And Click View cart from Side Menu
    Then Verify notebook is in cart
