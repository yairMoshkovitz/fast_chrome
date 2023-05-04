class LINK: # class for html links
    def __init__(self, number, href, text):
        self.href = href
        self.text = text
        self.number = number  # like id number of the object
    def __str__(self):  # if you want to put the link in your page print is.
        return f"<br>{self.number} <a href={self.href}>{self.text}</a>"
