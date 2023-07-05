

def abs_path_from_project(relative_path: str):
    import mobile_tests_5_23
    from pathlib import Path

    return (
        Path(mobile_tests_5_23.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )