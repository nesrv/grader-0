from fastapi import APIRouter, Depends
from typing import List

from app.api_v1.auth.models import Token, User, UserCreate, UserUpdate
from app.api_v1.auth.handlers import (
    login_for_access_token, read_users_me, read_users, create_user, update_user_me
)

router = APIRouter(prefix="/api/v1")

# Маршруты для аутентификации
router.add_api_route("/users/token", login_for_access_token, methods=["POST"], response_model=Token)
router.add_api_route("/users/me", read_users_me, methods=["GET"], response_model=User)
router.add_api_route("/users/me", update_user_me, methods=["PUT"], response_model=User)
router.add_api_route("/users", read_users, methods=["GET"], response_model=List[User])
router.add_api_route("/users", create_user, methods=["POST"], response_model=User)