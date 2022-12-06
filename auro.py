import time
import xml.etree.ElementTree as ET

# filename = orders.xml

tree = ET.parse("orders.xml")

root = tree.getroot()

print(root)
print(root[0].attrib) 
print(root[5][0].text)

# F = open(filename,"r")

# while(F.readline()) :


