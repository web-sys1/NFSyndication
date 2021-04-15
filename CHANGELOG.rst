======================================================
Changelog for NFSyndication (aka News Feed Syndication)
======================================================

A summary of changes in the NFSyndication. For more detailed
information, see [GitHub](https://github.com/web-sys1/NFSyndication).

Use `pip install NFSyndication --upgrade` or `conda upgrade NFSy` to
upgrade to the latest release.


Use `pip install pip --upgrade` to upgrade pip. Check pip version with
`pip --version`.


0.2.23
------
What's new
...........
- Re-arrange code: moving process_entry() and its initials from nfs_main to extras.py
- Extablishing arguments.
- Extablish `__main__.py` file. Adjust script snippets.
- More args to come: outputJSON, comparator_filter.
- Upcoming NamedTuple classes: 'ExtendedPost' and 'Post' tuples into class operator (NamedTuple).

0.2.22
------
- Upgrading the dependencies.

0.2.20
-------
- Another version release: removing from `NFSyndication.module` import `same_module` as known parent package is already opted-in. Always include module.

0.2.0
----------
- Starting project: deploy python package to PyPi.
