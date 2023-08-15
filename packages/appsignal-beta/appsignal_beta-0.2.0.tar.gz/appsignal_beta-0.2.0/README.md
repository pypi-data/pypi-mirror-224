# AppSignal Python: Deprecated package

The `appsignal-beta` Python package is now deprecated.

Please install [the `appsignal` Python package](https://pypi.org/project/appsignal/) instead.

## Release

Update the `pyproject.toml` file and update the version number.

Run these two commands:

```
rm -rf dist
hatch build
hatch publish
```

Tag the release in Git:

```
git tag v#.#.#
git push main v#.#.#
```
