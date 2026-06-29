for changed_package:

    filename = "paint"

    pr_name = ...
    pr_authors = ...

    if package_exists_on_main(filename):

        active_name = ...
        active_authors = ...

        # filename == NAME?
        if filename != active_name:
            fail()

        # GitHub user in AUTHORS?
        if github_user not in parse(active_authors):
            fail()

    else:

        # New package
        if filename != pr_name:
            fail()

success()
