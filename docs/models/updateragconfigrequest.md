# UpdateRagConfigRequest

UpdateRagConfigRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `description`                                                                      | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `collection_id`                                                                    | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `extractor_model`                                                                  | [OptionalNullable[models.ExtractorModel]](../models/extractormodel.md)             | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `embedding_model`                                                                  | [OptionalNullable[models.EmbeddingModel]](../models/embeddingmodel.md)             | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `sparse_embedding_model`                                                           | [OptionalNullable[models.SparseEmbeddingModel]](../models/sparseembeddingmodel.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `collect_metadata`                                                                 | *OptionalNullable[bool]*                                                           | :heavy_minus_sign:                                                                 | N/A                                                                                |