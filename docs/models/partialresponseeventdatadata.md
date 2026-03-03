# PartialResponseEventDataData


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `message`                                                | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `clean_message`                                          | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `citations`                                              | List[[models.Citations](../models/citations.md)]         | :heavy_minus_sign:                                       | N/A                                                      |
| `sources`                                                | List[[models.Sources](../models/sources.md)]             | :heavy_minus_sign:                                       | N/A                                                      |
| `follow_up_questions`                                    | List[*str*]                                              | :heavy_minus_sign:                                       | N/A                                                      |
| `call_to_actions`                                        | List[[models.CallToActions](../models/calltoactions.md)] | :heavy_minus_sign:                                       | N/A                                                      |
| `artifacts`                                              | List[[models.Artifacts](../models/artifacts.md)]         | :heavy_minus_sign:                                       | N/A                                                      |