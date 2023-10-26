Feature: add products on ecommerce site
Scenario: Verify items are listed in cart in the order as added to cart with price
    Given lunch chrome browser
    When open shopping page
    Then Add random 4 items with free shipping tag (items labelled as Free shipping)
    Then Add 1 item without free shipping tag (items without Free shipping label)
    Then Verify the order of items in cart and the price
    And close browser