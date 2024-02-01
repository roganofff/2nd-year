from abc import ABC, abstractmethod
from typing import Optional


class Education(ABC):
    years: int
    qualification: str
    
    @abstractmethod
    def __init__(self, years: Optional[int], qualification: Optional[str] = None) -> None:
        if years is not None:
            self.years = years
        if qualification is not None:
            self.qualification = qualification

class HigherEducation(Education):
    years = 5
    qualification = 'bachelor'

    def __init__(self, years: Optional[int], qualification: Optional[str] = None) -> None:
        super().__init__(years, qualification)

class ProfessionalEducation(Education):
    years = 4
    qualification = 'operator'

    def __init__(self, years: Optional[int], qualification: Optional[str] = None) -> None:
        super().__init__(years, qualification)

class College:
    def __init__(self, title: str, education: Education) -> None:
        self.title = title
        self.education = education

class CollegeCreator(ABC):
    @abstractmethod
    def create(self, title: str, years: Optional[int] = None) -> College:
        pass

class RUCollegeCreator(CollegeCreator):
    def create(self, title: str, years: Optional[int] = None) -> College:
        return College(title, ProfessionalEducation(years=years))
    
print(RUCollegeCreator().create('Sirius').education.years)