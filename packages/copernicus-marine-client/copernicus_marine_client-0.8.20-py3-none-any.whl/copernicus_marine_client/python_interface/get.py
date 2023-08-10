import pathlib
from typing import List, Optional, Union

from copernicus_marine_client.core_functions.get import get_function


def get(
    dataset_url: Optional[str] = None,
    dataset_id: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    no_directories: bool = False,
    show_outputnames: bool = False,
    output_directory: Optional[Union[pathlib.Path, str]] = None,
    credentials_file: Optional[Union[pathlib.Path, str]] = None,
    overwrite_output_data: bool = False,
    request_file: Optional[Union[pathlib.Path, str]] = None,
    force_service: Optional[str] = None,
    overwrite_metadata_cache: bool = False,
    no_metadata_cache: bool = False,
    filter: Optional[str] = None,
    regex: Optional[str] = None,
) -> List[pathlib.Path]:
    output_directory = (
        pathlib.Path(output_directory) if output_directory else None
    )
    credentials_file = (
        pathlib.Path(credentials_file) if credentials_file else None
    )
    request_file = pathlib.Path(request_file) if request_file else None
    return get_function(
        dataset_url,
        dataset_id,
        username,
        password,
        no_directories,
        show_outputnames,
        output_directory,
        credentials_file,
        True,
        overwrite_output_data,
        request_file,
        force_service,
        overwrite_metadata_cache,
        no_metadata_cache,
        filter,
        regex,
    )
