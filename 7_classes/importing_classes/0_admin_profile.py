# 9.11 & 9.12 - Imported Admin & Multiple Modules
from users import Users
from admin import Admin, Privileges

admin_profile = Admin('tianyao', 'he', 23, 'Male')
admin_profile.describe_user()
admin_profile.privileges.show_privileges()
