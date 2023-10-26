Feature: apply filter and check products on ecommerce site
  Scenario: verify the filters in product listing page as Filter validations
    Given lunch chrome browser
    When open shopping page
    Then find the total products in the the shopping page
    Then add filter for XS size and verify product count
    Then add filter for xl size and verify product count
    Then find total count of xs products and xl products
    Then compare the total products with sum of xs products and xl size products
    And close browser

#  Scenario: Verify items are listed in cart in the order as added to cart with price
#    Given lunch chrome browser
#    When open product listing page
#    Then Add random 4 items with free shipping (items labelled as Free shipping) and Add 1 item without free shipping (items without Free shipping label)
#    Then Verify the order of items in cart and the price
#    And close browser
#
#  Scenario: Verify user is able to add same items as desired
#    Given lunch chrome browser
#    When open product listing page
#    Then Add a same item one or more times using ‘Add to cart’ button
#    Then verify the count & price is increased in cart accordingly
#    Then Add an item which is already present in the cart using ‘+’ button
#    Then verify the count & price is increased in cart accordingly
#    And close browser
#
#  Scenario: Update and checkout to complete order
#    Given lunch chrome browser
#    When open product listing page
#    Then Verify user can delete items in cart
#    Then Add few items to cart and verify the total count and price is displayed correctly
#    Then Clear all items in cart and verify price & count is reset to 0
#    Then verify the count & price is increased in cart accordingly
#    And close browser
#
#  Scenario: Verify user is able to place order
#    Given lunch chrome browser
#    When open product listing page
#    Then Add few items to cart and click on “checkout”
#    Then verify alert message is displayed with correct price same as cart
#    Then Verify items in cart is reset on refreshing the page
#    And close browser