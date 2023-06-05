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

# RulesetCheckingToolOutputReport
|    Name     |                           Description                           | Data Type  | Units | Range | Req |                                                           Notes                                                           |
|-------------|-----------------------------------------------------------------|------------|-------|-------|-----|---------------------------------------------------------------------------------------------------------------------------|
| `title`     | Title of output report from Ruleset Checking Tool               | `String`   |       |       |     | Existing template value shows- ASHRAE STD 229P RULESET CHECKING TOOL                                                      |
| `purpose`   | Reason for the report                                           | `String`   |       |       |     | Existing template value shows- Project Testing Report                                                                     |
| `ruleset`   | References output that correspond to specific simulation model. | `String`   |       |       |     | Existing template value shows- ASHRAE 90.1-2019 Performance Rating Method (Appendix G)                                    |
| `date_run`  | Time stamp for the output report                                | `String`   |       |       |     | This does not seem exactly like a TimeStamp data type but close. Existing template value shows- 2022-02-01T18:25:43-05:00 |
| `rmd_files` | A list of names of RMD files                                    | `[String]` |       |       |     | Existing template value shows- user_rmr.json, baseline_rmr.json, proposed_rmr.json                                        |
| `rules`     | List of rule that is being evaluated                            | `[{Rule}]` |       |       |     |                                                                                                                           |

# Rule
|        Name        |               Description               |         Data Type         | Units | Range | Req |                          Notes                          |
|--------------------|-----------------------------------------|---------------------------|-------|-------|-----|---------------------------------------------------------|
| `rule_id`          | The identification of the specific rule | `String`                  |       |       |     | Existing template value shows- 1-1                      |
| `description`      | Textual description of the rule         | `String`                  |       |       |     | Existing template value shows- Description of rule 1-1. |
| `evaluation_type`  | Indicator if full evaluated rule        | `<EvaluationTypeOptions>` |       |       |     |                                                         |
| `standard_section` | Section number for rule                 | `String`                  |       |       |     | Existing template value shows- G3.1.2.2                 |
| `evaluations`      | List of evalations perfomed             | `[{Evaluation}]`          |       |       |     | Existing template value shows-                          |

# Evaluation
|        Name         |           Description            |       Data Type       | Units | Range | Req |                           Notes                           |
|---------------------|----------------------------------|-----------------------|-------|-------|-----|-----------------------------------------------------------|
| `id`                | Identifier                       | `Integer`             |       |       |     | Existing template value shows- 1                          |
| `outcome`           | Expected outcome                 | `<OutcomeOptions>`    |       |       |     | Existing template value shows- PASS                       |
| `messages`          | List of messages from evaluation | `[String]`            |       |       |     |                                                           |
| `calculated_values` |                                  | `[{CalculatedValue}]` |       |       |     | Not same as template since template shows key-value pairs |

# CalculatedValue
|    Name    | Description |      Data Type      | Units | Range | Req |                      Notes                       |
|------------|-------------|---------------------|-------|-------|-----|--------------------------------------------------|
| `variable` | Variable    | `String`            |       |       |     | Existing template value shows- calculated_value1 |
| `value`    | Value       | `(Numeric, String)` |       |       |     | Existing template value shows- 1.0               |

