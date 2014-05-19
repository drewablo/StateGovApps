from scrapy.item import Item, Field

class ILGAitems(Item):
    name = Field()
  	individual_site = Field()
    legislation_number = Field()
  	chamber = Field()
    last_action = Field()
  	last_action_date = Field()
