class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, rest = email.split("@")
        mail, domain = rest.split(".")
        if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True

        return False


mails = ["me"]
domains = ["you", "he"]
email_validator = EmailValidator(5, mails, domains)
print(email_validator.validate("itsme@me.you"))
print(email_validator.validate("me@me.you"))
print(email_validator.validate("itsme@me.she"))
print(email_validator.validate("itsme@you.he"))
