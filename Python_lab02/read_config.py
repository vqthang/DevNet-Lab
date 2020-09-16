import yaml


def read_config(file_config):
    with open(file_config, 'r') as file:
        output = yaml.load(file)
        return output


conf = read_config('router_config.ini')
print(conf)
