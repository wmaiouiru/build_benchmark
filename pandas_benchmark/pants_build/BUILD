# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs", source="third_party/requirements.txt")

# This target allows us to bundle our app into a PEX binary file via
#  `./pants package`. We can also run it with `./pants run`. See
#  https://www.pantsbuild.org/docs/python-package-goal and
#  https://www.pantsbuild.org/docs/python-run-goal.

pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        "third_party:reqs#pandas",
        "third_party:reqs#fire",
    ],
)

python_sources(
    name="root",
)