# Project 3 – Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section: 
# classes and functionalities will be provided here
from __future__ import annotations


class Division:
    def __init__(self, id: int, division_name: str):
        self.id = id
        self.division_name = division_name

    def __repr__(self) -> str:
        return "Division(id={}, division_name='{}')".format(self.id, self.division_name)


class Graduate:
    def __init__(
        self,
        id: int,
        major: str,
        bachelor: tuple[int, int],
        master: tuple[int, int],
        doctor: tuple[int, int],
    ):
        self.id = id
        self.major = major
        self.bachelor = bachelor      # (female, male)
        self.master = master          # (female, male)
        self.doctor = doctor          # (female, male)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graduate):
            return False
        return (
            self.bachelor == other.bachelor
            and self.master == other.master
            and self.doctor == other.doctor
        )

    def __repr__(self) -> str:
        return (
            "Graduate(id={}, major='{}', bachelor={}, master={}, doctor={})"
            .format(self.id, self.major, self.bachelor, self.master, self.doctor)
        )


def _safe_int(s: str) -> int:
    s = s.strip()
    return 0 if s == "" else int(s)


# Design Recipe
# Input: file_name (str)
# Output: tuple[list[str], list[str]]
# Purpose: Read file and return the 3 header lines and the remaining data lines.
def read_file(file_name: str) -> tuple[list[str], list[str]]:
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    header = lines[:3]
    data = lines[3:]
    return header, data


# Design Recipe
# Input: list_str (list[str])
# Output: list[Division]
# Purpose: Create a list of Division objects from the division rows (IDs ending in 00).
def create_division(list_str: list[str]) -> list[Division]:
    divisions: list[Division] = []
    seen: set[int] = set()
    for line in list_str:
        parts = [x.strip() for x in line.strip().split(",")]
        if len(parts) < 2:
            continue
        try:
            id_num = int(parts[0])
        except ValueError:
            continue
        if id_num % 100 == 0 and id_num not in seen:
            div_name = parts[1]
            divisions.append(Division(id_num, div_name))
            seen.add(id_num)
    return divisions


# Design Recipe
# Input: list_str (list[str])
# Output: list[Graduate]
# Purpose: Create a list of Graduate objects from major rows (IDs not ending in 00).
def create_graduate(list_str: list[str]) -> list[Graduate]:
    grads: list[Graduate] = []
    seen_major_ids: set[int] = set()

    for line in list_str:
        parts = [x.strip() for x in line.strip().split(",")]
        if len(parts) < 2:
            continue
        try:
            id_num = int(parts[0])
        except ValueError:
            continue
        if id_num % 100 == 0:
            continue
        if id_num in seen_major_ids:
            continue
        seen_major_ids.add(id_num)
        major = parts[1]
        def get(i: int) -> str:
            return parts[i] if i < len(parts) else ""
        bach_male = _safe_int(get(2))
        bach_female = _safe_int(get(3))
        mast_male = _safe_int(get(4))
        mast_female = _safe_int(get(5))
        doc_male = _safe_int(get(6))
        doc_female = _safe_int(get(7))
        bachelor = (bach_female, bach_male)
        master = (mast_female, mast_male)
        doctor = (doc_female, doc_male)
        grads.append(Graduate(id_num, major, bachelor, master, doctor))
    return grads


# Design Recipe
# Input: lst_div_obj (list[Division]), lst_grad_obj (list[Graduate])
# Output: None
# Purpose: Create one CSV file per division with totals per major (female+male) for each degree.
def create_files(list_str: list[Division], lst_grad_obj: list[Graduate], lst_div_obj=None) -> None:
    first_line = 'This table shows '
    second_line = 'id,major,bachelor,master,doctor'
    for div in lst_div_obj:
        words = div.division_name.split()
        first_word = words[0]
        filename=first_word + ".csv"
        file=open(filename, "w", encoding="utf-8")
        file.write(first_line + "\n")
        file.write(second_line + "\n")
        for g in lst_grad_obj:
            if g.id//100==div.di//100:
                bachelor = g.bachelor[0]+g.bachelor[1]
                master = g.master[0]+g.master[1]
                doctor = g.doctor[0]+g.doctor[1]
                line = str(g.id)+" " + str(g.major) + " " + str(bachelor) + " " + str(master) + " " + str(doctor)
                file.write(line + "\n")
        file.close()

#input:division_name (str)
#output:tuple[int, float]
#example:find_total_avg_of_division("Agriculture") -> (total, average)

def find_total_avg_of_division (division_name: str) -> tuple:
    words = division_name.split()
    first_word = words[0]
    filename=first_word+".csv"
    file = open(filename)
    lines = file.readlines()
    file.close()
    total = 0
    count = 0
    for i in range(2, len(lines)):
        parts = lines[i].split()
        if len(parts) >= 5:
            bachelor = int(parts[2])
            master = int(parts[3])
            doctor = int(parts[4])
            total = total + bachelor + master + doctor
            count = count + 1
        if count==0:
            average =0.0
        else:
            average = total/count
        return total, average
    return None


# Input: lst_grad_obj (list[Graduate])
# Output: tuple[int, float]
# Example: find_graduate_total_avg(graduates) -> (total, average)
def find_graduate_total_avg(lst_grad_obj: list[Graduate]) -> tuple[int, float]:
    total = 0
    count = 0
    for g in lst_grad_obj:
        bachelor_total = g.bachelor[0] + g.bachelor[1]
        master_total = g.master[0] + g.master[1]
        doctor_total = g.doctor[0] + g.doctor[1]
        total = total + bachelor_total + master_total + doctor_total
        count = count + 1
    if count == 0:
        average = 0.0
    else:
        average = total / count
    return total, average