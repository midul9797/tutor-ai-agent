from gemini import ask_gemini
PHYSICS_CONSTANTS = {
    "speed of light": "3.0 x 10^8 m/s",
    "gravitational constant": "6.674 x 10^-11 N·m²/kg²",
    "planck constant": "6.626 x 10^-34 J·s",
    "elementary charge": "1.602 x 10^-19 C",
    "avogadro's number": "6.022 x 10^23 mol⁻¹",
    "boltzmann constant": "1.381 x 10^-23 J/K",
    "gas constant": "8.314 J/(mol·K)",
    "electron mass": "9.109 x 10^-31 kg",
    "proton mass": "1.673 x 10^-27 kg",
    "neutron mass": "1.675 x 10^-27 kg",
    "permittivity of free space": "8.854 x 10^-12 F/m",
    "permeability of free space": "4π x 10^-7 N/A²",
    "stefan-boltzmann constant": "5.670 x 10^-8 W/(m²·K⁴)",
    "coulomb's constant": "8.988 x 10^9 N·m²/C²",
    "rydberg constant": "1.097 x 10^7 m⁻¹",
    "hubble constant": "70 km/s/Mpc",
    "fine-structure constant": "1/137",
    "standard atmospheric pressure": "101325 Pa",
    "atomic mass unit": "1.6605 x 10^-27 kg",
    "universal mass-energy equivalence (E=mc²)": "9 x 10^16 J/kg"
}

class PhysicsAgent:
    def lookup_constant(self, query: str) -> str:
        for name in PHYSICS_CONSTANTS:
            if name in query.lower():
                return f"{name}: {PHYSICS_CONSTANTS[name]}"
        return None

    def handle_query(self, query: str) -> str:
        constant_info = self.lookup_constant(query)
        if constant_info:
            gemini_prompt = (
                f"A student asked: '{query}'. This involves the constant: {constant_info}. "
                "Explain it in context."
            )
        else:
            gemini_prompt = f"A student asked a physics question: '{query}'. Help the student with a clear explanation and solve it if needed."
        return ask_gemini(gemini_prompt)