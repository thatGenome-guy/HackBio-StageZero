"""
Team Tyrosine Info Collector
HackBio Internship Task 1
Author: Oduola David

Description:
This script collects, validates, and displays information about team members.
It supports DNA validation, translation into protein sequences, and optional
Hamming distance computation for comparison between sequences.
"""

from typing import List, Dict


class TeamMember:
    """
    Represents a member of Team Tyrosine with biological and personal details.
    """

    def init(self, name: str, slack: str, country: str, hobby: str,
                 affiliations: str, gene: str, dna: str,
                 github: str, linkedin: str):
        self.name = name
        self.slack = slack
        self.country = country
        self.hobby = hobby
        self.affiliations = affiliations
        self.gene = gene
        self.dna = dna.upper().strip()
        self.github = github
        self.linkedin = linkedin

    def validate_dna(self) -> bool:
        """Ensures that the DNA sequence contains only valid nucleotides (A, T, C, G)."""
        valid_bases = {'A', 'T', 'C', 'G'}
        return all(base in valid_bases for base in self.dna)

    def translate_dna(self) -> str:
        """Translates DNA sequence into amino acids using codon mapping."""
        codon_table: Dict[str, str] = {
            "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
            "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
            "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
            "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
            "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
            "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
            "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
            "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
            "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
            "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
            "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
            "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
            "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
            "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
            "TAC": "Y", "TAT": "Y",
            "TAA": "Stop", "TAG": "Stop", "TGA": "Stop",
            "TGC": "C", "TGT": "C", "TGG": "W"
        }

        protein_seq = ""
        try:
            for i in range(0, len(self.dna) - 2, 3):
                codon = self.dna[i:i + 3]
                amino_acid = codon_table.get(codon, "")
                if amino_acid == "Stop":
                    break
                protein_seq += amino_acid
        except Exception:
            return "Error during translation: invalid DNA format."

        return protein_seq or "No valid translation available."

    def display_info(self) -> None:
        """Displays member information in a structured format."""
        print("\n===== TEAM TYROSINE MEMBER INFO =====")
        print(f"Name: {self.name}")
        print(f"Slack Username: {self.slack}")
        print(f"Country: {self.country}")
        print(f"Hobby: {self.hobby}")
        print(f"Affiliations: {self.affiliations}")
        print(f"Favorite Gene: {self.gene}")
        print(f"DNA Sequence: {self.dna}")
        print(f"Protein Translation: {self.translate_dna()}")
        print(f"GitHub: {self.github}")
        print(f"LinkedIn: {self.linkedin}")
        print("=====================================\n")


def hamming_distance(seq1: str, seq2: str) -> str:
    """Computes the Hamming distance between two DNA sequences."""
    if len(seq1) != len(seq2):
        return "Sequences must be of equal length for comparison."
    return str(sum(base1 != base2 for base1, base2 in zip(seq1, seq2)))


def collect_team_data() -> List[TeamMember]:
    """Collects data for multiple team members with validation."""
    team: List[TeamMember] = []
    print("Welcome to Team Tyrosine Info Collector\n")
while True:
        try:
            num_members = int(input("Enter the number of team members: "))
            if num_members < 1:
                print("⚠️ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

    for i in range(num_members):
        print(f"\n--- Enter details for member {i + 1} ---")
        name = input("Enter your name: ").strip()
        slack = input("Enter your Slack username: ").strip()
        country = input("Enter your country: ").strip()
        hobby = input("Enter your hobby: ").strip()
        affiliations = input("Enter your affiliations: ").strip()
        gene = input("Enter your favorite gene: ").strip()
        dna = input("Enter the DNA sequence: ").strip().upper()
        github = input("Enter your GitHub link:").strip()
        linkedin = input("Enter your LinkedIn link:").strip()

        member = TeamMember(name, slack, country, hobby, affiliations, gene, dna, github, linkedin)

        if not member.validate_dna():
            print("⚠️ Invalid DNA sequence detected! Only A, T, C, and G are allowed.")
        team.append(member)

    return team


def display_team(team: List[TeamMember]) -> None:
    """Displays all team members’ information."""
    print("\n=========== TEAM TYROSINE SUMMARY ===========")
    for member in team:
        member.display_info()
    print("=============================================\n")


if name == "main":
    team_members = collect_team_data()
    display_team(team_members)

    if len(team_members) >= 2:
        seq1 = team_members[0].dna
        seq2 = team_members[1].dna
        print(f"Hamming Distance between {team_members[0].name} and {team_members[1].name}: {hamming_distance(seq1, seq2)}")

    # Represent team as list of dictionaries for clarity and data export
    team_data: List[Dict[str, str]] = [
        {
            "Name": m.name,
            "Slack": m.slack,
            "Country": m.country,
            "Hobby": m.hobby,
            "Affiliations": m.affiliations,
            "Favorite Gene": m.gene,
            "DNA": m.dna,
            "Protein": m.translate_dna(),
            "GitHub": m.github,
            "LinkedIn": m.linkedin
        } for m in team_members
    ]

    print("\nTeam data structure (for verification):")
    print(team_data)
