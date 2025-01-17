from abc import ABC, abstractmethod
from sinch.core.clients.sinch_client_configuration import Configuration
from sinch.domains.authentication import AuthenticationBase
from sinch.domains.numbers import NumbersBase
from sinch.domains.conversation import ConversationBase
from sinch.domains.sms import SMSBase


class ClientBase(ABC):
    """
    Sinch abstract base class for concrete Sinch Client implementations.
    By default, this SDK provides two implementations - sync and async.
    Feel free to utilize any of them for you custom implementation.
    """
    configuration = Configuration
    authentication = AuthenticationBase
    numbers = NumbersBase
    conversation = ConversationBase
    sms = SMSBase

    @abstractmethod
    def __init__(
        self,
        key_id,
        key_secret,
        project_id,
        logger_name=None,
        logger=None,
        application_key: str = None,
        application_secret: str = None
    ):
        pass

    def __repr__(self):
        return f"Sinch SDK client for project_id: {self.configuration.project_id}"
