from contact_tracing import add_contact, contact_events

def test_invalid_duration():
    # Attempt to add a contact with 0 minutes
    initial_length = len(contact_events)
    add_contact("Alice", "Bob", 0)
    
    if len(contact_events) == initial_length:
        print("Test Passed: Invalid duration was correctly ignored.")
    else:
        print("Test Failed: Invalid duration was added to the list.")

if __name__ == "__main__":
    test_invalid_duration()