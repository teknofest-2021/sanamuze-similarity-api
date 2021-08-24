# Get Image List

Get image list(name, prefix, base64Format) from server

**URL** : `/api/similarity/getImageList`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

- No required

## Success Response

**Condition** : If everything is OK and Server is UP.

**Code** : `200 SUCCESSFUL`

**Content example**

```json
[
    {
        "imageName"     : "herkul",
        "imagePrefix"   : "jpg",
        "imageBase64"   : "/9j/4AAQSkZJRgABAQAAAQABAAD/...."
    }
]
```
## Error Responses

**Condition** : If Server does not contain any image.

**Code** : `404 FAILED`

**Headers** : `Location: http://194.31.79.154/api/similarity/getImageList`

**Content** : `{}`