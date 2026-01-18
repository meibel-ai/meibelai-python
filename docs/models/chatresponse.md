# ChatResponse

The structured chat response.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `message`                                              | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `sources`                                              | List[[models.Source](../models/source.md)]             | :heavy_minus_sign:                                     | N/A                                                    |
| `follow_up_questions`                                  | List[*str*]                                            | :heavy_minus_sign:                                     | N/A                                                    |
| `call_to_actions`                                      | List[[models.CallToAction](../models/calltoaction.md)] | :heavy_minus_sign:                                     | N/A                                                    |
| `artifacts`                                            | List[[models.Artifact](../models/artifact.md)]         | :heavy_minus_sign:                                     | N/A                                                    |