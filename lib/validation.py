from prompt_toolkit.validation import Validator, ValidationError
import regex


class BinaryNumberValidator(Validator):
    def validate(self, document) -> None:
        ok = regex.match("\A[01]+\Z", document.text)
        if not ok:
            raise ValidationError(
                message="Please enter a valid binary number.",
                cursor_position=len(document.text)
            )
