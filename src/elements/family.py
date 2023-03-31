from src.elements.sub_elements.commonEvent import GedcomCommonEvent
from src.elements.sub_elements.date import GedcomDate
from src.elements.sub_elements.place import GedcomPlace
from .element import GedcomElement


class GedcomFamily(GedcomElement):
    """The family element.
    
    :param level: The level of the family.
    :type level: int
    :param xref: The xref of the family.
    :type xref: str
    :param tag: The tag of the family.
    :type tag: str
    :param sub_elements: The sub elements of the family.
    :type sub_elements: list
    :return: The family.
    :rtype: GedcomFamily
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the family."""
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__husband = self.__find_husband()
        self.__wife = self.__find_wife()
        self.__children = self.__find_children()
        self.__married = self.__find_are_married()
        if self.__married:
            self.__marriage = self.__find_marriage()

    def __find_marriage(self) -> GedcomCommonEvent:
        """Find the marriage of the family.

        :return: The marriage of the family.
        :rtype: GedcomCommonEvent
        """
        if self.find_sub_element("MARR") != []:
            marriage = self.find_sub_element("MARR")[0]
            marriage.__class__ = GedcomCommonEvent
            marriage.init_properties()
            return marriage
        else:
            return None

    def __find_husband(self) -> str:
        """Find the husband of the family.

        :return: The husband of the family.
        :rtype: str
        """
        if self.find_sub_element("HUSB") != []:
            return self.find_sub_element("HUSB")[0].value
        else:
            return ""

    def __find_wife(self) -> str:
        """Find the wife of the family.

        :return: The wife of the family.
        :rtype: str
        """
        if self.find_sub_element("WIFE") != []:
            return self.find_sub_element("WIFE")[0].value
        else:
            return ""

    def __find_children(self) -> list[str]:
        """Find the children of the family.

        :return: The children of the family.
        :rtype: list[str]
        """
        children = []
        for child in self.find_sub_element("CHIL"):
            children.append(child.value)
        return children

    def __find_are_married(self) -> str:
        """Check if the family is married.

        :return: True if the family is married, False otherwise.
        :rtype: bool
        """
        return self.find_sub_element("MARR") != []

    def get_xref(self) -> str:
        """Get the xref of the family.

        :return: The xref of the family.
        :rtype: str
        """
        return self.__xref

    def get_husband(self) -> str:
        """Get the husband of the family.

        :return: The husband of the family.
        :rtype: str
        """
        return self.__husband

    def get_wife(self) -> str:
        """Get the wife of the family.

        :return: The wife of the family.
        :rtype: str
        """
        return self.__wife

    def get_children(self) -> list:
        """Get the children of the family.

        :return: The children of the family.
        :rtype: list
        """
        return self.__children

    def get_parents(self) -> list:
        """Get the parents of the family.

        :return: The parents of the family.
        :rtype: list
        """
        return [self.__husband, self.__wife]

    def get_data(self):
        """Get the data of the family. The result contains husband, wife, children, marriage status and marriage data.

        :return: The data of the family.
        :rtype: dict
        """
        return {
            "husband": self.__husband,
            "wife": self.__wife,
            "children": self.__children,
            "married": self.__married,
            "marriage": self.__marriage.get_data() if self.__married else "",
        }
