import numpy as np
from decimal import Decimal
import os
import dataclasses
import tempfile
from typing import Union, List, Tuple, Dict, Any, Optional, Callable
import networkx as nx
import yaml


class Atom:
    def __init__(self, element, position,speed=[0.0,0.0,0.0] ,is_fixed=False):
        self.element = element
        self.position = position
        self.speed = speed
        self.is_fixed = is_fixed


class POSCAR:
    atoms = None
    filename = None
    elements = None
    num_elements = None
    comment = None
    scaling_factor = None
    lattice_vectors = None
    filetype = None
    coordtype = None

    def __init__(self, filename, filetype='POSCAR'):
        self.atoms = []
        self.filename = filename
        self.elements = []
        self.num_elements = []
        self.comment = None
        self.scaling_factor = None
        self.lattice_vectors = None
        self.filetype= filetype
        self.coordtype=None
        self.read_file(filetype=self.filetype)
        

    def read_file(self,filetype):
        if filetype=='POSCAR':
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                self.comment = lines[0].strip()
                self.scaling_factor = float(lines[1])
                self.lattice_vectors = [list(map(float, line.split())) for line in lines[2:5]]
                self.elements = lines[5].strip().split()
                self.num_elements = list(map(int, lines[6].strip().split()))                
                # 遍历每一行，查找关键词
                for line in lines:
                    if 'Cartesian' in line:  # 如果这一行包含关键词
                        self.coordtype='Cartesian'
                    if 'Direct' in line:  # 如果这一行包含关键词
                        self.coordtype='Direct'
                for i, num in enumerate(self.num_elements):
                    page_start=9  if lines[7].strip() == "Selective Dynamics"   else   8
                    for line in lines[page_start + sum(self.num_elements[:i]): page_start + sum(self.num_elements[:i+1])]:
                        position = list(map(float, line.split()[:3]))
                        if self.coordtype == "Direct":
                            position = self.direct_to_cartesian(position)
                        is_fixed = line.split()[3:] == ['F', 'F', 'F']
                        self.atoms.append(Atom(self.elements[i], position, [0,0,0],is_fixed))
                        
        elif filetype=='CONTCAR':
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                self.comment = lines[0].strip()
                self.scaling_factor = float(lines[1])
                self.lattice_vectors = [list(map(float, line.split())) for line in lines[2:5]]
                self.elements = lines[5].strip().split()
                self.num_elements = list(map(int, lines[6].strip().split()))
                totalnums=np.sum(self.num_elements)
                # 遍历每一行，查找关键词
                for line in lines:
                    if 'Cartesian' in line:  # 如果这一行包含关键词
                        self.coordtype='Cartesian'
                    if 'Direct' in line:  # 如果这一行包含关键词
                        self.coordtype='Direct'
                for i, num in enumerate(self.num_elements):
                    page_start=9  if lines[7].strip() == "Selective dynamics"   else   8
                    
                    for ii in range(page_start + sum(self.num_elements[:i]), page_start + sum(self.num_elements[:i+1])):
                        atominfo_line=lines[ii]
                        speedinfo_line=lines[ii+totalnums+1]
                        position = list(map(float, atominfo_line.split()[:3]))
                        if self.coordtype == "Direct":
                            position = self.direct_to_cartesian(position)
                        is_fixed = atominfo_line.split()[3:] == ['F', 'F', 'F']
                        speed=list(map(float, speedinfo_line.split()[:3]))
                        self.atoms.append(Atom(self.elements[i], position,speed, is_fixed))

    def write_file(self, filename,speed_tag=False):
        # 创建元素和对应原子的字典
        elements_dict = {}
        for atom in self.atoms:
            if atom.element in elements_dict:
                elements_dict[atom.element].append(atom)
            else:
                elements_dict[atom.element] = [atom]

        # 按照元素的出现顺序排序
        elements_sorted = sorted(elements_dict.keys(), key=lambda x: self.elements.index(x))
        # 获取排序后的元素对应的原子数目
        num_elements_sorted = [len(elements_dict[x]) for x in elements_sorted]

        with open(filename, 'w') as f:
            f.write(self.comment + "\n")
            f.write(f"{self.scaling_factor}\n")
            for vector in self.lattice_vectors:
                f.write(" ".join(map(str, vector)) + "\n")
            f.write(" ".join(elements_sorted) + "\n")
            f.write(" ".join(map(str, num_elements_sorted)) + "\n")
            f.write("Selective Dynamics\n")
            f.write("Cartesian\n")
            speedinfototal='\n'
            for element in elements_sorted:
                for atom in elements_dict[element]:
                    f.write(" ".join(format(Decimal(coord), ".10f") for coord in atom.position) + " ")
                    if atom.is_fixed:
                        f.write("F F F\n")
                    else:
                        f.write("T T T\n")
                    speedinfo_one=" ".join(format(Decimal(coord), ".10f") for coord in atom.speed) + " \n"
                    speedinfototal+=speedinfo_one
            if speed_tag==True:
                f.write(speedinfototal)

    def add_atom(self, element, position, is_fixed=False):
        self.atoms.append(Atom(element, position, [0,0,0],is_fixed))
        if element in self.elements:
            self.num_elements[self.elements.index(element)] += 1
        else:
            self.elements.append(element)
            self.num_elements.append(1)

    def remove_atom(self, index):
        del self.atoms[index]

    def display(self):
        for i, atom in enumerate(self.atoms):
            print(f'Atom {i+1}: Element = {atom.element}, Position = {atom.position}, Fixed = {atom.is_fixed}')

    def filter_atoms(self, ranges):
        new_atoms = []
        for atom in self.atoms:
            if all(r[0] <= p <= r[1] for p, r in zip(atom.position, ranges)):
                new_atoms.append(atom)
        self.atoms = new_atoms
        
    def display_atoms(self): 
        for i, atom in enumerate(self.atoms):
            print(f"Atom {i+1}:")
            print(f"Element: {atom.element}")
            print(f"Position: {atom.position}")
            print(f"Speed: {atom.speed}")
            print(f"Is fixed: {atom.is_fixed}")
            print()
            
    def fix_atoms_in_region(self, region):
        """
        Fix atoms within a certain region. The region is defined as [[xmin,xmax],[ymin,ymax],[zmin,zmax]]

        :param region: The region to fix atoms in.
        """
        xmin, xmax = region[0]
        ymin, ymax = region[1]
        zmin, zmax = region[2]

        for atom in self.atoms:
            x, y, z = atom.position
            if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
                atom.is_fixed = True
    
    def unfix_atoms_in_region(self, region):
        """
        Unfix atoms within a certain region. The region is defined as [[xmin,xmax],[ymin,ymax],[zmin,zmax]]

        :param region: The region to unfix atoms in.
        """
        xmin, xmax = region[0]
        ymin, ymax = region[1]
        zmin, zmax = region[2]

        for atom in self.atoms:
            x, y, z = atom.position
            if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
                atom.is_fixed = False
                
    def direct_to_cartesian(self, direct_coords):
        lattice_matrix = np.array(self.lattice_vectors)
        direct_coords = np.array(direct_coords)
        cartesian_coords = np.dot(direct_coords, lattice_matrix)
        return cartesian_coords.tolist()

    def remove_molecules(self, max_atoms=8, fixed_threshold=2, output_file='removed_molecules.yaml'):
        """
        Removes molecules from the POSCAR object based on the criteria:
        1) The number of fixed atoms in the molecule should be less than fixed_threshold.
        2) The number of atoms in the molecule should not exceed max_atoms.

        :param max_atoms: The maximum number of atoms allowed in a molecule to be removed.
        :param fixed_threshold: The maximum number of fixed atoms allowed in a molecule to be removed.
        :param output_file: The name of the output file to store information about removed molecules.
        """
        # Dictionary to store information about removed molecules
        removed_molecules_info = {}

        # List to store indices of atoms to be removed
        indices_to_remove = []

        # Iterate through the atoms in the POSCAR object
        for i, atom in enumerate(self.atoms):
            # Check if the atom is part of a molecule that should be removed
            same_type_atoms = [a for a in self.atoms if a.element == atom.element]
            num_fixed_atoms = sum(1 for a in same_type_atoms if a.is_fixed)

            # Check the criteria for removing the molecule
            if len(same_type_atoms) <= max_atoms and num_fixed_atoms < fixed_threshold:
                # If the atom is not fixed, mark it for removal
                if not atom.is_fixed:
                    element = atom.element
                    indices_to_remove.append(i)
                    # Update the removed molecules information
                    removed_molecules_info[element] = removed_molecules_info.get(element, 0) + 1

        # Remove the marked atoms in reverse order to avoid index shifting
        for index in reversed(indices_to_remove):
            del self.atoms[index]

        # Write the removed molecules information to a YAML file
        with open(output_file, 'w') as file:
            yaml.dump(removed_molecules_info, file, default_flow_style=False)

