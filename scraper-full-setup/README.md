# WEBSCRAPERAPP

A Sample Web Scraper setup using the Scrapy framework.

## Getting started

```
scrapy crawl <spider_name>
```

### Prerequisites
    
    Main components are:
        Python 2.7.6
        Scrapy 1.5.0
        Scrapyd 1.2.0
        Scrapyd-client 1.1.0

### Installing

1. Install and activate virtualenv 
```
    $pip install virtualenv
    
    $virtualenv -p <python-version> <your virtualenv>

    $./<your virtualenv>/bin/activate
```

2. Install scrapy and other requirements

3. Run spider for supported media
```
    $scrapy crawl <spider name>
```

## Running the tests

```$python -m pytest```

  
e.g Functional test  
***Install chromedriver in your system to pass the functional test**

Test if the user can login with the defined credentials.

            def test_user_can_login(browser):
                login_msg = u'Welcome'
                assert login_msg in browser.find_element_by_xpath(
                "//div[@class='flash-messages']/div").text

## Deployment

scrapy.cfg:

    [settings]
    default = webscraperapp.settings

    [deploy:test]
    url = <url>:<port>
    project = webscraperapp


    [deploy:production]
    url = <url>:<port>
    username = <username>
    password = <password>
    project = webscraperapp


Deploy the app with:

```$ scrapyd-deploy <production, staging, test> -p webscraperapp --version GIT```

---
## Built with:
[Scrapy 1.5.0](https://scrapy.org/)

*Check the documentations for more info.*
          

## Contributing

Please read CONTRIBUTING.md for details.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/rodelrebucas/scrapy-samples). 

## Authors

- [Rodel C. Rebucas](https://github.com/rodelrebucas)

## License

## Acknowledgments
---
## Todos

- [x] Port existing codebase to Python 3.

