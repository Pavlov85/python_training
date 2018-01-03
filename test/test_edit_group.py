from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="wwww", header="qqqq", footer="rrrr"))
    app.group.edit(Group(name="xxxx", header="yyyyy", footer="zzzz"))