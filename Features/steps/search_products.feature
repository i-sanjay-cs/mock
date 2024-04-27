Feature: Search functionality
As a user
I want to be able to search for products
So that I can find the products I need

Scenario Outline: Search for a product
    Given I am on the Home page of Amazon
    When I search for "<product>"
    Then I should see search results for "<product>"
