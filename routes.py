from fastapi import APIRouter

router=APIRouter()

@router.get("/users/get")
def get_data():
    return "Get Data"
@router.put("/users/put")
def post_data():
    return "Put Data"
@router.patch("/users/patch")
def patch_data():
    return "Patch Data"
@router.delete("/users/delete")
def delete_data():
    return "Delete Data"