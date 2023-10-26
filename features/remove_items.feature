Feature: remove items from cart
    Scenario: Update and checkout to complete order
    Given lunch chrome browser
    When open shopping page
    Then Add few items to cart and verify the total count and price is displayed correctly
    Then Clear all items in cart and verify price & count is reset to 0
    And close browser