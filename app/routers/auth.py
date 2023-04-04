from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth'], responses={
                   404: {'description': 'Not found'}})


@router.post('/register')
async def register():
  return {'message': 'Register a new user'}


@router.post('/login')
async def login():
  return {'message': 'Login a user'}
