## Workflows


1. Contants -> file_paths, local_dir_path
2. Config.yaml -> define component specific members sources (Source_URL, artifacts_dir, local_file_name)
3. Entity_config -> define component spefic dataclasses 
4. ConfigurationManger -> declare a method to assign component specific members to members from config.yaml
5. Component -> define different operations for each component
6. Pipeline -> define steps by calling methods from component in order

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml