import pathlib
from datetime import datetime
from typing import List, Optional, Union

from copernicus_marine_client.core_functions.subset import subset_function


def subset(
    dataset_url: Optional[str] = None,
    dataset_id: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    variables: Optional[List[str]] = None,
    minimal_longitude: Optional[float] = None,
    maximal_longitude: Optional[float] = None,
    minimal_latitude: Optional[float] = None,
    maximal_latitude: Optional[float] = None,
    minimal_depth: Optional[float] = None,
    maximal_depth: Optional[float] = None,
    vertical_dimension_as_originally_produced: bool = True,
    start_datetime: Optional[datetime] = None,
    end_datetime: Optional[datetime] = None,
    output_filename: Optional[Union[pathlib.Path, str]] = None,
    force_service: Optional[str] = None,
    request_file: Optional[Union[pathlib.Path, str]] = None,
    output_directory: Optional[Union[pathlib.Path, str]] = None,
    credentials_file: Optional[Union[pathlib.Path, str]] = None,
    motu_api_request: Optional[str] = None,
    overwrite_output_data: bool = False,
    overwrite_metadata_cache: bool = False,
    no_metadata_cache: bool = False,
) -> pathlib.Path:
    output_filename = (
        pathlib.Path(output_filename) if output_filename else None
    )
    request_file = pathlib.Path(request_file) if request_file else None
    output_directory = (
        pathlib.Path(output_directory) if output_directory else None
    )
    credentials_file = (
        pathlib.Path(credentials_file) if credentials_file else None
    )
    return subset_function(
        dataset_url,
        dataset_id,
        username,
        password,
        variables,
        minimal_longitude,
        maximal_longitude,
        minimal_latitude,
        maximal_latitude,
        minimal_depth,
        maximal_depth,
        vertical_dimension_as_originally_produced,
        start_datetime,
        end_datetime,
        output_filename,
        force_service,
        request_file,
        output_directory,
        credentials_file,
        motu_api_request,
        True,
        overwrite_output_data,
        overwrite_metadata_cache,
        no_metadata_cache,
    )
