from setuptools import setup


def main():
    setup(
        use_scm_version={
            "relative_to": __file__,
            "write_to": "src/collegial/_version.py",
        },
        setup_requires=["setuptools-scm", "setuptools>=40.0"],
    )


if __name__ == "__main__":
    main()
