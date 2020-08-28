from model.project import Project


def test_add_project(app):
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    app.project.manage_project_page()
    old_project_list = app.project.get_projects_list()
    # print("old_project_list_app = ", old_project_list)
    if len(old_project_list) == 0:
        project_first_name = 'first_test_1'
        app.project.create_project(project_first_name)
    old_project_list = app.soap.get_projects_list(username, password) # ??add?? username, password
    # print("old_project_list_soap = ", old_project_list)
    project_name = 'test_51'
    app.project.create_project(project_name)
    new_project_list = app.soap.get_projects_list(username, password)# ??add?? username, password
    # print("new_project_list_soap = ", new_project_list)
    append_project = sorted(new_project_list, key=app.project.id_or_max)[-1]
    # print("append_project = ", append_project)
    old_project_list.append(append_project)
    # print("old_project_list_after_append=", old_project_list)
    assert sorted(old_project_list, key=app.project.id_or_max) == sorted(new_project_list, key=app.project.id_or_max)
