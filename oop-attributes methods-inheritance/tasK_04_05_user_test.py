from task_02_05_user import *


def test_guest_admin_class(capsys):
    guest = Guest("goha21")

    admin = Admin("joker")

    assert guest.permissions() == "Read-only access: can view content but cannot modify"
    assert admin.permissions() == "Full access: can add, edit, delete users and settings"

