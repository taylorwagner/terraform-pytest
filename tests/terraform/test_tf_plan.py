import pytest
import configparser


from tests.data_util.data_resolver import inject_test_data

config = configparser.ConfigParser()
config.read('tests/resources/datatable.ini')

for sect in config.sections():
    resource_names = list(config['RESOURCES'].values())
    print(resource_names)


class TestPlan:
    test_plan = inject_test_data(file="tf_plan/plan.json")

    @pytest.mark.parametrize("plan", test_plan)
    def test_resource_names(self, plan):
        resources = plan['planned_values']['root_module']['resources']
        names_from_json = [resource['name'] for resource in resources]

        # bi directional delta of lists
        diff1 = [name for name in resource_names if name not in names_from_json]
        diff2 = [name for name in names_from_json if name not in resource_names]
        print(diff1 + diff2)

        assert not diff1 and not diff2


                