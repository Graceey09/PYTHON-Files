class DogException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WrongPinException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidInputException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class AccountErrorException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
