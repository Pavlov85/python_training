from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="wwww", header="qqqq", footer="rrrr"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="xxxx", header="yyyyy", footer="zzzz")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)