#!/bin/env python

from    subprocess import call
import  json
import  config

class   Page():
  def   __init__(self, name):
    self.name = name
    self.shortName = self.name.strip()
    self.relpath = "static/" + self.shortName
    
  def   prepare(self):
    call(["hugo", "new", "site", self.relpath])
    call(["git", "clone", config.theme_repo, self.relpath + "/themes/" + config.theme])
    return

  def   configure(self, header, logo, services, optin, footer):
    with open(self.relpath + "/" + config.hugo_config, "w+") as f:
      hugo_config = config.hugo_config_template %(
        self.shortName,
        self.name,
        self.name,
        header,
        self.name,
        self.name,
        optin
      )
      f.write(hugo_config)
    with open(self.relpath + "/data/footer.json", "w+") as f:
      f.write(json.dumps(footer))
    with open(self.relpath + "/data/services.json", "w+") as f:
      f.write(json.dumps(services))

  def   deploy(self):
    return

def	main():
  page = Page("Test Page")
  page.prepare()
  page.configure("This is my generated page",
                 "https://lp1.eu/public/amsell_j.png",
                 {"services": [{"title":"Test"}]},
                 "",
                 {"footer":"Hello I'm the footer"}
  )
  page.deploy()
  return

if __name__ == '__main__':
  main()
