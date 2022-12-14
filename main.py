from fastapi import FastAPI, Request, Response, status

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I'm a walnut"}

@app.post("/image")
async def post_image(request: Request, response: Response):
    image: bytes = await request.body()

    with open('stored_image.jpg', 'wb+') as f:
        f.write(image)

    response.headers['Content-Location'] = '/image.jpg'
    response.status_code = status.HTTP_201_CREATED

    return ""

@app.get("/image.jpg")
async def get_image():
    with open('stored_image.jpg', 'rb') as f:
        image = f.read()

    return Response(content=image, media_type='image/jpeg', status_code=status.HTTP_200_OK)