Feature: CRUD Contact

  Scenario: Access to Index page
    When I open Contact List website
    Then I verify that the count of Contacts is 0