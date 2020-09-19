[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/jona/jona-io)

# jona.io

Personal Website, build with [Jekyll](https://jekyllrb.com). See the components used on [this Stack on Stackshare](https://stackshare.io/jona/jona-io).

### Development

Install [Jekyll](https://jekyllrb.com) and it's prerequisites if you don't have them installed yet:
```
gem install bundler jekyll github-pages
```
Serve the website and test your changes locally:
```
cd jonakoudijs.github.io
bundle exec jekyll serve
```
If you want to test outside your local machine (with your phone for example) add the host parameter:
```
cd jonakoudijs.github.io
bundle exec jekyll serve --host 0.0.0.0
```

### Functions

This website is a static site but has a few dynamic components. Javascript retrieves specific data from custom API's to fill certain area's of the website.
Google Cloud functions are exposed as REST API's. These functions are deployed with [gcloud](https://cloud.google.com/functions/docs/quickstart) and can be found in the `_functions` directory.

First you will need to install the gcloud sdk. See the quickstart tutorials for your specific environment: [https://cloud.google.com/sdk/docs/quickstarts](https://cloud.google.com/sdk/docs/quickstarts).

The functions need a few environment variables to be set which are defined in the `env.yml` configuration file. Copy the example `env.yml.example` file to `env.yml` and
add the required values.

To deploy a function go to the `_functions` directory and run the `./deploy.sh` script to deploy one specific or all functions:
```
./deploy all
```
```
./deploy spotify-nowplaying
```
You can find other gcloud functions deploy flags here: [https://cloud.google.com/sdk/gcloud/reference/functions/deploy](https://cloud.google.com/sdk/gcloud/reference/functions/deploy) if you want to change the behaviour of the deployment.
