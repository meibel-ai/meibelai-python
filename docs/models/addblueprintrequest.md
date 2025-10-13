# AddBlueprintRequest

AddBlueprintRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `execution_mode`                                   | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `version`                                          | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `description`                                      | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `dsl_definition`                                   | [models.DslDefinition](../models/dsldefinition.md) | :heavy_check_mark:                                 | DslDefinition                                      |
| `yaml_spec_content`                                | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `json_spec_content`                                | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |
| `workflow_type`                                    | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `workflow_task_queue`                              | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `init_input`                                       | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |