from pygerrit.ssh import GerritSSHClient
import json
import argparse
import logging
import sys

parser = argparse.ArgumentParser(description='Gerrit topics helper')
parser.add_argument('-t','--topics', nargs='+', help='topics to perform on', required=True)
parser.add_argument('-d', '--delete-drafts',  dest='deleteDrafts', help='delete draft changes')
parser.add_argument('-a', '--abandon',  dest='abandon', help='abandon the topic patches')
parser.add_argument('-o', '--owners', nargs='+', help='specifies the owners of the patches', required=True)
parser.add_argument('-p', '--projects', nargs='+', help='specifies the projects', required=True)
parser.add_argument('-r', '--reviewers', nargs='+', help='specifies the reviewers to add to the patches')
parser.add_argument('-v', '--verbose', action='store_true', help='execute with extensive logging')
parser.set_defaults(abandon=False)

args = parser.parse_args()
d = vars(args)

log = logging.getLogger('Gerrit-topic-helper')
log.setLevel(logging.INFO)
sl = logging.StreamHandler(sys.stdout)
sl.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s::%(levelname)s::%(message)s')
sl.setFormatter(formatter)
log.addHandler(sl)
if d["verbose"]:
	log.setLevel(logging.DEBUG)

def safeGet(key, d):
        if key in d:
                return d[key]
        return None

def applyProp(d, query, prop, arg, sep):
	p = safeGet(arg, d)
        if p is not None:
        	tmp = sep.join(p)

        query+=" {}:{} ".format(prop, tmp)
        return query

def applyOrProp(d, query, prop, arg):
	return applyProp(d, query, prop, arg, " OR ")


client = GerritSSHClient("gerrit.ovirt.org")

def run_gerrit_command(command):
        try:
                return client.run_gerrit_command(command)
        except Exception as e:
                print 'Error when running gerrint command:', e

query = "query --format=JSON status:open --current-patch-set limit:1"
query = applyOrProp(d, query, "owner", "owners")
query = applyOrProp(d, query, "topic", "topics")
query = applyOrProp(d, query, "project", "projects")
log.info("Running query %s", query)
result = run_gerrit_command(query)
data = result.stdout.readlines()
data = data[:-1]


reviewers = safeGet("reviewers", d)
for line in data:
	parsed=json.loads(line)
	print parsed

	commit=parsed["currentPatchSet"]["revision"]
	if reviewers is not None:
		reviewers_com = "set-reviewers {} --add ".format(commit)
		reviewers_com+="--add ".join(reviewers)
		log.debug("adding reviewers using command %s", reviewers_com)
		run_gerrit_command(client, reviewers_com)

	deleteDrafts = safeGet("deleteDrafts", d)
	abandon = safeGet("abandon", d)
	if deleteDrafts or abandon:
		if parsed["status"]=="DRAFT":
			if deleteDrafts:
				log.debug("deleting draft commit %s", commit)
				client.run_gerrit_command("review --delete {}".format(commit))
				continue
			log.debug("publishing draft commit %s", commit)
			client.run_gerrit_command("review --publish {}".format(commit))
		if abandon:
			log.debug("abandoning %s", commit)
			client.run_gerrit_command("review --abandon {}".format(commit))
