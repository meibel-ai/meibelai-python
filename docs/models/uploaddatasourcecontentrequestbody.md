# UploadDatasourceContentRequestBody


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `files`                                   | List[[models.Files](../models/files.md)]  | :heavy_check_mark:                        | Files to upload to the datasource         |
| `prefix`                                  | *Optional[str]*                           | :heavy_minus_sign:                        | Path prefix for organizing uploaded files |
| `extract_zip`                             | *Optional[bool]*                          | :heavy_minus_sign:                        | Auto-extract ZIP archives                 |
| `extract_eml`                             | *Optional[bool]*                          | :heavy_minus_sign:                        | Extract EML email files                   |
| `max_concurrent`                          | *Optional[int]*                           | :heavy_minus_sign:                        | Maximum concurrent file uploads           |