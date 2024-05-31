import os


def is_codebuild() -> bool:
    """
    detects whether we are running in codebuild
    """
    x = os.environ.get('CODEBUILD_BUILD_ID')
    return bool(x)