@dataclasses.dataclass
class XDATCARParser:
    """
    A parser for XDATCAR files.

    Attributes:
        file_raw_str (str): Raw content of the XDATCAR file.
        file_header_str (str): Header content of the XDATCAR file.
        frame_list (List): List of frames parsed from the XDATCAR file.
        total_frame (int): Total number of frames in the XDATCAR file.
    """

    file_raw_str: str = None
    file_header_str: str = None
    frame_list: List = dataclasses.field(default_factory=list)
    total_frame: int = 0

    def __init__(self, filename: str):
        """
        Initializes the XDATCARParser with the given filename.

        :param filename: Path to the XDATCAR file.
        """
        self.filename = filename
        self.frame_list = []

    def _parse(self):
        """
        Parses the XDATCAR file and stores the frames in frame_list.
        """
        # Read the file and store its contents in file_raw_str
        with open(self.filename, 'r') as f:
            self.file_raw_str = f.read()

        # Read the first 7 lines for the header
        self.file_header_str = '\n'.join(self.file_raw_str.split('\n')[:7]) + "\n" + "Selective Dynamics\n" + "Direct"
        self.total_frame = self.get_max_step_from_XDATCAR()

        # Split the file into frames based on "Direct configuration=" lines
        frames = self.file_raw_str.split("Direct configuration=")[1:]

        # Check if the number of frames matches the total number of steps
        assert len(frames) == self.total_frame, "The number of frames is not equal to the number of steps!"

        # Process each frame
        for frame in frames:
            frame = "\n".join(frame.split("\n")[1:])
            POSCAR_str = self.file_header_str + "\n" + frame

            # Create a temporary file for this frame
            with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
                temp_file.write(POSCAR_str)
                temp_file.flush()
                temp_file_path = temp_file.name

                # Process the temporary file (assuming POSCAR is a class or function that processes it)
                POSCAR_parser = POSCAR(temp_file_path)
                self.frame_list.append(POSCAR_parser)

    def save_specific_frame(self, idx: int, name: str = "POSCAR"):
        """
        Save a specific frame to a POSCAR file.

        :param idx: The index of the frame to save.
        :param name: The name of the output file.
        """
        self.frame_list[idx].write_file(name)

    def count_atoms_at_specific_frame(self, idx: int) -> int:
        """
        Count the number of atoms in a specific frame.

        :param idx: The index of the frame to count.
        :return: The number of atoms in the specified frame.
        """
        return len(self.frame_list[idx].atoms)

    def get_max_step_from_XDATCAR(self) -> int:
        """
        Get the maximum step number from the XDATCAR file.

        :return: The maximum step number.
        """
        max_step = 0
        with open(self.filename, 'r') as f:
            for line in f:
                if line.startswith('Direct configuration='):
                    step = int(line.split('=')[1].strip())
                    if step > max_step:
                        max_step = step
        return max_step


