from dataclasses import dataclass, field


@dataclass
class PujanNeupane:
    role: str = "AI/ML Engineer"
    company: str = "Cyber Alert Nepal"
    education: str = "Computer Engineering @ IOE Purwanchal Campus"
    focus: list[str] = field(default_factory=lambda: [
        "Deepfake Detection",
        "NLP",
        "Computer Vision",
        "Full-Stack AI Systems",
    ])
    stack: list[str] = field(default_factory=lambda: [
        "Python",
        "PyTorch",
        "FastAPI",
        "React",
        "Docker",
    ])

    def currently_building(self) -> str:
        return f"Production AI/ML systems @ {self.company}"

    def open_to_collab(self) -> str:
        return "AI/ML research, OSS projects, and impactful products"

    def fun_fact(self) -> str:
        return "I debug with coffee and deploy with optimism."


me = PujanNeupane()
print(me.currently_building())
