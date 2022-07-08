from datetime import datetime

from pydriller import RepositoryMining

for commit in RepositoryMining('path/to/the/repo').traverse_commits():
print('Hash {}, author {}'.format(commit.hash, commit.author.name))


urls = ["repos/repo1", "repos/repo2", "https://github.com/ishepard/pydriller.git",
"repos/repo3", "https://github.com/apache/hadoop.git"]
for commit in RepositoryMining(path_to_repo=urls).traverse_commits():
print("Project {}, commit {}, date {}".format(
commit.project_path, commit.hash, commit.author_date))


for commit in RepositoryMining('path/to/the/repo').traverse_commits():
for modification in commit.modifications:
print('Author {} modified {} in commit {}'.format(commit.author.name,
modification.filename, commit.hash))

for commit in RepositoryMining('path/to/the/repo').traverse_commits():
for mod in commit.modifications:
print('{} has complexity of {}, and it contains {} methods'.format(
mod.filename, mod.complexity, len(mod.methods)))


# analyze only 1 local repository
url = "repos/pydriller/"
# analyze 2 local repositories
url = ["repos/pydriller/", "repos/anotherrepo/"]
# analyze both local and remote
url = ["repos/pydriller/", "https://github.com/apache/hadoop.git", "repos/anotherrepo"]
# analyze 1 remote repository
url = "https://github.com/apache/hadoop.git"


# Analyze single commit
RepositoryMining('path/to/the/repo', single='6411e3096dd2070438a17b225f44475136e54e3a').traverse_commits()
# Since 8/10/2016
RepositoryMining('path/to/the/repo', since=datetime(2016, 10, 8, 17, 0, 0)).traverse_commits()
# Between 2 dates
dt1 = datetime(2022, 7, 8, 17, 0, 0)
dt2 = datetime(2022, 7, 8, 17, 59, 0)
RepositoryMining('path/to/the/repo', since=dt1, to=dt2).traverse_commits()
# Between tags
from_tag = 'tag1'
to_tag = 'tag2'
RepositoryMining('path/to/the/repo', from_tag=from_tag, to_tag=to_tag).traverse_commits()
# Up to a date
dt1 = datetime(2016, 10, 8, 17, 0, 0, tzinfo=to_zone)
RepositoryMining('path/to/the/repo', to=dt1).traverse_commits()
# !!!!! ERROR !!!!! THIS IS NOT POSSIBLE
RepositoryMining('path/to/the/repo', from_tag=from_tag, from_commit=from_commit).traverse_commits()

for commit in RepositoryMining('path/to/the/repo').traverse_commits():
print(
'The commit {"Repository Mining"} has been modified by {Fayshal}, '
'committed by {Fayshal} in date {2022, 7, 8}'.format(
commit.hash,
commit.author.name,

commit.committer.name,
commit.committer_date
)
)

