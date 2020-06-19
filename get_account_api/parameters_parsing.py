import yaml


def parse_onedrive_params(onedrive_param_file_path):
    with open(onedrive_param_file_path, 'r') as stream:
        onedrive_login = yaml.safe_load(stream)
    return onedrive_login


def parse_bankin_params(bankin_param_file_path):
    with open(bankin_param_file_path, 'r') as stream:
        bankin_param = yaml.safe_load(stream)
    return bankin_param
