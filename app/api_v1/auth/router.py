from fastapi import APIRouter, Depends
from typing import List

from app.api_v1.auth.models import Token, User, UserCreate, UserUpdate
from app.api_v1.auth.handlers import (
    login_for_access_token, read_users_me, read_users, create_user, update_user_me,
    read_user_by_id, get_current_active_user
)

router = APIRouter()

# Маршруты для аутентификации
router.add_api_route("/token", login_for_access_token, methods=["POST"], response_model=Token)
router.add_api_route("/me", read_users_me, methods=["GET"], response_model=User)
router.add_api_route("/me", update_user_me, methods=["PUT"], response_model=User)
router.add_api_route("", read_users, methods=["GET"], response_model=List[User], dependencies=[Depends(get_current_active_user)])
router.add_api_route("", create_user, methods=["POST"], response_model=User)
router.add_api_route("/{user_id}", read_user_by_id, methods=["GET"], response_model=User, dependencies=[Depends(get_current_active_user)])