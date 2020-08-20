import random


def test_delete_project(app):
    app.session.login('administrator', 'root')
    app.project.manage_project_page()
    old_project_list = app.project.get_projects_list()
    if len(old_project_list) == 0:
        app.project.create_project('first_project_for_del')
    old_project_list = app.project.get_projects_list()
    # print("old_project_list = ", old_project_list)
    name = random.choice(old_project_list)
    # print("project_for_deletion = ", name)
    app.project.del_some_project(name)
    new_project_list = app.project.get_projects_list()
    # print("new_project_list = ", new_project_list)
    old_project_list.remove(name)
    # print("old_project_list_remove = ", new_project_list)
    assert sorted(old_project_list) == sorted(new_project_list)