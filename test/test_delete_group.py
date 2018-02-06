from model.group import Group
import random

# удаление группы по id
def test_delete_group_by_id(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="xxx", header="yyy", footer="zzz"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups

# удаление группы по индексу
#def test_delete_some_group(app):
 #   if app.group.count() == 0:
 #      app.group.create(Group(name="xxx", header="yyy", footer="zzz"))
 #   old_groups = app.group.get_group_list()
 #   index = randrange(len(old_groups))
 #  app.group.delete_group_by_index(index)
 #   new_groups = app.group.get_group_list()
 #  assert len(old_groups) - 1 == len(new_groups)
 #  old_groups[index:index+1] = []
 #  assert old_groups == new_groups