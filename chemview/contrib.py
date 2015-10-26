'''Integration with other programs'''

def topology_mdtraj(traj):
    '''Generate topology spec for the MolecularViewer from mdtraj.

    :param mdtraj.Trajectory traj: the trajectory
    :return: A chemview-compatible dictionary corresponding to the topology defined in mdtraj.

    '''
    import mdtraj as md

    top = {}
    top['atom_types'] = [a.element.symbol for a in traj.topology.atoms]
    top['atom_names'] = [a.name for a in traj.topology.atoms]
    top['bonds'] = [(a.index, b.index) for a, b in traj.topology.bonds]
    top['secondary_structure'] = md.compute_dssp(traj[0])[0]
    top['residue_types'] = [r.name for r in traj.topology.residues ]
    top['residue_indices'] = [ [a.index for a in r.atoms] for r in traj.topology.residues ]

    return top

def topology_pytraj(traj):
    '''Generate topology spec for the MolecularViewer from pytraj.

    :param pytraj.Trajectory or pytraj.TrajectoryIterator (out of memory) traj: the trajectory
    :return: A chemview-compatible dictionary corresponding to the topology defined in pytraj.

    '''
    import pytraj as pt
    # TODO: make pytraj's API similiar to mdtraj so we don't need to have two methods?
    # >>> atom.element
    # ('HYDROGEN', 'H', 1.00794)

    top = {}
    top['atom_types'] = [a.element[1] for a in traj.topology.atoms]
    top['atom_names'] = [a.name for a in traj.topology.atoms]
    top['bonds'] = traj.topology.bond_indices.tolist()
    top['secondary_structure'] = pt.dssp(traj[:1])[1]
    top['residue_types'] = [r.name for r in traj.topology.residues ]
    top['residue_indices'] = [ list(range(r.first_atom_idx, r.last_atom_idx)) for r in traj.topology.residues ]

    return top
