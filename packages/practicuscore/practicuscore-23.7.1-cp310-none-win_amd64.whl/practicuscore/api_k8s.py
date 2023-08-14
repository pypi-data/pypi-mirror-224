import hashlib
from dataclasses import dataclass
from typing import Optional, List

from practicuscore.util import CryptoUtil


class K8sAuthToken:
    def __init__(self, refresh_token: str, access_token: str) -> None:
        self.refresh_token = refresh_token
        self.access_token = access_token


@dataclass
class K8sClusterDefinition:
    name: str = ""
    region_name: str = ""


class K8sConfig:
    def __init__(self, host_url: str, email: str, refresh_token: Optional[str] = None):
        super().__init__()
        self.host_url = host_url
        self.email = email
        self.refresh_token = refresh_token
        self.password: Optional[str] = None
        self.cluster_name: Optional[str] = None
        self.region_name: Optional[str] = None

    def to_dict(self) -> dict:
        conf_dict = {'host_url': self.host_url, 'email': self.email}

        if self.password is not None:
            conf_dict['password'] = self.password

        if self.refresh_token is not None:
            conf_dict['refresh_token'] = self.refresh_token

        if self.cluster_name is not None:
            conf_dict['cluster_name'] = self.cluster_name

        if self.region_name is not None:
            conf_dict['region_name'] = self.region_name

        return conf_dict

    @staticmethod
    def from_dict(dict_item: dict) -> 'K8sConfig':
        k8s_config = K8sConfig(
            host_url=dict_item['host_url'], email=dict_item['email'], refresh_token=dict_item['refresh_token'])
        k8s_config.password = dict_item['password']
        k8s_config.cluster_name = dict_item['cluster_name']
        k8s_config.region_name = dict_item['region_name']
        return k8s_config

    def set_password(self, password_plain_text: str):
        self.password = CryptoUtil.encrypt(password_plain_text)

    @property
    def password_in_plain_text(self) -> Optional[str]:
        if self.password:
            return CryptoUtil.decrypt(self.password)
        else:
            return None

    @property
    def ssl(self) -> bool:
        return self.host_url.startswith("https")

    @property
    def host_dns(self) -> str:
        return self.host_url.replace("https://", "").replace("http://", "")

    @property
    def hash_key(self) -> str:
        text_to_hash = f"{self.host_url}-{self.email}-{self.refresh_token}-{self.password}"
        m = hashlib.md5()
        m.update(bytes(text_to_hash, "utf-8"))
        return str(m.hexdigest())


class ModelPrefix:

    def __init__(self, key: str, prefix: str) -> None:
        super().__init__()
        self.key = key
        self.prefix = prefix


class ModelDeployment:

    def __init__(self, key: str, name: str) -> None:
        super().__init__()
        self.key = key
        self.name = name


class ModelVersionInfo:
    def __init__(self, version_tag: str, version: str | None = None):
        self.version_tag = version_tag
        self.version = version

    @staticmethod
    def create_from_version(version: str) -> 'ModelVersionInfo':
        return ModelVersionInfo(version_tag=f"v{version}", version=version)

    @staticmethod
    def create_latest() -> 'ModelVersionInfo':
        return ModelVersionInfo(version_tag="latest")

    @staticmethod
    def create_production() -> 'ModelVersionInfo':
        return ModelVersionInfo(version_tag="production")

    @staticmethod
    def create_staging() -> 'ModelVersionInfo':
        return ModelVersionInfo(version_tag="staging")


class ModelMetaVersion:
    def __init__(self, version_id: int, version: str, model_deployment: ModelDeployment, stage: Optional[str] = None) -> None:
        super().__init__()
        self.id = version_id
        self.version = version
        self.stage = stage
        self.model_deployment = model_deployment

    def to_model_version_info(self) -> ModelVersionInfo:
        return ModelVersionInfo.create_from_version(self.version)


class ModelMeta:

    def __init__(self, model_id: int, name: str, model_prefix: ModelPrefix, model_versions: List[ModelMetaVersion]) \
            -> None:
        super().__init__()
        self.model_id = model_id
        self.name = name
        self.model_prefix = model_prefix
        self.model_versions = model_versions

    @property
    def production_version(self) -> Optional[ModelMetaVersion]:
        for model_meta_version in self.model_versions:
            if model_meta_version.stage == "Production":
                return model_meta_version
        return None

    @property
    def staging_version(self) -> Optional[ModelMetaVersion]:
        for model_meta_version in self.model_versions:
            if model_meta_version.stage == "Staging":
                return model_meta_version
        return None
