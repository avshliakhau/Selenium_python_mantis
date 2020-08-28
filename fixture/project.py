import time
from sys import maxsize


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project_name):
        # create add project
        wd = self.app.wd
        self.manage_project_page()
        wd.find_element_by_xpath('//input[@value="Create New Project"]').click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        # time.sleep(1)
        wd.find_element_by_xpath('//select[@name="status"]').click()
        # time.sleep(1)
        wd.find_element_by_css_selector("select[name='status']>option[value='10']").click()
        wd.find_element_by_xpath('//input[@type="checkbox"]').click()
        # time.sleep(1)
        wd.find_element_by_xpath('//input[@type="checkbox"]').click()
        # time.sleep(1)
        wd.find_element_by_name("description").send_keys("description project -'%s'" % project_name)
        # time.sleep(1)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        # time.sleep(1)
        # self.project_cache = None
        # self.open_home_page()
        # self.project_cache = None

    def manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_css_selector(
            'body div:nth-child(4) p span:nth-child(2) a').click()

    def del_project(self):
        wd = self.app.wd
        self.manage_project_page()
        # time.sleep(1)
        wd.find_element_by_xpath("//table[3]/tbody/tr[3]/td[1]/a").click()
        # time.sleep(1)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        # time.sleep(1)
        wd.find_element_by_css_selector(
            'input[value="Delete Project"]').click()
        # time.sleep(1)

    def del_some_project(self, name):
        wd = self.app.wd
        self.manage_project_page()
        wd.find_element_by_link_text(name).click()
        # wd.find_element_by_xpath("//table[3]/tbody/tr[%d]/td[1]/a" % d).click()
        # time.sleep(1)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        # time.sleep(1)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        # time.sleep(1)

    def get_projects_list(self):
        wd = self.app.wd
        result_list = []
        if 'manage_proj_page.php' not in wd.current_url:
            self.manage_project_page()
        rows = wd.find_elements_by_tag_name("tr.row-1 td a") + wd.find_elements_by_tag_name("tr.row-2 td a")
        # print("len = ", len(rows))
        s = 3
        if len(rows) == 0:
            return result_list
        else:
            for row in rows:
                result_list.append(row.find_element_by_xpath(
                    "//table[3]/tbody/tr[%s]/td[1]" % s).text)
                s += 1
        return result_list

    def id_or_max(self, project):
        # self.select_project_by_id()
        if project.id:
            return int(project.id)
        else:
            return maxsize