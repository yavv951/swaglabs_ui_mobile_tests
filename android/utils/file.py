def abs_path_from_project(relative_path: str):
    from android import utils
    from pathlib import Path

    return (
        Path(utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )