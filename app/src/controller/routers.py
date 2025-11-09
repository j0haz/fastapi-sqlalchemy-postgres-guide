from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from model import crud, schemas, db_manager

dbSession = Depends(db_manager.get_db)


# use APIRouters to assign URL-routes to request handler functions


userCrudRouter = APIRouter()

@userCrudRouter.post("/user_create", response_model = schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = dbSession):
    """ 
        endpoint for creating specified user in database 
    """
    json_response = crud.create_user(db=db, user=user)

    return json_response


@userCrudRouter.get("/user_read", response_model = list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 10, db: Session = dbSession):
    """
        endpoint for reading users from the database
    """
    json_response = crud.read_users(db, skip=skip, limit=limit)

    return json_response

@userCrudRouter.post("/user_update")
def update_user(user: schemas.UserUpdate, db: Session = dbSession) -> dict[str, str]:
    """ 
        endpoint for updating specified user from database
    """

    ret = crud.update_user(db=db, user=user)
    if not ret:
        raise HTTPException(status_code=404, detail="User not found")

    json_response = {"message": "User updated sucessfully!"}

    return json_response

@userCrudRouter.post("/user_delete")
def delete_user(user: schemas.UserDelete, db: Session = dbSession) -> dict[str, str]:
    """ 
        endpoint for deleting specified user from database
    """

    ret = crud.delete_user(db=db, user=user)
    if not ret:
        raise HTTPException(status_code=404, detail="User not found")

    json_response = {"message": "User deleted sucessfully!"}

    return json_response



templateRouter = APIRouter()

templates = Jinja2Templates(directory="view/templates")

@templateRouter.get("/reflect")
async def reflect_request(request: Request):
    """  reflects user request in HTML response body

    Args:
        request (fastapi.Request): http request object

    Returns:
        fastapi.templating.Jinja2Templates.TemplateResponse: rendered HTML 
    """

    headers = dict(request.headers.__dict__["_list"])

    params = request.query_params.__dict__["_dict"]
    body = await request.body()


    return templates.TemplateResponse(
        request=request, name="reflect.html", context={"method": request.method, "url": request.url, "headers": headers, "params": params, "body": body}
    )
