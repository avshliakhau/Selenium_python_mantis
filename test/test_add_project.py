# from model.project import Project


def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.manage_project_page()
    if len(app.project.get_projects_list()) == 0:
        project_first_name = 'first_test_1'
        app.project.create_project(project_first_name)
    old_project_list = app.project.get_projects_list()
    # print("old_project_list = ", old_project_list)
    project_name = 'test_17'
    app.project.create_project(project_name)
    new_project_list = app.project.get_projects_list()
    # print("new_project_list = ", new_project_list)
    old_project_list.append(project_name)
    # print("append_old_project_list = ", old_project_list)
    assert sorted(old_project_list) == sorted(new_project_list)