"""
Dropbox Connector
The Dropbox Connector presents a couple abnormal situations.
1) They don't have an unexpiring token
2) They require a forward slash `/` in front of the remote_file_path. This presents
some real problems creating paths. When appending a path that begins with a
forward slash to any path, whether using the / shorthand or joinpath, causes the
starting path to disappear. So the `/` needs to be stripped off.
3) To list and get files from the root directory Dropbox you need a ""," ", or " /"
"""
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Type

from unstructured.ingest.connector.fsspec import (
    FsspecConnector,
    FsspecIngestDoc,
    SimpleFsspecConfig,
)
from unstructured.ingest.interfaces import StandardConnectorConfig
from unstructured.utils import requires_dependencies


class MissingFolderError(Exception):
    """There is no folder by that name. For root try `dropbox:// /`"""


@dataclass
class SimpleDropboxConfig(SimpleFsspecConfig):
    pass


class DropboxIngestDoc(FsspecIngestDoc):
    @requires_dependencies(["dropboxdrivefs", "fsspec"])
    def get_file(self):
        super().get_file()

    @property
    def _output_filename(self):
        # Dropbox requires a forward slash at the front of the folder path. This
        # creates some complications in path joining so a custom path is created here.
        # Dropbox uses an empty string `""`, or a space `" "`` or a `" /"` to list root
        if self.config.dir_path == " ":
            return Path(self.standard_config.output_dir) / re.sub(
                "^/",
                "",
                f"{self.remote_file_path}.json",
            )
        else:
            return (
                Path(self.standard_config.output_dir)
                / f"{self.remote_file_path.replace(f'/{self.config.dir_path}/', '')}.json"
            )

    def _tmp_download_file(self):
        # Dropbox requires a forward slash at the front of the folder path. This
        # creates some complications in path joining so a custom path is created here.
        # Dropbox uses an empty string `""`, or a space `" "`` or a `" /"` to list root
        if self.config.dir_path == " ":
            return Path(self.standard_config.download_dir) / re.sub(
                "^/",
                "",
                self.remote_file_path,
            )
        else:
            return Path(self.standard_config.download_dir) / self.remote_file_path.replace(
                f"/{self.config.dir_path}/",
                "",
            )


@requires_dependencies(["dropboxdrivefs", "fsspec"])
class DropboxConnector(FsspecConnector):
    ingest_doc_cls: Type[DropboxIngestDoc] = DropboxIngestDoc

    def __init__(
        self,
        config: SimpleDropboxConfig,
        standard_config: StandardConnectorConfig,
    ) -> None:
        super().__init__(standard_config, config)

    def initialize(self):
        # Dropbox requires a forward slash at the front of the folder path. This
        # creates some complications in path joining so a custom path is created here.
        ls_output = self.fs.ls(f"/{self.config.path_without_protocol}")
        if ls_output and len(ls_output) >= 1:
            return
        elif ls_output:
            raise ValueError(
                f"No objects found in {self.config.path}.",
            )
        else:
            raise MissingFolderError(
                "There is no folder by that name. For root try `dropbox:// /`",
            )

    def _list_files(self):
        # Dropbox requires a forward slash at the front of the folder path. This
        # creates some complications in path joining so a custom path is created here.
        if not self.config.recursive:
            # fs.ls does not walk directories
            # directories that are listed in cloud storage can cause problems because they are seen
            # as 0byte files
            return [
                x.get("name")
                for x in self.fs.ls(
                    f"/{self.config.path_without_protocol}",
                    detail=True,
                )
                if x.get("size")
            ]
        else:
            # fs.find will recursively walk directories
            # "size" is a common key for all the cloud protocols with fs
            return [
                k
                for k, v in self.fs.find(
                    f"/{self.config.path_without_protocol}",
                    detail=True,
                ).items()
                if v.get("size")
            ]
