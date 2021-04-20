======================================================
Changelog for NFSyndication (aka News Feed Syndication)
======================================================

A summary of changes in the NFSyndication. For more detailed
information, see REPOSITORY_.

Use `pip install NFSyndication --upgrade` or `conda upgrade NFSy` to
upgrade to the latest release.


Use `pip install pip --upgrade` to upgrade pip. Check pip version with
`pip --version`.

0.2.25
------
20 April 2021
.............
- Fixing background faults, by giving further improvements. See ``NFSyndication/nfs_main.py`` and ``extras.py`` (diff-`a63e8a220f8551cd5dba8c5ff9fb0fd82f0478a6e4fa432caf11c22f85427061`_)
- Improving additional logging output (on ``nfsyndication-src --verbose`` command).

.. _a63e8a220f8551cd5dba8c5ff9fb0fd82f0478a6e4fa432caf11c22f85427061: https://github.com/web-sys1/NFSyndication/commit/7011cf3249cee8f2800a192b87f6c80eb1d10fb3#diff-a63e8a220f8551cd5dba8c5ff9fb0fd82f0478a6e4fa432caf11c22f85427061


0.2.23
------
What's new (15 April 2021)
...........
- Re-arrange code: moving ``process_entry()`` and its initials from ``nfs_main`` to extras.py
- Extablishing arguments.
- Extablish ``__main__.py`` file. Adjust script snippets.
- More args to come: ``outputJSON``, ``comparator_filter``.
- Upcoming NamedTuple classes: 'ExtendedPost' and 'Post' tuples into class operator (``NamedTuple``).

0.2.22
------
March 2021
..........
- Upgrading the dependencies.

0.2.20
-------
September 2020
..............
- Another version release: removing from ``NFSyndication.module`` import ``same_module`` as known parent package is already opted-in. Always include module.

0.2.0
----------
August 2020
............
- Starting project: deploy python package to PyPi.

.. _REPOSITORY: https://github.com/web-sys1/NFSyndication/