class MoleculeIdentifier:
    """
    A class to identify molecules in a POSCAR object.

    Attributes:
        poscar (POSCAR): The POSCAR object containing atomic information.
        molecule_groups (dict): A dictionary containing identified molecules.
    """

    def __init__(self, poscar):
        """
        Initializes the MoleculeIdentifier with a POSCAR object.

        :param poscar: A POSCAR object containing atomic information.
        """
        self.poscar = poscar
        self.molecule_groups = {}

    def calculate_distance(self, atom1, atom2) -> float:
        """
        Calculates the Euclidean distance between two atoms.

        :param atom1: The first atom.
        :param atom2: The second atom.
        :return: The Euclidean distance between the two atoms.
        """
        position1 = np.array(atom1.position)
        position2 = np.array(atom2.position)
        return np.linalg.norm(position1 - position2)

    def is_bonded(self, atom1: Atom, atom2: Atom, bonding_thresholds: dict = None) -> bool:
        """
        Determines if two atoms are bonded based on their distance.

        :param atom1: The first atom.
        :param atom2: The second atom.
        :param bonding_thresholds: A dictionary containing bonding thresholds for different pairs of atom types.
        :return: True if the atoms are bonded, False otherwise.
        """
        distance = self.calculate_distance(atom1, atom2)

        # Check if bonding_thresholds dictionary is provided
        if bonding_thresholds:
            # Get the atom types
            atom_type1 = atom1.element
            atom_type2 = atom2.element

            # Sort the atom types lexicographically to ensure consistent ordering
            atom_type1, atom_type2 = sorted([atom_type1, atom_type2])

            # Get the bonding threshold for this pair of atom types
            threshold = bonding_thresholds.get((atom_type1, atom_type2), 1.5)
        else:
            # Use default threshold
            threshold = 1.5

        # Check if the distance is less than the threshold
        return distance < threshold

    def identify_molecules(self) -> Dict:
        """
        Identifies molecules in the POSCAR object.

        :return: A dictionary containing identified molecules.
        """
        # Create a graph
        graph = nx.Graph()

        # Add nodes (atoms)
        for i, atom in enumerate(self.poscar.atoms):
            graph.add_node(i)

        # Add edges (bonds)
        for i, atom1 in enumerate(self.poscar.atoms):
            for j, atom2 in enumerate(self.poscar.atoms):
                if i != j and self.is_bonded(atom1, atom2):
                    graph.add_edge(i, j)

        # Find connected components (molecules)
        connected_components = nx.connected_components(graph)

        # Label molecule groups
        for component in connected_components:
            molecule = {}
            for index in component:
                atom_type = self.poscar.atoms[index].element
                molecule[atom_type] = molecule.get(atom_type, 0) + 1

            # Use atom types and counts as keys
            molecule_key = frozenset(molecule.items())
            if molecule_key not in self.molecule_groups:
                self.molecule_groups[molecule_key] = []
            self.molecule_groups[molecule_key].extend(component)

        return self.molecule_groups


