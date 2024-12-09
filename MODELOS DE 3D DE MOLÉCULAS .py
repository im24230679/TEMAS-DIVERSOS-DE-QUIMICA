from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

def visualize_molecule(smiles, name):
    # Generar la molécula desde SMILES
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)  # Añadir hidrógenos explícitos
    AllChem.EmbedMolecule(mol)  # Generar conformación inicial
    AllChem.UFFOptimizeMolecule(mol)  # Optimizar geometría

    # Convertir la molécula a formato 3D mol
    mol_block = Chem.MolToMolBlock(mol)

    # Visualizar con py3Dmol
    viewer = py3Dmol.view(width=400, height=300)
    viewer.addModel(mol_block, "mol")  # Agregar el modelo 3D
    viewer.setStyle({"stick": {}})  # Estilo de varilla
    viewer.zoomTo()  # Ajustar zoom
    viewer.setBackgroundColor("white")
    print(f"Modelo para {name}:")
    return viewer.show()

# Lista de moléculas con sus nombres y SMILES
molecules = [
    ("Agua", "O"),
    ("Etanol", "CCO"),
    ("Ciclohexano", "C1CCCCC1"),
    ("Ácido acético", "CC(=O)O"),
    ("Benceno", "C1=CC=CC=C1"),
    ("Metano", "C"),
    ("Metanol", "CO"),
    ("Etano", "CC"),
    ("Propano", "CCC"),
    ("Butano", "CCCC"),
    ("Acetona", "CC(=O)C"),
    ("Glicina", "C(C(=O)O)N"),
    ("Alanina", "CC(C(=O)O)N"),
    ("Fenol", "C1=CC=C(C=C1)O"),
    ("Tetrahidrofurano", "C1CCOCC1"),
    ("Etanolamina", "NCCO"),
    ("Ácido aspártico", "C(C(=O)O)(N)C(=O)O"),
    ("Trietilamina", "CCN(CC)CC"),
    ("Dietil éter", "CCOCC"),
    ("Ácido láctico", "C(C(=O)O)O"),
    ("Naftaleno", "C1=CC=C2C=CC=CC2=C1"),
    ("Dimetilformamida", "CN(C)C=O"),
    ("Ácido cítrico", "C(C(=O)O)(C(=O)O)O")
]

# Generar visualizaciones
for name, smiles in molecules:
    visualize_molecule(smiles, name)
