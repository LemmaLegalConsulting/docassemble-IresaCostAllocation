Feature: Complete IresaCostAllocation interview

  # Reviewed against the interview and its local includes.
  # Static ALDashboard draft curated to the chosen branch; browser validation runs in CI.
  # The summary is terminal on the parent branch; placeholder_ending is not reached.
  Scenario: Complete IresaCostAllocation and verify the result
    Given I start the interview at "main.yml"
    And the maximum seconds for each Step is 300
    And the user gets to "summary" with this data:
      | var | value |
      | welcome | True |
      | users[0].name.first | Maria |
      | users[0].name.last | Schmidt |
      | users[0].role | parent |
      | recipient[0].name.first | Anna |
      | recipient[0].name.last | Schmidt |
      | recipient[0].birthdate | 01/01/2010 |
      | service_category | service_1_1 |
      | users[0].pregnant | False |
      | users[0].lives_with_recipient | True |
      | monthly_cost | 1000 |
      | child_benefit | False |
      | cash_benefit | False |
      | users[0].monthly_income | 3000 |
      | other_recipients_same_benefit | False |
      | impacted_maint_rights | True |
      | impacted_maint_rights_num | 1 |
    Then I should see the phrase "Summary of your responses:"
