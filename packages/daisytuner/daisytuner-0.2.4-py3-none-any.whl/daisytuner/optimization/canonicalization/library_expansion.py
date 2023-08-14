import dace


class LibraryExpansion:
    """ """

    @classmethod
    def apply(cls, sdfg: dace.SDFG) -> None:
        sdfg.expand_library_nodes(recursive=True)
