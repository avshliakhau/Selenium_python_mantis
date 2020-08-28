import random
from model.project import Project


def test_delete_project(app):
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    app.project.manage_project_page()
    old_project_list = app.soap.get_projects_list(username, password)
    if len(old_project_list) == 0:
        app.project.create_project(Project(name='first_project_for_del'))
    old_project_list = app.soap.get_projects_list(username, password)
    # print("old_project_list = ", old_project_list)
    project_for_deletion = random.choice(old_project_list)
    # print("project_for_deletion = ", project_for_deletion)
    s = str(project_for_deletion)
    # print("s = ", s)
    name_project = s.split(": ")[-1]
    # print("name_project = ", name_project)
    app.project.del_some_project(name_project)###
    # app.project.del_project()### работает, но проверка не проходит (№ в списке)
    new_project_list = app.soap.get_projects_list(username, password)###
    # print("new_project_list = ", new_project_list)
    old_project_list.remove(project_for_deletion)###
    # print("old_project_list_after_remove = ", old_project_list)###
    assert sorted(old_project_list, key=app.project.id_or_max) == sorted(
        new_project_list, key=app.project.id_or_max)