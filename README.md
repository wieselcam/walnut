<p align="center"><img src="https://raw.githubusercontent.com/wieselcam/walnut/development/the_walnut.png" width="500px"/></p>
<hr>
<p align="center">
  Walnut is the new backend server of Wieselcam.
  It provides basic endpoints to store and provide webcam images.
</p>
<hr>

## Roadmap

- [X] Setup basic FastApi
- [X] Add Github actions for automatic testing
- [X] Add endpoints to store/provide current webcam image
- [X] Add a walnut image to this readme
- [ ] Add basic database and push image to database
- [ ] Refactor structure/files/tests to be more separate


## How to start
- Start Server with `uvicorn main:app --reload`
- Run `pytest` - all tests should pass
- Open http://127.0.0.1:8000/docs


## FAQ
### Why walnut?
I don't know, I simply like walnuts lately.
