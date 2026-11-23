from numpy import arange, meshgrid, sqrt
from numpy.typing import NDArray

α_lit = 1.747558

Coordinate = tuple[int, int, int]
Grid = tuple[NDArray, NDArray, NDArray]

def coordinate_differences(N: int, reference: Coordinate) -> Grid:
    """Create meshgrid with coordinate differences of all lattice ions to the reference ion."""
    return meshgrid(
        arange(N) - reference[0],
        arange(N) - reference[1],
        arange(N) - reference[2],
        indexing="ij",
    )

def charge_signs(dx: NDArray, dy: NDArray, dz: NDArray) -> NDArray:
    """Plus for opposite charges, minus for like charges.

    On the NaCl lattice the sign alternates with the parity of
    dx + dy + dz: odd parity means opposite charge.
    """
    parity = (dx+dy+dz) % 2
    return 2*parity - 1

def pair_terms(N: int, reference: Coordinate) -> NDArray:
    """Calculate all terms +-1/alpha_ij."""
    dx, dy, dz = coordinate_differences(N, reference)
    α_ij = sqrt(dx*dx + dy*dy + dz*dz)
    relevant = α_ij > 0  # mask for excluding the reference ion

    return charge_signs(dx, dy, dz)[relevant] / α_ij[relevant]

def madelung_const(position: str, N: int, reference: Coordinate) -> None:
    α = float(pair_terms(N, reference).sum())
    Δα = α - α_lit
    print(f"N = {N}; (bezogen auf {position}):\nα = {α:.6f}   (α - α_literatur = {Δα:+.6f})")

print("Referenz-Ion im Zentrum:")
for N in (20, 21, 22, 23):
    anchor = (N // 2, N // 2, N // 2)
    madelung_const("das Zentrum", N, anchor)

print("\nReferenz-Ion an anderen Positionen (nur für N = 20):")
center = (10, 10, 10)
face = (9, 9, 19)
corner = (0, 0, 0)
madelung_const("das Zentrum", 20, center)
madelung_const("die Mitte einer Seitenfläche", 20, face)
madelung_const("eine Ecke", 20, corner)

print(f"\nLiteraturwert: α = {α_lit}")
