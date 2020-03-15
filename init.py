def initialize_project():
    from utils.create_proto import create_proto_files
    from utils.import_fixer import convert_to_relative_imports
    
    create_proto_files()
    convert_to_relative_imports()


if __name__ == "__main__":
    initialize_project()
