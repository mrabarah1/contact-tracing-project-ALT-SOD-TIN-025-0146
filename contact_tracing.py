### Student Name: Abarah Lawrence Emeka

### Learner ID: ALT/SOD/TIN/025/0146

### Track: Data Engineering

### Mini Project: Contact Tracing System

infection_status = {
    "Bayo": False,
    "Wale": True,
    "Tolu": False,
    "Bisiola": False,
    "Ibrahim": True,
    "Mike": True,
    "Tinubu": False,
}


#Rules:
# Duration must be greater than 0
# A person cannot have contact with themselves
# Contacts are not directional (Alice–Bob = Bob–Alice)
# Multiple contact events between the same people are allowed
contact_events = [
    ("Bayo", "Wale", 15),
    ("Tolu", "Bisiola", 30),
    ("Ibrahim", "Mike", 45),
    ("Wale", "Tolu", 20),
    ("Bisiola", "Ibrahim", 10),
    ("Mike", "Tinubu", 25),
]


def add_person(name: str, infected: bool):
    """Clean the name and updates the global infection_status""" 
    clean_name = name.strip()
    #Add the person if they do not exist
    is_new = clean_name not in infection_status
    
    #Update infection status if the person already exists
    infection_status[clean_name] = infected
    return is_new

print(add_person("tola", True)) 


def add_contact(person1: str, person2: str, duration: int):
    """Validates and stores contact events.
    Adds missing people to the system as non-infcted by default"""
    # Clean the names
    p1 = person1.strip()
    p2 = person2.strip()
    
    # Validate duration
    if duration <= 0:
        return "Invalid duration"
    # Validate that person1 and person2 are not the same
    if p1 == p2:
        return "A person cannot have contact with themselves"
    # Add missing people as Not infected(false)
    if p1 not in infection_status:
        add_person(p1, False)
    if p2 not in infection_status:
        add_person(p2, False)
    
    # Store the contact event in a list
    contact_events.append((p1, p2, duration))
    
    
    
def get_high_risk_contacts() -> list:
    exposure_map = {}
    
    for p1, p2, duration in contact_events:
        #Determine who is infected
        p1_inf = infection_status.get(p1)
        p2_inf = infection_status.get(p2)
        
        # case1: person1 is exposed to infected person2
        if not p1_inf and p2_inf:
            key = (p1, p2)
        # pair = tuple(sorted([person1, person2]))
            exposure_map[key] = exposure_map.get(key, 0) + duration
        
        # case2: person2 is exposed to infected p1
        elif not p2_inf and p1_inf:
            key = (p2, p1)
            exposure_map[key] = exposure_map.get(key, 0) + duration
        
        #filter for >= 15 mins and sort by the high_risk_list =[]
        # and return sorted(high_risk_list, key=lambda x: x[2], reverse=True)
        high_risk_list = [
            (exposed, infected, time)
            for (exposed, infected), time in exposure_map.items()
            if time >= 15
        ]
        high_risk_list.sort(key=lambda x: x[2], reverse=True)
        return high_risk_list
    

def print_report():
    # calculate stats and prints the exposure report
    high_risk = get_high_risk_contacts()
    infected_count = sum(1 for status in infection_status.values() if status)
    print("Exposure Report")
    print("----------------")
    print(f"Total People: {len(contact_events)}")
    print(f"Total Contact Events: {len(contact_events)}")
    print(f"Infected People: {infected_count}")
    print(f"High Risk Individuals: {len(high_risk)}")
    print(f"Top Exposures: ")
    
    for exposed, infected, time in high_risk:
        print(f" - {exposed} exposed to {infected} for {time} minutes")
        
        

# sample data for testing
if __name__ == "__main__":
    add_person("Yemi", True)
    add_person("Titi", False)
    add_contact("Yemi", "Titi", 20)
    add_contact("Emeka", "Yemi", 10)
    add_contact("Titi", "Emeka", 25)
    add_contact("Titi", "Titi", 17)
    print_report()