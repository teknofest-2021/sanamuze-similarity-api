# SanAmuze Similarity Rate RESTAPIDocs

This repostory is about [SanAmuze Similarity Rate](https://github.com/teknofest-2021/similarity-rate-api) and so the api will return
JSON responses.

Where full URLs are provided in responses they will be rendered as if service
is running on 'http://194.31.79.154:6065/'.

## Open Endpoints

Open endpoints require no Authentication.

### Similarity Rate Related

Each endpoint manipulates or displays information related to the image which provided:

* [getImageList](readme/similarity/getImageList.md) : `GET /api/similarity/getImageList`
* [getImageBase64FromQR](readme/similarity/getImageBase64FromQR.md) : `POST /api/similarity/getImageBase64FromQR`
* [getSimilaritiyRateFromImage](readme/similarity/getSimilaritiyRateFromImage.md) : `POST /api/similarity/getSimilaritiyRateFromImage`

### API Test Related

* [getTest](readme/test/getImageList.md) : `GET /api/test/getTest`
* [getTestJenkins](readme/test/getImageBase64FromQR.md) : `GET /api/test/getTestJenkins`


