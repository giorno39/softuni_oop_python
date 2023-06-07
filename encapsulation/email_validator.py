class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        explode = email.split("@")
        username = explode[0]
        mail_parts = explode[1].split(".")
        mail = mail_parts[0]
        domain = mail_parts[1]
        valid_name = self.__is_name_valid(username)
        valid_mail = self.__is_mail_valid(mail)
        valid_domain = self.__is_domain_valid(domain)
        if all([valid_domain, valid_mail, valid_name]):
            return True

        return False



