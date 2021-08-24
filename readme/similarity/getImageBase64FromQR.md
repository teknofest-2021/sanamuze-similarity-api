# Get Image Base64 Format

Get Image Base64 Format from QR Code (QR returns image name)

**URL** : `/api/similarity/getImageBase64FromQR`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide name of Image to get Base64 Format.

```json
{
    "imageName" : "[unicode 64 chars max] (with prefix)"
}
```

**Data example** All fields must be sent.

```json
{
    "imageName" : "testImage.jpg"
}
```

## Success Response

**Condition** : If everything is OK and Server is UP.

**Code** : `200 SUCCESSFUL`

**Content example**

```json
{
    "imageBase64"   : "/9j/4AAQSkZJRgABAQAAAQABAAD/...."
}
```

## Error Responses

**Condition** : If image name doesnt exist or wrong.

**Code** : `404 FAILED`

**Headers** : `Location: http://194.31.79.154/api/similarity/getImageBase64FromQR`

**Content** : `{ "imageName" : "randomName.jpg"}`