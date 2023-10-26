Feature: Add same product by ‘Add to cart’ button & ‘+’ button
Scenario: Verify user is able to add same items as desired
    Given lunch chrome browser
    When open shopping page
    Then Add a same item more than 1 times using ‘Add to cart’ button
    Then verify the count & price is increased in cart accordingly
    Then Add an item which is already present in the cart using ‘+’ button
    Then verify the count & price is increased in cart accordingly after that
    And close browser