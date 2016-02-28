# gerrit-topic-helper
Script to perform operations easily on gerrit topic patches (abandon/add reviewers/delete drafts)

Gerrit topics helper

optional arguments:
  -h, --help            show this help message and exit
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        topics to perform on
  -d DELETEDRAFTS, --delete-drafts DELETEDRAFTS
                        delete draft changes in the specified topics
  -a ABANDON, --abandon ABANDON
                        abandon the changes in the specified topics
  -o OWNERS [OWNERS ...], --owners OWNERS [OWNERS ...]
                        specifies the owners of the patches
  -p PROJECTS [PROJECTS ...], --projects PROJECTS [PROJECTS ...]
                        specifies the projects
  -r REVIEWERS [REVIEWERS ...], --reviewers REVIEWERS [REVIEWERS ...]
                        specifies the reviewers to add to the patches
  -v, --verbose         execute with extensive logging

usage:
python gerrit-topic-handler.py


