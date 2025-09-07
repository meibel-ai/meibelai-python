# AddBlueprintRequest

AddBlueprintRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `version`                                          | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `description`                                      | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `dsl_definition`                                   | [models.DslDefinition](../models/dsldefinition.md) | :heavy_check_mark:                                 | DslDefinition                                      |
| `yaml_spec_content`                                | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `json_spec_content`                                | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |