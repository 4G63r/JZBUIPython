from keywords.get_data import GetData
from keywords.action_method import ActionMethod


class RunMain:
    def run_method(self):
        data = GetData()
        # action_method = ActionMethod()
        lines = data.get_case_lines()
        for i in range(1, lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_handle_value(i)
            expect_element = data.get_expect_element(i)


if __name__ == '__main__':
    r = RunMain()
    r.run_method()
