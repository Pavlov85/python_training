import pymysql.cursors
import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, phone2, notes from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, phone2, notes) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, nickname=nickname,
                 title=title, lastname=lastname, company=company,
                 adress=address, home=home, work=work, mobile=mobile,
                 fax=fax, email=email, email2=email2, email3=email3,
                 homepage=homepage, byear=byear, ayear=ayear, address2=address2,
                 phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return contact_list
