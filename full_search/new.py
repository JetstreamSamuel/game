import sys

from geocoder import get_ll_span
from mapapi import show_map
from search_org import search_organization


def main():
    search_address = " ".join(sys.argv[1:])

    if search_address:

        ll, span = get_ll_span(search_address)
        org_pos = search_organization(ll)
        show_map(ll, point=org_pos)


if __name__ == "__main__":
    main()