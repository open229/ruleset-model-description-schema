# OutcomeOptions
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `PASS`           | Pass           |       |
| `FAIL`           | Fail           |       |
| `NOT_APPLICABLE` | Not applicable |       |
| `UNDETERMINED`   | Undetermined   |       |

# EvaluationTypeOptions
|   Enumerator    |       Description        | Notes |
|-----------------|--------------------------|-------|
| `FULL`          | Full Evaluation          |       |
| `APPLICABILITY` | Applicability Evaluation |       |

# RulesetCheckingToolSoftwareOutputReport
|       Name       |                           Description                           |   Data Type    | Units | Range | Req |                                                           Notes                                                           |
|------------------|-----------------------------------------------------------------|----------------|-------|-------|-----|---------------------------------------------------------------------------------------------------------------------------|
| `title`          | Title of software output report from Ruleset Checking Tool      | `String`       |       |       |     | Existing template value shows- RULESET CHECKING TOOL                                                                      |
| `purpose`        | Reason for the report                                           | `String`       |       |       |     | Existing template value shows- RCT Ruleset Software Testing Report                                                        |
| `ruleset`        | References output that correspond to specific simulation model. | `String`       |       |       |     | Existing template value shows- ASHRAE 90.1-2019 Performance Rating Method (Appendix G)                                    |
| `date_run`       | Time stamp for the output report                                | `String`       |       |       |     | This does not seem exactly like a TimeStamp data type but close. Existing template value shows- 2023-03-16T14:45:33-05:00 |
| `schema_version` | Version of the schema corresponding to the tests.               | `String`       |       |       |     | Existing template value shows- 0.0.23                                                                                     |
| `rules_tests`    | List of rule that is being evaluated                            | `[{RuleTest}]` |       |       |     |                                                                                                                           |

# RuleTest
|                     Name                     |                        Description                        |         Data Type         | Units | Range | Req |                                                                                                                                                        Notes                                                                                                                                                         |
|----------------------------------------------|-----------------------------------------------------------|---------------------------|-------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `rule_id`                                    | The identification of the specific rule                   | `String`                  |       |       |     | Existing template value shows- 5-5                                                                                                                                                                                                                                                                                   |
| `test_id`                                    | The identification of the test case for the specific rule | `String`                  |       |       |     | Existing template value shows- a                                                                                                                                                                                                                                                                                     |
| `test_description`                           | Textual description of the test for the rule              | `String`                  |       |       |     | Existing template value shows- Description of rule: Building is located in climate zone 4A and includes a space that has residential occupancy type and is conditioned based on heating capacity of the HVAC system that servies the parent zone. The baseline roof U-factor for the space is established correctly. |
| `ruleset_section`                            | Section reference from the ruleset                        | `String`                  |       |       |     | Existing template value shows- Table G3.1(5) Baseline Building Performance (b)                                                                                                                                                                                                                                       |
| `ruleset_section_title`                      | Title of the section referenced from the ruleset          | `String`                  |       |       |     | Existing template value shows- Envelope                                                                                                                                                                                                                                                                              |
| `evaluation_type`                            | Indicator if full evaluated rule                          | `<EvaluationTypeOptions>` |       |       |     |                                                                                                                                                                                                                                                                                                                      |
| `rule_unit_test_outcome_agreement`           | True if the expected and actual agree                     | `Boolean`                 |       |       |     | Existing template value shows- false                                                                                                                                                                                                                                                                                 |
| `expected_rule_unit_test_evaluation_outcome` | Expected outcome                                          | `<OutcomeOptions>`        |       |       |     | Existing template value shows- PASS                                                                                                                                                                                                                                                                                  |
| `actual_rule_unit_test_evaluation_outcome`   | Expected outcome                                          | `<OutcomeOptions>`        |       |       |     | Existing template value shows- UNDETERMINED                                                                                                                                                                                                                                                                          |
| `rule_unit_test_evaluations`                 | List of evalations perfomed                               | `[{Evaluation}]`          |       |       |     | Existing template value shows-                                                                                                                                                                                                                                                                                       |

# Evaluation
|         Name         |                   Description                   |       Data Type       | Units | Range | Req |                                     Notes                                      |
|----------------------|-------------------------------------------------|-----------------------|-------|-------|-----|--------------------------------------------------------------------------------|
| `data_group`         | Reference to a data group being evaluated       | `Reference`           |       |       |     | Can reference any type of data group. Existing template value shows- Surface 1 |
| `messages`           | List of messages from evaluation                | `[String]`            |       |       |     | Existing template value shows- message                                         |
| `evaluation_outcome` | Expected outcome                                | `<OutcomeOptions>`    |       |       |     | Existing template value shows- PASS                                            |
| `calculated_values`  | a list of calculated values from the evaluation | `[{CalculatedValue}]` |       |       |     | Used to help understand and debug rule evaulation                              |

# CalculatedValue
|    Name    |   Description    |      Data Type      | Units | Range | Req |                           Notes                            |
|------------|------------------|---------------------|-------|-------|-----|------------------------------------------------------------|
| `variable` | Variable         | `String`            |       |       |     | Existing template value shows- roof_u_factor               |
| `value`    | Value with Units | `(Numeric, String)` |       |       |     | As an example- 5 Btu. Existing template value shows- 0.063 |

