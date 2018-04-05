Feature: Login to portal

  Scenario: Login and logout
    When I open automationpractice website
    And I login with username "javier@caballero.com" and password "36416999"
    Then I verify that I successfully logged in by logging out
