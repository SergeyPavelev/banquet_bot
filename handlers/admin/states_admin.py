from aiogram.fsm.state import State, StatesGroup


class AddUser(StatesGroup):
    name_new_user = State()
    

class DeleteUser(StatesGroup):
    user_id = State()
    

class EditUser(StatesGroup):
    user_id = State()
    new_name_user = State()
    

class AddTask(StatesGroup):
    name_task = State()


class DeleteTask(StatesGroup):
    task_id = State()
    

class EditTask(StatesGroup):
    task_id = State()
    new_name_task = State()
