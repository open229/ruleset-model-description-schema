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

# RulesetCheckingToolProjectOutputReport
|       Name       |                               Description                                |       Data Type       | Units | Range | Req |                                         Notes                                          |
|------------------|--------------------------------------------------------------------------|-----------------------|-------|-------|-----|----------------------------------------------------------------------------------------|
| `title`          | Title of project output report from Ruleset Checking Tool                | `String`              |       |       |     | Existing template value shows- ASHRAE STD 229P RULESET CHECKING TOOL                   |
| `purpose`        | Reason for the report                                                    | `String`              |       |       |     | Existing template value shows- Project Testing Report                                  |
| `ruleset`        | Names the ruleset including appropriate year, organization, and section. | `String`              |       |       |     | Existing template value shows- ASHRAE 90.1-2019 Performance Rating Method (Appendix G) |
| `date_run`       | Time stamp for the output report                                         | `Timestamp`           |       |       |     | Existing template value shows- 2022-02-01T18:25:43-05:00                               |
| `schema_version` | Version of the schema corresponding to the tests.                        | `String`              |       |       |     |                                                                                        |
| `rmd_files`      | A list of names of RMD files                                             | `[{FileDescription}]` |       |       |     | Existing template value shows- user_rmr.json, baseline_rmr.json, proposed_rmr.json     |
| `rules`          | List of rule that is being evaluated                                     | `[{Rule}]`            |       |       |     |                                                                                        |

# Rule
|        Name        |               Description               |         Data Type         | Units | Range | Req |                          Notes                          |
|--------------------|-----------------------------------------|---------------------------|-------|-------|-----|---------------------------------------------------------|
| `rule_id`          | The identification of the specific rule | `String`                  |       |       |     | Existing template value shows- 1-1                      |
| `description`      | Textual description of the rule         | `String`                  |       |       |     | Existing template value shows- Description of rule 1-1. |
| `evaluation_type`  | Indicator if full evaluated rule        | `<EvaluationTypeOptions>` |       |       |     |                                                         |
| `standard_section` | Section number for rule                 | `String`                  |       |       |     | Existing template value shows- G3.1.2.2                 |
| `evaluations`      | List of evalations perfomed             | `[{Evaluation}]`          |       |       |     | Existing template value shows-                          |

# Evaluation
|        Name         |                Description                |       Data Type       | Units | Range | Req |                                 Notes                                  |
|---------------------|-------------------------------------------|-----------------------|-------|-------|-----|------------------------------------------------------------------------|
| `data_group`        | Reference to a data group being evaluated | `Reference`           |       |       |     | Can reference any type of data group. Existing template value shows- 1 |
| `outcome`           | Outcome                                   | `<OutcomeOptions>`    |       |       |     | Existing template value shows- PASS                                    |
| `messages`          | List of messages from evaluation          | `[String]`            |       |       |     |                                                                        |
| `calculated_values` |                                           | `[{CalculatedValue}]` |       |       |     | Not same as template since template shows key-value pairs              |

# CalculatedValue
|    Name    |   Description    |      Data Type      | Units | Range | Req |                      Notes                       |
|------------|------------------|---------------------|-------|-------|-----|--------------------------------------------------|
| `variable` | Variable         | `String`            |       |       |     | Existing template value shows- calculated_value1 |
| `value`    | Value with Units | `(Numeric, String)` |       |       |     | Existing template value shows- 1.0               |

# FileDescription
|         Name         |                      Description                      |              Data Type               | Units | Range | Req |                                                                              Notes                                                                              |
|----------------------|-------------------------------------------------------|--------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ruleset_model_type` | Describes the type of model associated with the file. | `<RulesetModelOptions2019ASHRAE901>` |       |       |     | For 90.1 Appendix G would be USER, PROPOSED, BASELINE_0, BASELINE_90, BASELINE_180, BASELINE_270                                                                |
| `file_name`          | Value                                                 | `String`                             |       |       |     | The name of the json file with file extension and may include the file path. Existing template value shows- user_rmr.json, baseline_rmr.json, proposed_rmr.json |

