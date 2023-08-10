from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class Repo:
    group: str
    name: str

    @classmethod
    def from_url(cls, url: str) -> "Repo":
        parsed_url = urlparse(url)
        path_components = parsed_url.path.rstrip("/").split("/")
        return cls(group=path_components[-2], name=path_components[-1])

    def to_url(self) -> str:
        return f"https://github.com/{self.group}/{self.name}"