#
# 以上面代码为基础， 实现以下功能:
# 太强了，再额外增加一个需求，根据分子类型从poscar类的原子库删除该分子类型的全部原子
# ，但是删除分子的前提如下：1.分子中原子不允许有fixed的  2.分子原子个数不允许超过警戒值比如8
# 并且将删除的分子种类和所删的个数放到一个文本文件中储存,推荐yaml格式比较容易提取以便分析，当然这个可以自己把握。


if __name__ == "__main__":

    # poscar0.remove_molecules(max_atoms=3, output_file="removed_molecules.yaml")
    # 假设你已经有一个POSCAR对象，名为poscar
    poscar = POSCAR("CONTCAR(2)", filetype="CONTCAR")
    poscar.display()
    # 小于等于8个就删除
    # Remove molecules based on the criteria and save information to a YAML file
    poscar.remove_molecules(max_atoms=22, fixed_threshold=1, output_file="removed_molecules.yaml")
    poscar.display()

    # molecule_identifier = MoleculeIdentifier(poscar)
    # molecule_groups = molecule_identifier.identify_molecules()
    #
    # # 打印分子群
    # for molecule, indices in molecule_groups.items():
    #     print(f"Molecule: {dict(molecule)}, Atom indices: {indices}")

    # Molecule: {'F': 1}, Atom
    # indices: [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 29, 30, 32, 33, 35]
    # Molecule: {'F': 1}
    # 表示这个分子群由单个氟原子组成。
    # Atom
    # indices: [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 29, 30, 32, 33, 35]
    # 表示这个分子群包含了atoms列表中索引为0, 1, 2, 3, ...
    # 的原子。


    # # Example usage:
    #
    # # Initialize the parser with the path to the XDATCAR file
    # parser = XDATCARParser("XDATCAR(1)(1)")
    #
    # # Parse the file
    # parser._parse()
    #
    # # Save the first frame to a file named "POSCAR0"
    # parser.save_specific_frame(10, name="POSCAR10")
    #
    # # Print the number of atoms in the first frame
    # print(parser.count_atoms_at_specific_frame(0))