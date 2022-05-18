#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base

# Internal
from addons.general_category import general_category

# External
import sqlalchemy.exc


class CatFiller:
    cats = {
        'Computer science': {
            'cs.AI': 'Artificial Intelligence',
            'cs.AR': 'Hardware Architecture',
            'cs.CC': 'Computational Complexity',
            'cs.CE': 'Computational Engineering, Finance, and Science',
            'cs.CG': 'Computational Geometry',
            'cs.CL': 'Computation and Language',
            'cs.CR': 'Cryptography and Security',
            'cs.CV': 'Computer Vision and Pattern Recognition',
            'cs.CY': 'Computers and Society',
            'cs.DB': 'Databases',
            'cs.DC': 'Distributed, Parallel, and Cluster Computing',
            'cs.DL': 'Digital Libraries',
            'cs.DM': 'Discrete Mathematics',
            'cs.DS': 'Data Structures and Algorithms',
            'cs.ET': 'Emerging Technologies',
            'cs.FL': 'Formal Languages and Automata Theory',
            'cs.GL': 'General Literature',
            'cs.GR': 'Graphics',
            'cs.GT': 'Computer Science and Game Theory',
            'cs.HC': 'Human-Computer Interaction',
            'cs.IR': 'Information Retrieval',
            'cs.IT': 'Information Theory',
            'cs.LG': 'Machine Learning',
            'cs.LO': 'Logic in Computer Science',
            'cs.MA': 'Multiagent Systems',
            'cs.MM': 'Multimedia',
            'cs.MS': 'Mathematical Software',
            'cs.NA': 'Numerical Analysis',
            'cs.NE': 'Neural and Evolutionary Computing',
            'cs.NI': 'Networking and Internet Architecture',
            'cs.OH': 'Other Computer Science',
            'cs.OS': 'Operating Systems',
            'cs.PF': 'Performance',
            'cs.PL': 'Programming Languages',
            'cs.RO': 'Robotics',
            'cs.SC': 'Symbolic Computation',
            'cs.SD': 'Sound',
            'cs.SE': 'Software Engineering',
            'cs.SI': 'Social and Information Networks',
            'cs.SY': 'Systems and Control',
        },

        'Economics': {
            'econ.EM': 'Econometrics',
            'econ.GN': 'General Economics',
            'econ.TH': 'Theoretical Economics',
        },

        'Electrical Engineering and Systems Science': {
            'eess.AS': 'Audio and Speech Processing',
            'eess.IV': 'Image and Video Processing',
            'eess.SP': 'Signal Processing',
            'eess.SY': 'Systems and Control',
        },

        'Mathematics': {
            'math.AC': 'Commutative Algebra',
            'math.AG': 'Algebraic Geometry',
            'math.AP': 'Analysis of PDEs',
            'math.AT': 'Algebraic Topology',
            'math.CA': 'Classical Analysis and ODEs',
            'math.CO': 'Combinatorics',
            'math.CT': 'Category Theory',
            'math.CV': 'Complex Variables',
            'math.DG': 'Differential Geometry',
            'math.DS': 'Dynamical Systems',
            'math.FA': 'Functional Analysis',
            'math.GM': 'General Mathematics',
            'math.GN': 'General Topology',
            'math.GR': 'Group Theory',
            'math.GT': 'Geometric Topology',
            'math.HO': 'History and Overview',
            'math.IT': 'Information Theory',
            'math.KT': 'K-Theory and Homology',
            'math.LO': 'Logic',
            'math.MG': 'Metric Geometry',
            'math.MP': 'Mathematical Physics',
            'math.NA': 'Numerical Analysis',
            'math.NT': 'Number Theory',
            'math.OA': 'Operator Algebras',
            'math.OC': 'Optimization and Control',
            'math.PR': 'Probability',
            'math.QA': 'Quantum Algebra',
            'math.RA': 'Rings and Algebras',
            'math.RT': 'Representation Theory',
            'math.SG': 'Symplectic Geometry',
            'math.SP': 'Spectral Theory',
            'math.ST': 'Statistics Theory',
        },

        'Physics': {
            'acc-phys': 'Accelerator Physics',
            'astro-ph.CO': 'Cosmology and Nongalactic Astrophysics',
            'astro-ph.EP': 'Earth and Planetary Astrophysics',
            'astro-ph.GA': 'Astrophysics of Galaxies',
            'astro-ph.HE': 'High Energy Astrophysical Phenomena',
            'astro-ph.IM': 'Instrumentation and Methods for Astrophysics',
            'astro-ph.SR': 'Solar and Stellar Astrophysics',
            'cond-mat.dis-nn': 'Disordered Systems and Neural Networks',
            'cond-mat.mes-hall': 'Mesoscale and Nanoscale Physics',
            'cond-mat.mtrl-sci': 'Materials Science',
            'cond-mat.other': 'Other Condensed Matter',
            'cond-mat.quant-gas': 'Quantum Gases',
            'cond-mat.soft': 'Soft Condensed Matter',
            'cond-mat.stat-mech': 'Statistical Mechanics',
            'cond-mat.str-el': 'Strongly Correlated Electrons',
            'cond-mat.supr-con': 'Superconductivity',
            'gr-qc': 'General Relativity and Quantum Cosmology',
            'hep-ex': 'High Energy Physics - Experiment',
            'hep-lat': 'High Energy Physics - Lattice',
            'hep-ph': 'High Energy Physics - Phenomenology',
            'hep-th': 'High Energy Physics - Theory',
            'math-ph': 'Mathematical Physics',
            'nlin.AO': 'Adaptation and Self-Organizing Systems',
            'nlin.CD': 'Chaotic Dynamics',
            'nlin.CG': 'Cellular Automata and Lattice Gases',
            'nlin.PS': 'Pattern Formation and Solitons',
            'nlin.SI': 'Exactly Solvable and Integrable Systems',
            'nucl-ex': 'Nuclear Experiment',
            'nucl-th': 'Nuclear Theory',
            'physics.acc-ph': 'Accelerator Physics',
            'physics.ao-ph': 'Atmospheric and Oceanic Physics',
            'physics.app-ph': 'Applied Physics',
            'physics.atm-clus': 'Atomic and Molecular Clusters',
            'physics.atom-ph': 'Atomic Physics',
            'physics.bio-ph': 'Biological Physics',
            'physics.chem-ph': 'Chemical Physics',
            'physics.class-ph': 'Classical Physics',
            'physics.comp-ph': 'Computational Physics',
            'physics.data-an': 'Data Analysis, Statistics and Probability',
            'physics.ed-ph': 'Physics Education',
            'physics.flu-dyn': 'Fluid Dynamics',
            'physics.gen-ph': 'General Physics',
            'physics.geo-ph': 'Geophysics',
            'physics.hist-ph': 'History and Philosophy of Physics',
            'physics.ins-det': 'Instrumentation and Detectors',
            'physics.med-ph': 'Medical Physics',
            'physics.optics': 'Optics',
            'physics.plasm-ph': 'Plasma Physics',
            'physics.pop-ph': 'Popular Physics',
            'physics.soc-ph': 'Physics and Society',
            'physics.space-ph': 'Space Physics',
            'quant-ph': 'Quantum Physics',

        },

        'Quantitative Biology': {
            'q-bio.BM': 'Biomolecules',
            'q-bio.CB': 'Cell Behavior',
            'q-bio.GN': 'Genomics',
            'q-bio.MN': 'Molecular Networks',
            'q-bio.NC': 'Neurons and Cognition',
            'q-bio.OT': 'Other Quantitative Biology',
            'q-bio.PE': 'Populations and Evolution',
            'q-bio.QM': 'Quantitative Methods',
            'q-bio.SC': 'Subcellular Processes',
            'q-bio.TO': 'Tissues and Organs',
        },

        'Quantitative Finance': {
            'q-fin.CP': 'Computational Finance',
            'q-fin.EC': 'Economics',
            'q-fin.GN': 'General Finance',
            'q-fin.MF': 'Mathematical Finance',
            'q-fin.PM': 'Portfolio Management',
            'q-fin.PR': 'Pricing of Securities',
            'q-fin.RM': 'Risk Management',
            'q-fin.ST': 'Statistical Finance',
            'q-fin.TR': 'Trading and Market Microstructure',
        },

        'Statistics': {
            'stat.AP': 'Applications',
            'stat.CO': 'Computation',
            'stat.ME': 'Methodology',
            'stat.ML': 'Machine Learning',
            'stat.OT': 'Other Statistics',
            'stat.TH': 'Statistics Theory',
        },

    }

    def __init__(self, db):
        self.db = db

    def run(self, table_base, table_cat, table_cat_general):
        unpack_dict = self.unpack_base(table_base)
        self.unpack(table_cat, unpack_dict)
        self.unpack_general(table_cat_general)

    def unpack(self, table, unpack_dict):
        db_list = []

        i = 1
        for cat_key in self.cats.keys():
            for cat in self.cats[cat_key].keys():
                cat_id = unpack_dict[cat_key]

                db_dict = {
                    'id': i,
                    'base_id': cat_id,
                    'category': cat,
                    'description': self.cats[cat_key][cat]
                }

                db_list.append(db_dict)

                i += 1

        try:
            self.db.insert(table, db_list)
        except sqlalchemy.exc.IntegrityError as e:
            print(e)

    def unpack_base(self, table):
        id_dict = {}
        db_list = []

        for cat_key_pair in enumerate(self.cats.keys(), start=1):
            id_dict[cat_key_pair[1]] = cat_key_pair[0]

            db_dict = {
                'id': cat_key_pair[0],
                'base_category': cat_key_pair[1]
            }

            db_list.append(db_dict)

        try:
            self.db.insert(table, db_list)
        except sqlalchemy.exc.IntegrityError as e:
            print(e)
        return id_dict

    def unpack_general(self, table):
        id_dict = {}
        db_list = []

        cat_set = set()

        for global_cat in self.cats.keys():
            for cat in self.cats[global_cat].keys():
                cat_set.add(general_category([cat])[0])

        for cat in enumerate(cat_set, start=1):
            db_dict = {
                'id': cat[0],
                'category': cat[1],
                'description': ' - '
            }

            db_list.append(db_dict)

        try:
            self.db.insert(table, db_list)
        except sqlalchemy.exc.IntegrityError as e:
            print(e)

        return id_dict


if __name__ == '__main__':
    from db.db_connection.db_local import LocalConnectDB
    from db.db_connection.db_external import ExternalConnectDB

    from db.db_init.db_init_base import BaseBase, base_name
    from db.db_init.db_init_base import BaseList, CatList, GeneralCatList

    config_path = r'E:\Projects\NeuralDiploma\conf\project.cfg'

    db_loc = LocalConnectDB(BaseBase, base_name, config_path)
    # db_ext = ExternalConnectDB(BaseBase, base_name, config_path)

    filler = CatFiller(db_loc)

    filler.run(BaseList, CatList, GeneralCatList)
