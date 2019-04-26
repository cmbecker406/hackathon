from dataclasses import dataclass

@dataclass
class User:
    name: str
    password: str
    phone: int
    skill_auto: bool
    skill_tech: bool
    skill_home: bool
    skill_misc: bool
    
    
@dataclass
class Request:
    init_date: datetime.datetime = datetime.datetime.today()
    title: str
    description: str
    skill_auto: bool
    skill_tech: bool
    skill_home: bool
    skill_misc: bool
    active_flag: bool
    due_date: datetime.datetime
