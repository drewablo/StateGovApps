import scraperwiki
from bs4 import BeautifulSoup
import urllib2
import lxml.etree
import re

u=urllib2.urlopen("http://ilga.gov/legislation/votehistory/98/house/09800HB3794_05292014_059000T.pdf")
x = scraperwiki.pdftoxml(u.read())
root = lxml.etree.fromstring(x)

pages = list(root)
chamber = str()


for page in pages:
	for el in page:
		if el.tag == 'text':
			if int(el.attrib['top']) == 168:
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
			elif int(el.attrib['top']) == 189:
				chamber = el.text
			if re.findall("HOUSE ROLL CALL", chamber):
				if int(el.attrib['top']) == 209:
					title = el.text
					if (re.findall('HOUSE', title)):
						title = (re.findall('[0-9]+', title))
						title = "HB"+title[0]
					elif (re.findall('Senate', title)):
						title = (re.findall('[0-9]+', title))
						title = "SB"+title[0]
				if int(el.attrib['top']) == 352 and int(el.attrib['left']) < 100:
					yeas = el.text
				if int(el.attrib['top']) == 332 and int(el.attrib['left']) > 350 and int(el.attrib['left']) <600 :
					nays = el.text
				if int(el.attrib['top']) == 332 and int(el.attrib['left']) > 600:
					present = el.text
				if int(el.attrib['top']) > 350 and int(el.attrib['top']) < 650:
					r = el.text
				if int(el.attrib['top']) >385 and int(el.attrib['top']) <1000:
					r = el.text
					names = re.findall(r'[A-z-\u00F1]{3,}',r)
					votes = re.findall(r'[A-Z]{1,2}\s',r)
					for name in names:
						legi = name
						for vote in votes:
							v = vote
						print title, legi, v			
			
