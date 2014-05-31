import scraperwiki
import urllib2
import lxml.etree
import re

u=urllib2.urlopen("http://ilga.gov/legislation/votehistory/98/senate/09800HB3794_05312014_001000T.pdf")
x = scraperwiki.pdftoxml(u.read())
root = lxml.etree.fromstring(x)

pages = list(root)
chamber = str()
vv=[]

for page in pages:
	for el in page:
		if el.tag == 'text':
			if int(el.attrib['top']) > 150 and int(el.attrib['left']) > 400 and int(el.attrib['top']) <200:
				chamber = el.text
			if re.findall("Senate Vote", chamber):
				if int(el.attrib['top']) == 230:
					title = el.text
					if (re.findall('House', title)):
						title = (re.findall('[0-9]+', title))
						title = "HB"+title[0]
				if int(el.attrib['top']) == 332 and int(el.attrib['left']) < 100:
					yeas = el.text
				if int(el.attrib['top']) == 332 and int(el.attrib['left']) > 340 and int(el.attrib['left']) <600 :
					nays = el.text
				if int(el.attrib['top']) == 332 and int(el.attrib['left']) > 600:
					present = el.text
				if int(el.attrib['top']) > 350 and int(el.attrib['top']) < 650:
					r = el.text
				if int(el.attrib['top']) >370 and int(el.attrib['top']) <650:
					r = el.text
					names = re.findall(r'[A-z-\u00F1]{3,}',r)
					votes = re.findall(r'[A-Z]{1,2}\s',r)
					for name in names:
						legi = name
						for vote in votes:
							v = vote
				

