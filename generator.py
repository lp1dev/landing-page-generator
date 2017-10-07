#!/bin/env python

from    subprocess import call
import  json
import  config

class   Page():
  def   __init__(self, name):
    self.name = name
    self.shortName = self.name.lower().replace(' ', '-')
    self.relpath = "sites/" + self.shortName
    
  def   configure(self, page_config):
    with open(config.hugo_config, "w+") as f:
      hugo_config = config.hugo_config_template %(
        self.shortName,
        self.name,
        page_config['description'],
        page_config['mainTitle'],
        page_config['logo'],
        page_config['subTitle'],
        page_config['optinTitle'],
        page_config['optinFormTitle'],
        page_config['background']
      )
      f.write(hugo_config)
    with open("data/footer.json", "w+") as f:
      f.write(json.dumps(page_config['footer']))
    with open("data/services.json", "w+") as f:
      f.write(json.dumps(page_config['services']))

  def   deploy(self):
    call(["hugo", "-d", self.relpath])
    return

def	main():
  page = Page("Test Page")
  page_config = {
    "description": "lp1.eu - Generated Page - Description",
    "mainTitle": "Generated page main title",
    "logo": "https://lp1.eu/res/svg/avatar.svg",
    "subTitle": "Generated Page subtitle",
    "optinTitle": "Generated Page optInTitle",
    "optinFormTitle": "Generated Page optinFormTitle",
    "background": "img/bg.png",
    "services": {"services":[{"title": "Test Generated Service", "description": "Test description"}]},
    "footer": {"footer": "Test Generated footer"}
  } ## Default page config
  page.configure(page_config)
  page.deploy()
  return

if __name__ == '__main__':
  main()
