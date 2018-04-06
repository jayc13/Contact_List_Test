Feature: CRUD Contact

	Scenario: Access to Index page
    	Given I open Contact List website
    	Then I verify that the count of Contacts is 0

	Scenario: Create a Contact
    	Given I open Contact List website
    	When I access to create contact page
    	And I create a new Contact with random values
    	And I back to home page from a show contact page
    	Then I verify that the count of Contacts is 1

    Scenario: Edit a Contact
    	Given I open Contact List website
    	When I verify that the count of Contacts is 1
    	And I go to edit one contact
    	And I edit a current Contact with random values
    	And I back to home page from a show contact page
    	Then I verify that the count of Contacts is 1

    Scenario: Delete a Contact
    	Given I open Contact List website
    	When I verify that the count of Contacts is 1
    	And I delete one contact
    	Then I verify that the count of Contacts is 0
