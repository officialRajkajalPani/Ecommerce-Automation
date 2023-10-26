 Feature: Verify user is able to place order
  Scenario: Verify user is able to place order
      Given lunch chrome browser
      When open shopping page
      Then Add few items to cart and click on “checkout”
      Then verify alert message is displayed with correct price same as cart
      Then Verify items in cart is reset on refreshing the page
      And close browser