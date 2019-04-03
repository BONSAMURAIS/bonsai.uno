#!/usr/bin/env python
from staticjinja import Site


if __name__ == "__main__":
    site = Site.make_site(env_globals={
        'BASE_URL':'https://bonsamurais.github.io/bonsai.uno/',
    })
    site.render()
