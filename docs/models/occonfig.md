# OCConfig

Configuration for Observed Consistency confidence scoring.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `n_completions`                                                  | *OptionalNullable[int]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `max_tokens`                                                     | *OptionalNullable[int]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `temperature`                                                    | [OptionalNullable[models.Temperature]](../models/temperature.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `models`                                                         | List[*Nullable[str]*]                                            | :heavy_minus_sign:                                               | N/A                                                              |
| `nli_model_config`                                               | Dict[str, *Any*]                                                 | :heavy_check_mark:                                               | N/A                                                              |
| `n_bootstraps`                                                   | [OptionalNullable[models.NBootstraps]](../models/nbootstraps.md) | :heavy_minus_sign:                                               | N/A                                                              |
| `token_limit`                                                    | *OptionalNullable[int]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `original_completion`                                            | *OptionalNullable[str]*                                          | :heavy_minus_sign:                                               | N/A                                                              |
| `comparison_completions`                                         | List[*str*]                                                      | :heavy_minus_sign:                                               | N/A                                                              |