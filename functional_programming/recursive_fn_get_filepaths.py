def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for key in parent_directory:
        path_so_far = current_filepath + "/" + key

        if parent_directory[key] is None:
            file_paths.append(path_so_far)
        else:
            file_paths.extend(list_files(parent_directory[key], path_so_far))

    return file_paths
