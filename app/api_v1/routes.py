from fastapi import APIRouter, Depends
from typing import List, Dict

from app.api_v1.auth.models import Token, User, UserCreate, UserUpdate
from app.api_v1.auth.handlers import (
    login_for_access_token, read_users_me, read_users, create_user, update_user_me,
    read_user_by_id
)

from app.api_v1.profession.schemas import Profession, ProfessionCreate, ProfessionUpdate
from app.api_v1.profession.handlers import (
    read_professions, read_profession, create_new_profession,
    update_existing_profession, delete_existing_profession
)

router = APIRouter(prefix="/api/v1")

# Маршруты для аутентификации
router.add_api_route("/users/token", login_for_access_token, methods=["POST"], response_model=Token)
router.add_api_route("/users/me", read_users_me, methods=["GET"], response_model=User)
router.add_api_route("/users/me", update_user_me, methods=["PUT"], response_model=User)
router.add_api_route("/users", read_users, methods=["GET"], response_model=List[User])
router.add_api_route("/users", create_user, methods=["POST"], response_model=User)
router.add_api_route("/users/{user_id}", read_user_by_id, methods=["GET"], response_model=User)

# Маршруты для профессий
router.add_api_route("/professions", read_professions, methods=["GET"], response_model=List[Profession])
router.add_api_route("/professions", create_new_profession, methods=["POST"], response_model=Profession)
router.add_api_route("/professions/{profession_id}", read_profession, methods=["GET"], response_model=Profession)
router.add_api_route("/professions/{profession_id}", update_existing_profession, methods=["PUT"], response_model=Profession)
router.add_api_route("/professions/{profession_id}", delete_existing_profession, methods=["DELETE"], response_model=Dict[str, bool])