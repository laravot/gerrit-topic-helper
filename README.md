# gerrit-topic-helper
Script to perform operations easily on gerrit topic patches (abandon/add reviewers/delete drafts)

## Usage
 gerrit-topic-handler.py [-h] -t TOPICS [TOPICS ...] [-d DELETEDRAFTS]
                               [-a ABANDON] -o OWNERS [OWNERS ...] -p PROJECTS
                               [PROJECTS ...] [-r REVIEWERS [REVIEWERS ...]]
                               [-v] [-cr CODEREVIEW] [-vr VERIFIED]

## Optional arguments:
  -h, --help            show this help message and exit
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        topics to perform on
  -d DELETEDRAFTS, --delete-drafts DELETEDRAFTS
                        delete draft changes
  -a ABANDON, --abandon ABANDON
                        abandon the topic patches
  -o OWNERS [OWNERS ...], --owners OWNERS [OWNERS ...]
                        specifies the owners of the patches
  -p PROJECTS [PROJECTS ...], --projects PROJECTS [PROJECTS ...]
                        specifies the projects
  -r REVIEWERS [REVIEWERS ...], --reviewers REVIEWERS [REVIEWERS ...]
                        specifies the reviewers to add to the patches
  -v, --verbose         execute with extensive logging
  -cr CODEREVIEW, --code-review CODEREVIEW
                        code review to apply
  -vr VERIFIED, --verified VERIFIED
                        verified review to apply

## Setup:

gerrit-topic-helper requires [pygerrit](https://github.com/sonyxperiadev/pygerrit) to run.
One way to make sure its installed is to use pip:

    pip install pygerrit

