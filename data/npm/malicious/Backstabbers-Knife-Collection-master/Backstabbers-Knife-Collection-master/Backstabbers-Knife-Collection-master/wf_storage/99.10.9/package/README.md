A module that manages file storage

## Supported storage engines

### AWS S3 storage

Allows to store files in AWS S3 buckets.

Options:

```
var storageConfig = {
  s3: {
    s3Options: {
      accessKeyId: process.env.AWS_S3_ACCESS_KEY,
      secretAccessKey: process.env.AWS_S3_ACCESS_KEY_SECRET,
      region: process.env.AWS_S3_REGION
    },
    bucket: "my-files"
  }
}
require('wf-storage')(mediator, storageConfig);
```

### Gridfs MongoDB storage

Allows to store file in MongoDB database using Gridfs driver

Options:
```
var storageConfig = {
  gridFs: {
    mongoUrl: "mongodb://localhost:27017/files"
  }
};
require('wf-storage')(mediator, storageConfig);
```

### Topic Subscriptions

Topics are used in file module.

##### Description

Saves file to the storage

##### Example


```javascript
var parameters = {
   // File namespace (folder)
   namespace:null,
   fileName:"test",
   location: "/tmp/file"
  //Optional topic unique identifier
  topicUid: "uniquetopicid"
}

mediator.publish("mm:files-store:create", parameters);
```
##### Description

Retrieve file from the storage (BinaryStream)

##### Example

```javascript
var parameters = {
  namespace:null,
  fileName:"test",
  topicUid: "uniquetopicid"
}

mediator.publish("mm:files-store:get", parameters);
```
