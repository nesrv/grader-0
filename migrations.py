import os
import sys
from alembic.config import Config
from alembic import command

def init_migrations():
    alembic_cfg = Config("alembic.ini")
    command.init(alembic_cfg, "alembic")
    print("Alembic initialized")

def create_migration(message):
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, message=message, autogenerate=True)
    print(f"Migration created: {message}")

def upgrade_db():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("Database upgraded to latest version")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python migrations.py [init|create|upgrade] [message]")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == "init":
        init_migrations()
    elif action == "create":
        if len(sys.argv) < 3:
            print("Migration message required")
            sys.exit(1)
        create_migration(sys.argv[2])
    elif action == "upgrade":
        upgrade_db()
    else:
        print("Unknown action. Use init, create or upgrade")
        sys.exit(1)