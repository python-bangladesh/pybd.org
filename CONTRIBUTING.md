# Instructions for Contributing

* `Fork` the repo to your account
* `git clone` from your fork
* Add original repo as `upstream`
```bash
git remote add upstream https://github.com/python-bangladesh/pybd.org.git
# if you use ssh, git@github.com:python-bangladesh/pybd.org.git
```
* *Recommended:* Create a local dev branch (ex: `dev-lenin`) and work in that branch
* Before pushing your changes, checkout master branch and pull the latest changes from upstream
```bash
git checkout master
git pull upstream master
```
* Go back to your local dev branch (ex: `dev-lenin`) and `rebase` from master. Resolve any conflicts that may happen in this step
```back
git checkout dev-lenin
git rebase master
# resolve conflicts, if any, and commit before pushing it to github
```
* Push your changes on a new branch in your fork
```bash
git push origin dev-lenin:new-branch-name
```
* Finally go to the original repo and make a Pull Request if everything is ok.

# Instructions for creating Issues
* Mark the issue as either **Support**, **Feature**, **Request** or **Query** (or something else if these do not seem appropriate).

> Support: Module X crashes on system Y.

* If its a support issue, try to include a log and/or other relevant information.
* Use a service such as [gist], [pastebin] or [some alternatives][1] while submitting logs.
* Try and be descriptive about your issues, this helps both the developers and other users that may be reading it :smile:

[gist]: https://gist.github.com
[pastebin]: https://pastebin.com
[1]: http://dpaste.com/
