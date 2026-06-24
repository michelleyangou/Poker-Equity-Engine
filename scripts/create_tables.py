import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from backend.app.database import engine
from backend.app.models.models import Base

print("Creating tables...")
Base.metadata.create_all(engine)
print("Done! All tables created.")