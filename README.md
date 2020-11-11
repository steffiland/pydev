* https://www.docker.com/blog/containerized-python-development-part-3/

## VSCode Usage:
* if you have an imported distro, make sure to set a non-root default user for the distro in `/etc/wsl.conf`:
  ```
  [user]
  default = myusername
  ```
  (After making the change, restart the distro with `wsl -t distroname` from an windows terminal)
* in WSL, `git clone` this repo and `cd` into it.
* create a python veirtual environment with `python -m venv .envs/dev`
* and source it: `source .envs/dev/bin/activate`
* `pip3 install -r requirements.txt` to install pylint and other useful stuff
* `code .` to start vscode in current folder
* in VS Code taskbar, select Python interpreter "Python 3.xxx ('dev': venv)", now pylint etc should become available

### VS Code Python Cheat Sheet
* <kbd>shift</kbd> + <kbd>enter</kbd>  run currentline/selection
* <kbd>F9</kbd> toogle breakpoint in current line
* <kbd>F5</kbd> Run+Debug; next step. (to cancel the running script and debugger, press <kbd>ctrl</kbd> + <kbd>F5</kbd>)
* 