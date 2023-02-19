from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, \
    TextField, ManyToManyField, BooleanField, SmallIntegerField

from tools.notifications.periodes import InactivePeriodStatus
from .settings import database, DT_FORMAT


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    tg_id = IntegerField(unique=True, index=True)
    registration_dt = DateTimeField(formats=[DT_FORMAT])
    username = CharField(max_length=64)
    full_name = CharField(max_length=64)
    last_activity_dt = DateTimeField(formats=[DT_FORMAT], null=True)
    inactive_notification_period = SmallIntegerField(default=InactivePeriodStatus.LESS_DAY)
    
    def __str__(self):
        return f"Пользователь с TG ID {self.tg_id}. " \
               f"Username {self.username}, " \
               f"Полное имя {self.full_name}"


class StageGroup(BaseModel):
    title = CharField(unique=True, max_length=256)
    picture = CharField(max_length=256)
    
    class Meta:
        table_name = "stage_group"


class Stage(BaseModel):
    title = CharField(unique=True, max_length=256)
    icon = CharField(max_length=256)
    picture = CharField(max_length=256)
    quote = CharField(max_length=256, null=True)
    content = TextField()
    tested_users = ManyToManyField(User, backref="completed_stages")
    is_active = BooleanField(default=True)
    
    def __str__(self):
        return f"Стадия «{self.title}» c содержанием {self.content[:48]}"


StagePasser = Stage.tested_users.get_through_model()


class CheckPointOfStage(BaseModel):
    stage = ForeignKeyField(Stage)
    point = CharField(max_length=256)
    tested_users = ManyToManyField(User, backref="completed_points")
    
    class Meta:
        table_name = "checkpoint_of_stage"


CheckPointPasser = CheckPointOfStage.tested_users.get_through_model()


class FeedbackByStage(BaseModel):
    user = ForeignKeyField(User, unique=True)
    lesson = ForeignKeyField(Stage)
    text = TextField()
    
    class Meta:
        table_name = "feedback_by_stage"


class BlogpostCategory(BaseModel):
    name = CharField(max_length=64)
    
    class Meta:
        table_name = "blogpost_category"


class Blogpost(BaseModel):
    category = ForeignKeyField(BlogpostCategory, backref="category")
    title = CharField(max_length=256)
    logo = CharField(max_length=256)
    link = CharField(max_length=256)


class WorkDirectorate(BaseModel):
    ru_title = CharField(max_length=512)
    director_name = CharField(max_length=128)
    
    class Meta:
        table_name = "work_directorate"


class WorkDepartment(BaseModel):
    ru_title = CharField(max_length=512)
    directorate = ForeignKeyField(WorkDirectorate)
    
    class Meta:
        table_name = "work_department"


tables = [User, StageGroup, Stage, StagePasser, CheckPointOfStage, CheckPointPasser,
          FeedbackByStage, BlogpostCategory, Blogpost, WorkDirectorate, WorkDepartment]

database.create_tables(tables)
