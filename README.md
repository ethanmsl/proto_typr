# proto_typr
Test Repo for use with [Typer CLI framework](https://typer.tiangolo.com/)

Note:
`coverage` had some issues -- possibly related to the typer framework -- `coverage` pre-commit hook tests would only acknowledge files after commenting out all of the typer code in `__main__.py`, strangely they continued running after uncommenting.
I was not able to find anything on this suggesting it may not be a persitant problem.  However the fact that typer runs many of the programs may indirection that confuses coverage.
`pytest` tested all the files without a problem however.


