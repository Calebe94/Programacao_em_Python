"""from lxml import etree

# create XML 
root = etree.Element('root')
root.append(etree.Element('child'))
# another child with text
child = etree.Element('child')
child.text = 'some text'
root.append(child)
root.write('arquivo.xml')
# pretty string
s = etree.tostring(root, pretty_print=True)
print (s)"""


"""
import lxml.builder as lb
from lxml import etree

nstext = "new story"
story = lb.E.Asset(
  lb.E.Attribute(nstext, name="Name", act="set"),
  lb.E.Relation(lb.E.Asset(idref="Scope:767"),
            name="Scope", act="set")
  )

print ('story:\n', etree.tostring(story, pretty_print=True))
"""

from xml.dom import minidom

doc = minidom.Document()

root = doc.createElement('root')
doc.appendChild(root)

leaf = doc.createElement('leaf')
text = doc.createTextNode('Text element with attributes')
leaf.appendChild(text)
leaf.setAttribute('color', 'white')
root.appendChild(leaf)

leaf_cdata = doc.createElement('leaf_cdata')
cdata = doc.createCDATASection('<em>CData</em> can contain <strong>HTML tags</strong> without encoding')
leaf_cdata.appendChild(cdata)
root.appendChild(leaf_cdata)

branch = doc.createElement('branch')
branch.appendChild(leaf.cloneNode(True))
root.appendChild(branch)

mixed = doc.createElement('mixed')
mixed_leaf = leaf.cloneNode(True)
mixed_leaf.setAttribute('color', 'black')
mixed_leaf.setAttribute('state', 'modified')
mixed.appendChild(mixed_leaf)
mixed_text = doc.createTextNode('Do not use mixed elements if it possible.')
mixed.appendChild(mixed_text)
root.appendChild(mixed)

xml_str = doc.toprettyxml(indent="  ")
with open("minidom_example.xml", "w") as f:
    f.write(xml_str)
