import sys
import os
import json

# Add backend directory to path so we can import models
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from models import User, Job, Gig, Mentor, Skill
from core.security import get_password_hash


def seed_data():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # 1. Seed Users
    if not db.query(User).first():
        print("Seeding Users...")
        admin = User(
            email="admin@stepup.com",
            hashed_password=get_password_hash("admin123"),
            role="admin"
        )
        youth = User(
            email="youth@stepup.com",
            hashed_password=get_password_hash("youth123"),
            role="youth"
        )
        db.add(admin)
        db.add(youth)
        db.commit()

    # 2. Seed Jobs
    if not db.query(Job).first():
        print("Seeding Jobs...")
        with open('data/jobs.json', 'r') as f:
            jobs_data = json.load(f)
            for j in jobs_data:
                job = Job(
                    title=j['title'],
                    company=j['company'],
                    location=j['location'],
                    type=j['type'],
                    description=j['description'],
                    salary=j['salary'] if 'salary' in j else "Competitive"
                )
                db.add(job)
        db.commit()

    # 3. Seed Gigs
    if not db.query(Gig).first():
        print("Seeding Gigs...")
        with open('data/gigs.json', 'r') as f:
            gigs_data = json.load(f)
            for g in gigs_data:
                gig = Gig(
                    title=g['title'],
                    description=g['description'],
                    budget=float(g['budget']),
                    currency=g['currency'],
                    is_premium=g.get('is_premium', False)
                )
                db.add(gig)
        db.commit()

    # 4. Seed Mentors
    if not db.query(Mentor).first():
        print("Seeding Mentors...")
        with open('data/mentorship.json', 'r') as f:
            mentors_data = json.load(f)
            for m in mentors_data:
                mentor = Mentor(
                    name=m['name'],
                    role=m['role'],
                    company=m['company'],
                    expertise=m['expertise'],
                    availability=m['availability'],
                    image_url=m.get('image', '')
                )
                db.add(mentor)
        db.commit()

    # 5. Seed Skills
    if not db.query(Skill).first():
        print("Seeding Skills...")
        try:
            with open('data/skills.json', 'r') as f:
                skills_data = json.load(f)
                for s in skills_data:
                    # Check if skill exists to avoid unique constraint error if run partially
                    if not db.query(Skill).filter(Skill.name == s['name']).first():
                        skill = Skill(
                            name=s['name'],
                            category=s['category'],
                            level=s['level'],
                            resources=s.get('resources', [])
                        )
                        db.add(skill)
                db.commit()
        except FileNotFoundError:
            print("Warning: data/skills.json not found. Skipping skills seed.")

    print("Database seeded successfully!")
    db.close()


if __name__ == "__main__":
    seed_data()
