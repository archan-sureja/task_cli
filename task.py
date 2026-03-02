import uuid 
from datetime import datetime 
class Task:
    def __init__(self,description):
        self.id = str(uuid.uuid4())[:5] 
        self.description = description
        self.status = 'todo'
        self.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = None
        