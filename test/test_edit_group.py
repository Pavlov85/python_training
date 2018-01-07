from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="wwww", header="qqqq", footer="rrrr"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="xxxx", header="yyyyy", footer="zzzz"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)