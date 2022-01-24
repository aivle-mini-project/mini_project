import re

from django.core.exceptions import ValidationError

def validate_sentence(value):
    if value.isalnum():
        raise ValidationError(
            str(value)+'는 올바른 문장이 아닙니다. 한글로 작성해 주세요')

    check3 = r"[가-힣0-9%.?!~]+"
    regex3 = re.compile(check3)
    if not regex3.match(value):
        raise ValidationError(
            str(value)+'는 올바른 문장이 아닙니다. 한글로만 작성해 주세요')
