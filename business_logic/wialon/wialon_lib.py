from python_wialon.api import WialonError


# def create_unit(wialon_api):
#     try:
#         creator_id = login(wialon_api, token)
#         params = {'creatorId': creator_id, 'name': 'ips_unitttss',
#                   'hwTypeId': 96266, 'dataFlags': 1}

#         create_user_params = {"id": 352093083080803,
#                               "flags": 4}
#         action_name = 'core/create_unit'
#         create_user_action_name = 'core/search_item'
#         print(wialon_api.avl_evts())

#         wialon_api.call(create_user_action_name, **create_user_params)
#         print("sucessfully")

#     except WialonError as e:
#         print(e)


def view_units(wialon_api):
    try:
        view_units_params = {
            "spec": [{"type": "type", "data": "avl_unit", "flags": 1, "mode": 0}]}

        svc = "core/update_data_flags"

        result = wialon_api.call(svc, **view_units_params)

        return (result)

    except WialonError as e:
        print(e)


def view_users(wialon_api):
    try:
        view_users_params = {
            "spec": [{"type": "type", "data": "user", "flags": 1, "mode": 0}]}

        svc = "core/update_data_flags"

        result = wialon_api.call(svc, **view_users_params)

        return (result)

    except WialonError as e:
        print(e)


def get_resource(wialon_api, id):
    try:
        view_resource_params = {
            "spec": [{"type": "id", "data": id, "flags": 1, "mode": 0}]}

        svc = "core/update_data_flags"

        result = wialon_api.call(svc, **view_resource_params)

        return (result)

    except WialonError as e:
        print(e)


def get_resources(wialon_api):
    try:
        view_resource_params = {
            "spec": [{"type": "type", "data": "avl_resource", "flags": 16641, "mode": 0}]}

        svc = "core/update_data_flags"

        result = wialon_api.call(svc, **view_resource_params)

        return (result)

    except WialonError as e:
        print(e)

def get_resources(wialon_api):
    try:
        view_resource_params = {
            "spec": [{"type": "type", "data": "avl_resource", "flags": 16641, "mode": 0}]}

        svc = "core/update_data_flags"

        result = wialon_api.call(svc, **view_resource_params)

        return (result)

    except WialonError as e:
        print(e)
