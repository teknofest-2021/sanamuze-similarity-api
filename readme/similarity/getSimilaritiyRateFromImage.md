# Get Image Base64 Format

Get Image Similarity Rate between two images. One of them exist in server and another one come from with API (as a base64).

**URL** : `/api/similarity/getSimilaritiyRateFromImage`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide name of Image to get Base64 Format.

```json
{
    "compareImageName"  : "[unicode 64 chars max] (with prefix)",
    "imageBase64"       : "[unicode chars max] (image base64 format)"
}
```

**Data example** All fields must be sent.

```json
{
    "compareImageName" : "testImage.jpg",
    "imageBase64"      : "/9j/4AAQSkZJRgABAQAAAQABAAD/...."
}
```

## Success Response

**Condition** : If everything is OK and Server is UP.

**Code** : `200 SUCCESSFUL`

**Content example**

```json
{
    "similarityRate"   : "95.50"
}
```

## Error Responses

**Condition** : If image name doesnt exist or wrong and base64 format is not valid.

**Code** : `404 FAILED`

**Headers** : `Location: http://194.31.79.154/api/similarity/getImageBase64FromQR`

**Content** : `{"compareImageName" : "randomName.jpg","imageBase64" : "123?3/9j/4AAQSkZJRgABAQAAAQABAAD/...."}`