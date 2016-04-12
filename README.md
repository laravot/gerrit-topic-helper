# gerrit--helper
Script to perform operations easily on gerrit topic patches and commits present in local branch
(abandon/add reviewers/delete drafts)

## Usage:
 gerrit-helper.py [-h] [-r REVIEWERS [REVIEWERS ...]] [-v]
                        [-cr CODEREVIEW] [-vr VERIFIED] [-a ABANDON]
                        [-d DELETEDRAFTS]
                        {gerrit-topic,current-branch} ...

## Gerrit helper:

positional arguments:
  {gerrit-topic,current-branch}
                        Operation options
    gerrit-topic        Gerrit patches topics
    current-branch      Current local branch

optional arguments:
  -h, --help            show this help message and exit
  -r, --reviewers REVIEWERS [REVIEWERS ...]
                        specifies the reviewers to add to the patches
  -v, --verbose         execute with extensive logging
  -cr, --code-review
                        code review score to apply
  -vr, --verified
                        verified score to apply
  -a, --abandon
                        abandon the topic patches
  -d, --delete-drafts
                        delete draft changes


## Setup:

gerrit-topic-helper requires [pygerrit](https://github.com/sonyxperiadev/pygerrit) to run.
One way to make sure its installed is to use pip:

    pip install pygerrit

Furthermore, you need to replace gerrit.ovirt.org with your Gerrit address.


## Example usages:
python gerrit-helper.py --code-review 0 --verified -1 gerrit-topic --topic test1 --owners laravot@gmail.com -p
ovirt-engine


python gerrit-helper.py --verified 0 -v current-branch --first-commit ba480518d6a6b83c4d7802a13cee812fb32ced21
--last-commit faacba529da7e2556d095b7ca77e8a3fd947e8ab --path /home/ovirt-engine

