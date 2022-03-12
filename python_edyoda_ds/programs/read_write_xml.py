from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as xml_tree

def read_xml(filename):

    data = ""
    with open(filename, "r") as file:
        data = file.read()

    bs_obj = bs(data, "xml")
    waiter_list = bs_obj.find_all("waiter")
    for waiter in waiter_list:
        person = waiter.find("person")
        f_name = person.find("firstname").getText()
        l_name = person.find("lastname").getText()
        gender = person['gender']

        print("Name : {} {}, Gender : {}".format(f_name, l_name, gender))


def write_xml(filename):

    root = xml_tree.Element("waiters")
    waiter = xml_tree.Element("waiter")
    person = xml_tree.Element("person")
    person.attrib["gender"] = "male"
    first_name = xml_tree.Element("firstname")
    first_name.text = "Kallol"
    last_name = xml_tree.Element("lastname")
    last_name.text = "Ghose"

    person.append(first_name)
    person.append(last_name)
    waiter.append(person)
    root.append(waiter)

    tree = xml_tree.ElementTree(root)

    with open(filename, "wb") as file:
        tree.write(file)

read_xml("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/read_dummy_xml.xml")
write_xml("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/write_dummy_xml.xml")