from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from core.settings import TEMPLATE_FOLDER


password_msg_regex = 'Minimum eight and maximum 20 characters, at least one uppercase letter, one lowercase letter, one number and one special character:'
password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"


password_light_msg_regex = 'Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:'
password_light_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


templates = Jinja2Templates(directory=TEMPLATE_FOLDER)


def view(request: Request, template: str, context: dict = {},   *args, **kwargs):
    context['request'] = request
    print('====REQUEST', context)
    return templates.TemplateResponse(name=template, context=context,  *args, **kwargs)


def redirect(to: str):
    return RedirectResponse(url=to)
