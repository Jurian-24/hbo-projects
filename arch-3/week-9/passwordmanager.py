class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords

    def set_password(self, new_password):
        if self.is_correct(new_password):
            if new_password in self.old_passwords:
                return

            self.old_passwords.append(new_password)

    def is_correct(self, new_password):
        if len(self.old_passwords) != 0:
            current_password = self.old_passwords[-1]

            if current_password != new_password:
                return True

        elif len(self.old_passwords) == 0:
            return True

        return False
