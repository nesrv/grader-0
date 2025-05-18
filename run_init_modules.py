from sqlalchemy.orm import Session
from app.database import SessionLocal, Grade
from app.init_modules_data import init_modules_data

if __name__ == "__main__":
    # Create a database session
    db = SessionLocal()
    
    try:
        # Check if the intern grade exists
        intern_grade = db.query(Grade).filter(
            Grade.level_name == "STAGER",  # Using the actual value stored in the database
            Grade.profession_id == 1  # Backend developer
        ).first()
        
        if not intern_grade:
            print("Intern grade not found. Please run init_db.py first to initialize the database.")
        else:
            # Initialize modules data
            init_modules_data(db)
    finally:
        # Close the session
        db.close()
    
    print("Script execution completed.")