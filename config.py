## Hugo configuration
theme = "vertical-land"
theme_repo = "https://github.com/lp1dev/vertical-land.git" ## Theme repository
hugo_config = "config.toml" ## Hugo config file
hugo_config_template = """
baseurl = "https://lp1.eu/%s"
languageCode = "en-us"
title = "%s"
theme = "vertical-land"

[params]
description = "%s"
mainTitle = "%s"
logo = "%s"
subTitle = "%s"
optinTitle = "%s"
optinFormTitle = "%s"
background = "%s" """
