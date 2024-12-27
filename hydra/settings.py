def return_project_config(project):
    config = {
        "ansible": {
            "paths": [
                "ansible/inventories/production/group_vars/group1.yml",
                "ansible/inventories/production/host_vars/",
                "ansible/inventories/production/hosts",
                "ansible/inventories/stage/group_vars/group1.yml",
                "ansible/inventories/stage/host_vars",
                "ansible/inventories/stage/hosts",
                "ansible/library",
                "ansible/module_utils",
                "ansible/filter_plugins",
                "ansible/roles/common",
                "ansible/oles/tasks",
                "ansible/oles/templates",
            ]
        }
    }

    return config[project]
